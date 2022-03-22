import requests
from bs4 import BeautifulSoup
import translators as ts
from time import time
from threading import Thread
import os


def NewsNasaApi():
    url = "https://iz.ru/tag/mks/publications"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    days = soup.find_all("div", "tabs-content")
    titleDays = days[0].find_all("h3")
    timeDays = days[0].find_all("div", "tag-materials-item__date")
    urlDays = days[0].find_all("a")
    cout_post = len(titleDays)
    daysList = []
    for i in range(cout_post):
        titleDay = titleDays[i].text
        timeDay = timeDays[i].text
        urlDay = urlDays[i].get("href")
        daySet = {"time": timeDay, "url": urlDay, "title": titleDay}
        daysList.append(daySet)
    return daysList


def date_format(date):
    date = date.split("-")
    date = date[2] + "." + date[1] + "." + date[0]
    return date


def text_format(text):
    text = text.split(".")[:-1]
    out_text = ""
    for i in text:
        out_text += i + "."
    return out_text


root_dir = os.path.dirname(os.path.abspath(__file__))


def newjson(text):
    file = open(root_dir + "/DayImg.json", "w")
    file.write(str(text))
    file.close()


def loadjson():
    file = open(root_dir + "/DayImg.json", "r")
    data = file.read()
    file.close()
    return eval(data)


def En_Ru(text):
    return ts.google(text, from_language="en", to_language="ru")


def ImageDayJson():
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    resp = requests.get(url=url)
    data = resp.json()
    date = date_format(data["date"])
    text_en = text_format(data["explanation"])
    text_ru = En_Ru(text_en)
    title_en = data["title"]
    title_ru = En_Ru(title_en)
    media_url = data["url"]
    media_type = data["media_type"]
    data = {
        "date": date,
        "title_en": title_en,
        "title_ru": title_ru,
        "text_en": text_en,
        "text_ru": text_ru,
        "media_url": media_url,
        "media_type": media_type,
    }
    return data


def NewImageDayJson():
    new_data = ImageDayJson()
    newjson([new_data, int(time())])


def ImageDayApi():
    data_json = loadjson()
    filter_time = (int(time()) - data_json[1]) / 86400
    if filter_time < 1:
        return data_json[0]
    else:
        Thread(target=NewImageDayJson).start()
        return data_json[0]
