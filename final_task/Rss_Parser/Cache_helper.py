import os
import Exceptions
import rss_parser_class
import json


def dirback():
    m = os.getcwd()
    n = m.rfind("\\")
    d = m[0: n + 1]
    os.chdir(d)
    return None


def file_exists(date, value):
    rss_parser_class.loger.debug(f"Function file_exists was started")
    if os.path.exists("Cache"):
        os.chdir("Cache")
        if os.path.exists(str(date)):
            with open(f"{date}.txt", "a") as file:
                file.write(str(value))
        else:
            with open(f"{date}.txt", "a") as file:
                file.write(str(value))
    else:
        os.mkdir("Cache")
        os.chdir("Cache")
        with open(f"{date}.txt", "a") as file:
            file.write(str(value))
    dirback()
    rss_parser_class.loger.debug(f"Function get_url successfully completed")


def cache_news_finder(date, limit):
    counter = 0
    rss_parser_class.loger.debug(f"Function cache_news_finder was started")
    if os.path.exists("Cache"):
        os.chdir("Cache")
        if os.path.exists(f"{str(date)}.txt"):
            with open(f"{str(date)}.txt", "r") as file:
                for line in file:
                    if "Title:" in line:
                        if counter == limit:
                            break
                        else:
                            counter += 1
                    print(line)
        else:
            raise Exceptions.NoCacheNews("There is no news on this date!")
    dirback()
    rss_parser_class.loger.debug(f"Function cache_news_finder successfully completed")


def cache_json_get_value(date, limit):
    rss_parser_class.loger.debug(f"Function cache_json_get_value was started")
    counter = 0
    data = {"news": [{}]}
    if os.path.exists("Cache"):
        os.chdir("Cache")
        if os.path.exists(f"{str(date)}.txt"):
            with open(f"{str(date)}.txt", "r") as file:
                for line in file:
                    if "Title:" in line:
                        if counter == limit:
                            break
                        else:
                            data["news"][counter]["title"] = " ".join(line.split()[1:])
                    elif "Date:" in line:
                        data["news"][counter]["date"] = " ".join(line.split()[1:])
                    # elif "Link:" == line.split()[0]:
                    elif "Link:" in line:
                        data["news"][counter]["link"] = " ".join(line.split()[1:])
                    elif "(image)" in line:
                        data["news"][counter]["image"] = " ".join(line.split()[1:-1])
                        data["news"].append({})
                        rss_parser_class.loger.debug(f"The {counter + 1} news was added!")
                        counter += 1
            data["news"].remove({})
            result = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
            print(result.decode())
            rss_parser_class.loger.debug(f"Function cache_json_get_value successfully completed")
