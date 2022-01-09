# IMPORTS
import json
import os
import re
import time
from functools import lru_cache
from multiprocessing.pool import ThreadPool as Pool

import requests
from bs4 import BeautifulSoup


# FUNCTIONS
def get_html(url: str) -> str:
    """
    Get HTML from URL

    :param url: URL t process
    :return: HTML in str format
    """
    r = requests.get(url, timeout=None)
    return r.text


@lru_cache
def get_soup(url: str) -> BeautifulSoup:
    """
    Get BeautifulSoup from page

    :param url: Page for process
    :return: BeautifulSoup object
    """

    return BeautifulSoup(get_html(url), "lxml")


def get_main_page_link(url: str, domain_zone: str) -> str:
    """
    Get website main page from URL

    :param url: URL to find its main page
    :param domain_zone: Domain zone (like ".com")
    :return: Main page URL
    """

    return url.split(domain_zone)[0] + domain_zone


@lru_cache
def get_pages_list(main_url: str, main_page: str) -> list:
    """
    Get all links from alphabetic menu from the top of the page

    :param main_url: First page
    :param main_page: Main page of the website
    :return: List with links for all the pages
    """

    soup = get_soup(main_url)
    pages_menu = soup.find_all("a", class_="tab__subnav__item")[1:]

    return [main_page + a.get("href") for a in pages_menu]


def get_links(soup: BeautifulSoup) -> list:
    """
    Get all relative link for each company from page with companies list

    :param soup: BeautifulSoup from companies list page
    :return: List of relative links
    """

    row_links = soup.find("tbody", class_="table__tbody").find_all(
        "a", href=True
    )
    return [a["href"] for a in row_links]


def get_growth(soup: BeautifulSoup) -> list:
    """
    Get growth value from companies list page for each company

    :param soup: BeautifulSoup from companies list page
    :return: List with growth values
    """

    row_links = soup.find_all("td", class_="table__td")[7::8]
    return [a.select("span:last-child")[-1].text for a in row_links]


def get_company_data(link: str, main_page: str, usd: float) -> dict:
    """
    Get required data from company page

    :param link: Relative link of company page
    :param main_page: Main page of the website
    :param usd: Dollar rate in rubles
    :return: Dict with company information
    """

    company_info = {}
    soup = get_soup(main_page + link)
    data = soup.find("main", class_="site-content")

    name = data.findChildren(
        "span", class_="price-section__label", recursive=True
    )[0].text.strip()
    code = (
        data.findChildren(
            "span", class_="price-section__category", recursive=True
        )[0]
        .text.split(",")[-1]
        .strip()
    )
    price = data.findChildren(
        "span", class_="price-section__current-value", recursive=True
    )[0].text.replace(",", "")

    try:
        pe = (
            data.find("div", text=re.compile("P/E Ratio"))
            .parent.text.split("\r")[1]
            .strip()
            .replace(",", "")
        )
    except AttributeError:
        pe = "inf"

    try:
        low_52 = (
            data.find("div", text=re.compile("52 Week Low"))
            .parent.text.split("\r")[1]
            .strip()
            .replace(",", "")
        )
    except AttributeError:
        low_52 = None

    try:
        high_52 = (
            data.find("div", text=re.compile("52 Week High"))
            .parent.text.split("\r")[1]
            .strip()
            .replace(",", "")
        )
    except AttributeError:
        high_52 = None

    potential_profit = "-inf"
    if high_52 and low_52:
        potential_profit = (
            f"{(float(high_52) - float(low_52)) / float(low_52) :.2%}"
        )

    company_info["name"] = name
    company_info["code"] = code
    company_info["price"] = round(float(price) * usd, 2)
    company_info["p/e"] = pe
    company_info["potential profit"] = potential_profit
    return company_info


def append_company_data(raw_dict: dict, main_page: str, usd: float) -> None:
    """
    Wrapper func to use with parallelization.
    Updates existing dict with links and growth
    using get_company_data func

    :param raw_dict: Existing dict with links
    :param main_page: Main page of the website
    :param usd: Dollar rate in rubles
    """

    global CNT
    add_data = get_company_data(raw_dict["link"], main_page, usd)
    raw_dict.update(add_data)
    if CNT % 10 == 0:
        print("|", end="")
    CNT += 1


