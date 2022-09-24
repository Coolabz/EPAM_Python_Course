import fpdf
import os
import requests
import feedparser
import DateFunc
import rss_parser_class
import Exceptions
import aspose.words as aw


def epub_converter(source, limit, path, count=1):
    rss_parser_class.loger.debug("Epub converter for news was started!")
    counter = 1
    pdf = fpdf.FPDF()
    pdf.add_page()
    url = feedparser.parse(source)
    header = url.feed.title
    pdf.set_font("Arial", "B", size=18)
    pdf.cell(w=200, h=10, txt=header, ln=1, align="C")
    rss_parser_class.loger.debug("The Header was added to EPUB file!")
    for index, i in enumerate(url.entries):
        try:
            title = f"Title:{i['title']}"
            link = f"Link:{i['links'][0]['href']}\n\n"
            date = f"Date:{DateFunc.change_date(i.published)}"
            p = requests.get(i.media_content[0]['url'])
            a = open("pictures" + str(count) + ".jpg", "wb")
            a.write(p.content)
            a.close()
            pdf.set_font("Arial", "B", 12)
            pdf.multi_cell(w=0, h=15, txt=title.encode('latin-1', 'replace').decode('latin-1'), align="L")
            pdf.set_font("Arial", "", 12)
            pdf.multi_cell(w=0, h=15, txt=date, align="L")
            pdf.multi_cell(w=0, h=15, txt=link, align="L")
            pdf.image("pictures" + str(count) + ".jpg", w=170, y=90)
            os.remove("pictures" + str(count) + ".jpg")
            pdf.add_page()
            rss_parser_class.loger.debug(f"{counter} news was added to EPUB file!")
            counter += 1
            count += 1
            if limit - 1 == index:
                break
        except AttributeError:
            image = None
        except RuntimeError:
            continue
    pdf.output(name="news.pdf")
    epub_doc = aw.Document(f"{os.getcwd()}\\news.pdf")
    epub_doc.save(f"{path}\\news.epub")
    os.remove("news.pdf")
    rss_parser_class.loger.debug("Epub converter for news finished successfully")


def date_epub_converter(date, limit, path):
    counter = 1
    rss_parser_class.loger.debug("Epub Converter for cache news was started!")
    parent_path = os.getcwd()
    if os.path.exists("Cache"):
        os.chdir("Cache")
        if os.path.exists(f"{date}.txt"):
            pdf = fpdf.FPDF()
            pdf.add_page()
            with open(f"{date}.txt", "r") as file:
                tile_count = 0
                title_count = 0
                for line in file:
                    if "Title:" in line.split():
                        tile_count += 1
                        title_count += 1
                        if limit == title_count - 1:
                            break
                        rss_parser_class.loger.debug(f"cache news was added to EPUB file!")
                        if len(line) > 90:
                            pdf.set_font("Arial", "B", 12)
                            pdf.cell(w=0, h=10, txt=line.encode('latin-1', 'replace').decode('latin-1')[0:90],
                                     align="L", ln=1)
                            pdf.cell(w=0, h=10, txt=line.encode('latin-1', 'replace').decode('latin-1')[90:], align="L",
                                     ln=1)
                        else:
                            pdf.set_font("Arial", "B", 12)
                            pdf.cell(w=0, h=10, txt=line.encode('latin-1', 'replace').decode('latin-1')[0:90],
                                     align="L", ln=1)
                    elif "[1]:" in line.split():
                        link = pdf.add_link()
                        pdf.cell(w=0, h=10, txt=f"Link to news: {line.split()[1]}", align="L", link=line.split()[1],
                                 ln=1)
                    elif "[2]:" in line.split():
                        link1 = pdf.add_link()
                        pdf.cell(w=0, txt=f"Image: {line.split()[1]}", align="L", link=line.split()[1], ln=1)
                        if tile_count == 3:
                            pdf.add_page()
                            tile_count = 0
                    else:
                        pdf.set_font("Arial", "", 11)
                        pdf.cell(w=0, h=10, txt=line.encode('latin-1', 'replace').decode('latin-1'), align="L", ln=2)
                rss_parser_class.loger.debug("Epub Converter for cache news finished successfully!")
        else:
            raise Exceptions.NoCacheNews("No news on this date!")
    pdf.output(name="news.pdf")
    epub_doc = aw.Document(f"{os.getcwd()}\\news.pdf")
    epub_doc.save(f"{path}\\news.epub")
    os.remove("news.pdf")
    os.chdir(parent_path)
    if os.path.exists("Cache") is False:
        print(os.getcwd())
        raise Exceptions.NoCacheNews("No news on this date!")
