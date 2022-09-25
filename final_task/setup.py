from setuptools import setup, find_packages

with open("README.md", "r") as file:
    description = file.read()


setup(
    name='rss-reader',
    version='4.0',
    description='Python RSS reader',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/Coolabz/EPAM_Python_Course',
    author='Mikalai Shupayeu',
    author_email='Mikalai_Shupayeu@epam.com',
    scripts=['RSS_Parser/argparser_rss.py',
             'RSS_Parser/Cache_helper.py',
             'RSS_Parser/DateFunc.py',
             'RSS_Parser/Exceptions.py',
             'RSS_Parser/main.py',
             'RSS_Parser/rss_parser_class.py',
             'RSS_Parser/to_epub.py',
             'RSS_Parser/to_pdf.py'],
    install_requires=['aspose-words==22.9.0', 'certifi==2022.9.24', 'charset-normalizer==2.1.1', 'feedparser==6.0.10', 'fpdf==1.7.2', 'idna==3.4','requests==2.28.1', 'sgmllib3k==1.0.0', 'sgmllib3k==1.0.0', 'urllib3==1.26.12'],
    entry_points={
        'console_scripts': [
            'rss-reader = Rss_Parser.main:main',
        ],
    },
    test_suite='RSS_Parser.test'
)
