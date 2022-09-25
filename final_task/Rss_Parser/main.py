import argparser_rss
import rss_parser_class
import Cache_helper
import to_pdf
import to_epub

THIS_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
sys.path.append(THIS_DIRECTORY)


def main():
    if argparser_rss.args['version']:
        print("Version 1.4")
    elif argparser_rss.args["to_pdf"]:
        if argparser_rss.args["date"]:
            if argparser_rss.args['json']:
                source = argparser_rss.args['source']
                limit = argparser_rss.args['limit']
                path = argparser_rss.args['to_pdf']
                cache_date = argparser_rss.args['date']
                parsing = rss_parser_class.Rss_parser(source)
                parsing.json_get_value(limit)
                to_pdf.date_pdf_news(cache_date, limit, path)
            else:
                source = argparser_rss.args['source']
                limit = argparser_rss.args['limit']
                path = argparser_rss.args['to_pdf']
                cache_date = argparser_rss.args['date']
                to_pdf.date_pdf_news(cache_date, limit, path)
        elif argparser_rss.args['json']:
            source = argparser_rss.args['source']
            limit = argparser_rss.args['limit']
            path = argparser_rss.args['to_pdf']
            parsing = rss_parser_class.Rss_parser(source)
            parsing.json_get_value(limit)
            to_pdf.url_parse(source=source, limit=limit, path=path, count=1)
        else:
            source = argparser_rss.args['source']
            limit = argparser_rss.args['limit']
            path = argparser_rss.args['to_pdf']
            to_pdf.url_parse(source=source, limit=limit, path=path, count=1)
    elif argparser_rss.args["to_epub"]:
        if argparser_rss.args["date"]:
            if argparser_rss.args['json']:
                source = argparser_rss.args['source']
                limit = argparser_rss.args['limit']
                path = argparser_rss.args['to_epub']
                cache_date = argparser_rss.args['date']
                parsing = rss_parser_class.Rss_parser(source)
                parsing.json_get_value(limit)
                to_epub.date_epub_converter(cache_date, limit, path)
            else:
                source = argparser_rss.args['source']
                limit = argparser_rss.args['limit']
                path = argparser_rss.args['to_epub']
                cache_date = argparser_rss.args['date']
                to_epub.date_epub_converter(cache_date, limit, path)
        elif argparser_rss.args['json']:
            source = argparser_rss.args['source']
            limit = argparser_rss.args['limit']
            path = argparser_rss.args['to_epub']
            parsing = rss_parser_class.Rss_parser(source)
            parsing.json_get_value(limit)
            to_epub.epub_converter(source=source, limit=limit, path=path, count=1)
        else:
            source = argparser_rss.args['source']
            limit = argparser_rss.args['limit']
            path = argparser_rss.args['to_epub']
            to_epub.epub_converter(source=source, limit=limit, path=path, count=1)
    elif argparser_rss.args['date']:
        cache_date = argparser_rss.args['date']
        limit = argparser_rss.args['limit']
        if argparser_rss.args['json']:
            Cache_helper.cache_json_get_value(cache_date, limit)
        else:
            Cache_helper.cache_news_finder(cache_date, limit)
    elif argparser_rss.args['json']:
        source = argparser_rss.args['source']
        limit = argparser_rss.args['limit']
        parsing = rss_parser_class.Rss_parser(source)
        parsing.json_get_value(limit)
    else:
        source = argparser_rss.args['source']
        limit = argparser_rss.args['limit']
        parsing = rss_parser_class.Rss_parser(source)
        parsing.get_header()
        parsing.get_value(limit)


if __name__ == "__main__":
    main()
