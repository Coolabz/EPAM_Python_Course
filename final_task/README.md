## Iteration 1
The RSS parser is command line utilit, which get RSS url and prints the news in appropriate format. 
Utility has the following interface:

Pure Python command-line RSS reader.

positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided

Json format:
    {                                                      
  "news": [
    {
      "title": "Pink Floyd founder cancels Poland concerts after war remarks",
      "date": "Sat, 24 Sep 2022 18:12:16",
      "link": "https://news.yahoo.com/pink-floyd-founder-cancels-poland-181216312.html",
      "image": "https://s.yimg.com/uu/api/res/1.2/9gtGY.9dvqT_hBA4jtJUmQ--~B/aD0zMzA0O3c9NDk1NTthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/9db52f68cddb2b4ffd7a613b754d7c2c"  
    }
  ]
}

##Iteration 2
If you want to run utility on your computer you need:
1) clone repository from https://github.com/Coolabz/EPAM_Python_Course
2) `$cd final_task`
3)  `$python setup.py sdist bdist_wheel`
4)  `$cd dist`
3) `$pip install rss_reader-1.1.tar.gz`
4) run `$rss_reader https://news.yahoo.com/rss --limit 2 --verbose`


##Iteration 3

News stored in Cache folder in txt format. After utility launching utility creates folder Cache, where it saves
news use date in format `%Y%m%d` as a name. 

Format news in file:
Title: Pink Floyd founder cancels Poland concerts after war remarks 
Date: Sat, 24 Sep 2022 18:12:16
Link: https://news.yahoo.com/pink-floyd-founder-cancels-poland-181216312.html

Links:
[1]: https://news.yahoo.com/pink-floyd-founder-cancels-poland-181216312.html (link)
[2]: https://s.yimg.com/uu/api/res/1.2/9gtGY.9dvqT_hBA4jtJUmQ--~B/aD0zMzA0O3c9NDk1NTthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/9db52f68cddb2b4ffd7a613b754d7c2c (image)

Utility works with date argument without internet with arguments --json, --verbose, limit.


## Iteration 4

For this iteration I choose PDF and EPUB formats. 
Utility with argument --to-pdf converts news to pdf format(needs positional argument path)
PDF:
`$python main.py https://news.yahoo.com/rss --to-pdf path`
EPUB:
`$python main.py https://news.yahoo.com/rss --to-epub path`

As for coverage, my tests covers 83% of code.

Thank you!
