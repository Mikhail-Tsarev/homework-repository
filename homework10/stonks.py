import json
import os
import re
import time
from functools import lru_cache
from multiprocessing.pool import ThreadPool as Pool

import requests
from bs4 import BeautifulSoup

all_companies_data = []


def get_main_page_link(url, domain_zone):
    return url.split(domain_zone)[0] + domain_zone


@lru_cache
def get_html(url):
    r = requests.get(url, timeout=None)
    return r.text


@lru_cache
def get_pages_list(main_url):
    domain = get_main_page_link(main_url, ".com")

    soup = BeautifulSoup(get_html(main_url), "lxml")
    pages_menu = soup.find_all("a", class_="tab__subnav__item")[1:]
    pages_list = [domain + a.get("href") for a in pages_menu]
    return pages_list


@lru_cache
def get_all_companies_links(main_url):
    domain = get_main_page_link(main_url, ".com")
    pages_list = get_pages_list(main_url)

    all_companies_links = []

    for page in pages_list:
        soup = BeautifulSoup(get_html(page), "lxml")
        trs = soup.find("tbody", class_="table__tbody").find_all("tr")
        page_companies_links = [
            domain + tr.find("a").get("href") for tr in trs
        ]
        all_companies_links.extend(page_companies_links)

    return all_companies_links


@lru_cache
def get_usd_rate():
    link = "https://www.cbr.ru/scripts/XML_daily.asp"
    soup = BeautifulSoup(get_html(link), "lxml-xml")

    return float(soup.find("Valute", ID="R01235").Value.text.replace(",", "."))


def get_company_data(company_page, main_url, usd_rate):
    company_info = {}

    soup = BeautifulSoup(get_html(company_page), "lxml")

    code = (
        soup.find("h1")
        .find("span", class_="price-section__category")
        .find("span")
        .text.replace(", ", "")
    )

    name = (
        soup.find("h1")
        .find("span", class_="price-section__label")
        .text.strip()
    )

    price_in_usd = float(
        soup.find("span", class_="price-section__current-value").text.replace(
            ",", ""
        )
    )

    price = round(usd_rate * price_in_usd, 2)

    try:
        pe = float(
            soup.find("div", text=re.compile("P/E Ratio"))
            .parent.text.strip()
            .split("\r")[0]
        )
    except:
        pe = float("inf")

    try:
        low_52 = (
            soup.find("div", text=re.compile("52 Week Low"))
            .parent.text.strip()
            .split("\r")[0]
            .replace(",", "")
        )
    except AttributeError:
        low_52 = None

    try:
        high_52 = (
            soup.find("div", text=re.compile("52 Week High"))
            .parent.text.strip()
            .split("\r")[0]
            .replace(",", "")
        )
    except AttributeError:
        high_52 = None

    potential_profit = "-100000000%"
    if high_52 and low_52:
        potential_profit = (
            f"{(float(high_52) - float(low_52)) / float(low_52) :.2%}"
        )

    pages_list = get_pages_list(main_url)

    growth = "-100000000%"
    for page in pages_list:
        p = get_html(page)
        if name not in p:
            continue
        else:
            soup = BeautifulSoup(p, "lxml")
            # hrf = "/stocks/" + code.lower() + "-stock"
            growth = (
                soup.find("a", title=name)
                .parent.parent.select("span:last-child")[-1]
                .text
            )
            break

    company_info["name"] = name
    company_info["code"] = code
    company_info["price"] = price
    company_info["p/e"] = pe
    company_info["growth"] = growth
    company_info["potential profit"] = potential_profit

    # print(name, growth)

    return company_info


def top_ten(data, sort_key, reverse=True):
    if isinstance(data[0][sort_key], str):
        return sorted(
            data,
            key=lambda d: float(d[sort_key][:-1]) / 100,
            reverse=reverse,
        )[:10]

    return sorted(
        data,
        key=lambda d: d[sort_key],
        reverse=reverse,
    )[:10]


def dump_to_json(data, filename):
    full_file_name = os.getcwd() + "\\" + filename + ".json"
    with open(full_file_name, "w") as f_out:
        json.dump(data, f_out)


def append_info(company_page, main_url, usd):
    global all_companies_data
    # random_number = random.uniform(0.01, 0.5)
    # time.sleep(random_number)

    all_companies_data.append(get_company_data(company_page, main_url, usd))


def main():
    main_url = "https://markets.businessinsider.com/index/components/s&p_500"
    usd = get_usd_rate()

    pool_size = 8
    pool = Pool(pool_size)

    for company_page in get_all_companies_links(main_url):
        pool.apply_async(append_info, (company_page, main_url, usd))
    pool.close()
    pool.join()
    time.sleep(4)

    print(f"Processed {len(all_companies_data)} companies")

    top_10_by_price = top_ten(all_companies_data, "price")
    top_10_by_low_pe = top_ten(all_companies_data, "p/e", False)
    top_10_by_growth = top_ten(all_companies_data, "growth")
    top_10_p_profit = top_ten(all_companies_data, "potential profit")

    # print(*top_10_by_price, sep="\n")
    # print()
    # print(*top_10_by_low_pe, sep="\n")
    # print()
    # print(*top_10_by_growth, sep="\n")
    # print()
    # print(*top_10_p_profit, sep="\n")

    dump_to_json(top_10_by_price, "top_10_by_price")
    dump_to_json(top_10_by_low_pe, "top_10_by_low_pe")
    dump_to_json(top_10_by_growth, "top_10_by_growth")
    dump_to_json(top_10_p_profit, "top_10_p_profit")

    print("4 JSON files has been recorded")


if __name__ == "__main__":
    main()
