import json
import operator
import os
import re

import requests
from bs4 import BeautifulSoup


def get_main_page_link(url, domain_zone):
    return url.split(domain_zone)[0] + domain_zone


def get_html(url):
    r = requests.get(url)
    return r.text


def get_pages_list(main_url):
    domain = get_main_page_link(main_url, ".com")

    soup = BeautifulSoup(get_html(main_url), "lxml")
    pages_menu = soup.find_all("a", class_="tab__subnav__item")[1:]
    pages_list = [domain + a.get("href") for a in pages_menu]
    return pages_list


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


def usd_to_rub(price_in_usd):
    link = "https://www.cbr.ru/scripts/XML_daily.asp"
    soup = BeautifulSoup(get_html(link), "lxml-xml")
    usd_rate = float(
        soup.find("Valute", ID="R01235").Value.text.replace(",", ".")
    )

    return round(usd_rate * price_in_usd, 2)


def get_company_data(company_page):
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

    price_in_usd = soup.find(
        "span", class_="price-section__current-value"
    ).text
    price = usd_to_rub(float(price_in_usd))

    try:
        pe = float(
            soup.find("div", text=re.compile("P/E Ratio"))
            .parent.text.strip()
            .split("\r")[0]
        )
    except:
        pe = None

    try:
        low_52 = (
            soup.find("div", text=re.compile("52 Week Low"))
            .parent.text.strip()
            .split("\r")[0]
        )
    except:
        low_52 = None

    try:
        high_52 = (
            soup.find("div", text=re.compile("52 Week High"))
            .parent.text.strip()
            .split("\r")[0]
        )
    except:
        high_52 = None

    potential_profit = None
    if high_52 and low_52:
        potential_profit = (
            f"{(float(high_52) - float(low_52)) / float(low_52) :.2%}"
        )

    company_info["name"] = name
    company_info["code"] = code
    company_info["price"] = price
    company_info["p/e"] = pe
    company_info["potential profit"] = potential_profit

    return company_info


def top_ten(data, sort_key, reverse=True):
    return sorted(data, key=operator.itemgetter(sort_key), reverse=reverse)[
        :10
    ]


def dump_to_json(data, filename):
    full_file_name = os.getcwd() + "\\" + filename + ".json"
    with open(full_file_name, "w") as f_out:
        json.dump(data, f_out)


def main():
    main_url = "https://markets.businessinsider.com/index/components/s&p_500"
    # all_companies_data = []
    #
    # for company_page in get_all_companies_links(main_url)[:15]:
    #     all_companies_data.append(get_company_data(company_page))
    #
    # top_10_by_price = top_ten(all_companies_data, "price")
    # top_10_by_low_pe = top_ten(all_companies_data, "p/e", False)
    # top_10_p_profit = top_ten(all_companies_data, "potential profit")
    #
    # print(top_10_by_price)
    # print(top_10_by_low_pe)
    # print(top_10_p_profit)
    # dump_to_json(top_10_by_price, "top_10_by_price")
    # dump_to_json(top_10_by_low_pe, "top_10_by_low_pe")
    # dump_to_json(top_10_p_profit, "top_10_p_profit")

    soup = BeautifulSoup(get_html(main_url), "lxml")
    name = "3M"
    growth = (
        (soup.find("a", title=name))
        .parent.parent.select("span:last-child")[-1]
        .text
    )
    print(growth)


if __name__ == "__main__":
    main()