@lru_cache
def get_usd_rate() -> float:
    """
    Get current USD rate from CBR website

    :return: Dollar rate in rubles
    """

    link = "https://www.cbr.ru/scripts/XML_daily.asp"
    soup = get_soup(link)

    return float(soup.find("valute", id="R01235").value.text.replace(",", "."))


def top_ten(data: list, sort_key: str, reverse: bool = True) -> list:
    """
    Sorts list of dicts using dict[sort_key] values as a sort key
    and returns first 10 elements

    :param data: List of dicts for sorting
    :param sort_key: Dict key for sort by its values
    :param reverse: Trigger to choose direction of sorting
    :return: First 10 elements of data sorted
    """

    if sort_key in ("growth", "potential profit"):
        func = (
            lambda d: float(d[sort_key][:-1]) / 100
            if d[sort_key] not in ("-inf", "inf")
            else float(d[sort_key])
        )
    else:
        func = lambda d: float(d[sort_key])
    return sorted(data, key=func, reverse=reverse)[:10]


def get_clear_data(data: list) -> list:
    """
    Deletes unnecessary information from dicts in list
    before saving in json

    :param data: List of dicts with companies info
    :return: List of cleared dicts
    """

    items = ("code", "name", "price", "p/e", "growth", "potential profit")
    new_data = []
    for d in data:
        new_d = {}
        for item in items:
            new_d[item] = d[item]
        new_data.append(new_d)
    return new_data


def dump_to_json(data: list, filename: str) -> None:
    """
    Saves info from list of dicts to json file

    :param data: List of dicts to dump info
    :param filename: Name of resulting json file

    """

    full_file_name = os.getcwd() + "\\" + filename + ".json"
    with open(full_file_name, "w") as f_out:
        json.dump(data, f_out)


def beauty_print(data: list, column: str, title: str) -> None:
    """
    Prints info about 10 ten companies in a good-looking way -
    "Company_name : chosen_column" with a title over the message

    :param data: List of dicts to print info from
    :param column: Dict key to print info from
    :param title: Required header
    """

    print(f"Top 10 by {title}:")
    print()
    for d in data:
        print(f"{d['name']:<35} : {d[column]}")
    print("-" * 50)
    print()


# GLOBALS
CNT = 1
ALL_COMPANIES_DATA = []


# MAIN
def main():

    url = "https://markets.businessinsider.com/index/components/s&p_500"
    usd = get_usd_rate()
    pool_size = 8
    pool = Pool(pool_size)
    main_page = get_main_page_link(url, ".com")

    for page in get_pages_list(url, main_page):
        soup = get_soup(page)
        ALL_COMPANIES_DATA.extend(
            [
                {"link": l, "growth": g}
                for l, g in zip(get_links(soup), get_growth(soup))
            ]
        )
        print("|", end=" ")
    print()
    print(
        f"Collected {len(ALL_COMPANIES_DATA)} companies for further processing"
    )

    for d in ALL_COMPANIES_DATA:
        pool.apply_async(append_company_data, (d, main_page, usd))
    pool.close()
    pool.join()
    time.sleep(4)
    print()
    print("All data processed")

    top_10_by_price = get_clear_data(top_ten(ALL_COMPANIES_DATA, "price"))
    top_10_by_low_pe = get_clear_data(
        top_ten(ALL_COMPANIES_DATA, "p/e", False)
    )
    top_10_by_growth = get_clear_data(top_ten(ALL_COMPANIES_DATA, "growth"))
    top_10_p_profit = get_clear_data(
        top_ten(ALL_COMPANIES_DATA, "potential profit")
    )

    dump_to_json(top_10_by_price, "top_10_by_price")
    dump_to_json(top_10_by_low_pe, "top_10_by_low_pe")
    dump_to_json(top_10_by_growth, "top_10_by_growth")
    dump_to_json(top_10_p_profit, "top_10_p_profit")

    beauty_print(top_10_by_price, "price", "price in RUB")
    beauty_print(top_10_by_low_pe, "p/e", "low P/E")
    beauty_print(top_10_by_growth, "growth", "1 year growth")
    beauty_print(top_10_p_profit, "potential profit", "potential profit")

    print("Detailed information has been saved in 4 json files")


if __name__ == "__main__":
    main()
