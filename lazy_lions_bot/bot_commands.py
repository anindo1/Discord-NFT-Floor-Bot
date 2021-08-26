import httpx
from bs4 import BeautifulSoup
import requests


def mainStats(stat):
    # Get data from get request to opensea api
    URL = "https://api.opensea.io/api/v1/collection/lazy-lions"
    response = requests.request("GET", URL).json()
    data = response["collection"]["stats"]

    # Assign data fields
    one_day_volume = round(data["one_day_volume"], 2)
    one_day_change = round(data["one_day_change"], 2)
    one_day_sales = round(data["one_day_sales"], 0)
    one_day_average_price = round(data["one_day_average_price"], 2)
    seven_day_volume = round(data["seven_day_volume"], 2)
    seven_day_change = round(data["seven_day_change"], 2)
    seven_day_sales = round(data["seven_day_sales"], 0)
    seven_day_average_price = round(data["seven_day_average_price"], 2)
    thirty_day_volume = round(data["thirty_day_volume"], 2)
    thirty_day_change = round(data["thirty_day_change"], 2)
    thirty_day_sales = round(data["thirty_day_sales"], 0)
    thirty_day_average_price = round(data["thirty_day_average_price"], 2)
    total_volume = round(data["total_volume"], 2)
    total_sales = round(data["total_sales"], 0)
    num_owners = data["num_owners"]
    average_price = round(data["average_price"], 2)
    floor_price = data["floor_price"]

    if stat == "floor":
        return [URL, floor_price]
    elif stat == "num_owners":
        return [URL, num_owners]
    elif stat == "volume":
        return [URL, total_volume]
    elif stat == "stats":
        return [
            "https://opensea.io/collection/lazy-lions?search[sortAscending]=true&search[sortBy]=PRICE",
            one_day_volume,
            one_day_change,
            one_day_sales,
            one_day_average_price,
            seven_day_volume,
            seven_day_change,
            seven_day_sales,
            seven_day_average_price,
            thirty_day_volume,
            thirty_day_change,
            thirty_day_sales,
            thirty_day_average_price,
            total_volume,
            total_sales,
            num_owners,
            average_price,
            floor_price,
        ]


def traitFloor(trait_type, trait):
    print("traitfloor")
    BASE_URL = "https://opensea.io/collection/lazy-lions?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]="
    TRAIT_TYPE = trait_type
    URL_EXTENSION = "&search[stringTraits][0][values][0]="
    TRAIT = trait
    URL = BASE_URL + TRAIT_TYPE + URL_EXTENSION + TRAIT + "&search[toggles][0]=BUY_NOW"

    headers = {"user-agent": "my-app/0.0.1"}
    page = httpx.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    price_info = soup.find_all(
        "div",
        {"class": "Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm Price--amount"},
    )
    if len(price_info) == 0:
        return "No results found. Please check your input"
    else:
        return [URL, price_info[0].get_text()]
