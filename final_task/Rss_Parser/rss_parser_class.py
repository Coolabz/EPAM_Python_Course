import feedparser
import json
import DateFunc
import logging
import requests
import Exceptions
import Cache_helper
import argparser_rss


verbose_or_note = "WARNING"

if argparser_rss.args['verbose']:
    verbose_or_note = "DEBUG"
logging.basicConfig(level=verbose_or_note)
loger = logging.getLogger()


class Rss_parser:
    def __init__(self, source, limit=None):
        self.source = source
        self.limit = limit

    def get_url(self):
        loger.debug(f"Function get_url was started")
        if str(requests.get(self.source)) == "<Response [200]>":
            url = feedparser.parse(self.source)
            loger.debug(f"Function get_url successfully completed")
            return url
        else:
            loger.debug("The server does not respond!")
            raise Exceptions.NoResponse("The server does not respond!")

    def get_header(self):
        loger.debug(f"Function header was started")
        loger.debug(f"The Header was successfully received")
        return self.get_url().feed.title

    def get_value(self, limit):
        loger.debug(f"Function get_value was started")
        print(f"Feed: {self.get_url().feed['title']}\n")
        for index, i in enumerate(self.get_url().entries):
            try:
                title = i['title']
                link = i['links'][0]['href']
                date = DateFunc.change_date(i.published)
                image = i.media_content[0]['url']
                value = f"Title: {title} \nDate: {date}\nLink: {link}\n\nLinks:\n[1]: {link} (link)\n[2]: {image} (image)\n"
                value_for_cache = f"Title: {title} \nDate: {date}\nLink: {link}\n\nLinks:\n[1]: {link} (link)\n[2]: {image} (image)\n\n"
                print(value)
                Cache_helper.file_exists(DateFunc.change_date_for_cache(i.published), value_for_cache)
                if limit - 1 == index:
                    break
            except AttributeError:
                image = None
        loger.debug(f"Function get_value successfully completed")

    def converter_func(self, limit):
        for index, i in enumerate(self.get_url().entries):
            try:
                title = i['title']
                link = i['links'][0]['href']
                date = DateFunc.change_date(i.published)
                image = i.media_content[0]['url']
            except AttributeError:
                image = None

    def json_get_value(self, limit):
        loger.debug(f"Function json_get_value was started")
        data = {"news": []}
        for index, i in enumerate(self.get_url().entries):
            try:
                data["news"].append({
                    "title": i['title'],
                    "date": DateFunc.change_date(i.published),
                    "link": i['links'][0]['href'],
                    "image": i.media_content[0]['url']})
                if limit - 1 == index:
                    break
            except AttributeError:
                image = None
        data = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
        print(data.decode())
        loger.debug(f"Function json_get_value successfully completed")

