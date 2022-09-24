import unittest
import sys
import os
import feedparser
from unittest.mock import Mock, patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import rss_parser_class
import argparser_rss
import Cache_helper
import DateFunc



class TestRss_parser(unittest.TestCase):

    def test_file_exists(self):
        self.assertEqual(Cache_helper.file_exists("20220918", "news"), None)

    def test_cache_news_finder(self):
        self.assertEqual(Cache_helper.cache_news_finder("20220918", 2), None)

    def test_cache_json_get_value(self):
        self.assertEqual(Cache_helper.cache_json_get_value("20220918", 2), None)

    def test_change_date(self):
        true_date = DateFunc.change_date("2022-09-22T07:02:18Z")
        self.assertEqual(true_date, "Thu, 22 Sep 2022 07:02:18")

    def test_change_date_for_cache(self):
        true_date = DateFunc.change_date_for_cache("2022-09-22T07:02:18Z")
        self.assertEqual(true_date, "20220922")

    def test_get_header(self):
        a = rss_parser_class.Rss_parser("https://news.yahoo.com/rss/", 1)
        self.assertEqual(a.get_header(), "Yahoo News - Latest News & Headlines")

    def test_get_value(self):
        a = rss_parser_class.Rss_parser("https://news.yahoo.com/rss/", 3)
        self.assertEqual(a.get_value(3), None)

    def test_converter_func(self):
        a = rss_parser_class.Rss_parser("https://news.yahoo.com/rss/", 3)
        self.assertEqual(a.converter_func(1), None)

    def test_json_get_value(self):
        a = rss_parser_class.Rss_parser("https://news.yahoo.com/rss/", 3)
        self.assertEqual(a.json_get_value(1), None)


if __name__ == "__main__":
    unittest.main()
