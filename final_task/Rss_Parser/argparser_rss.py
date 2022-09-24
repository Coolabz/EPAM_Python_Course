import argparse
import math

parser = argparse.ArgumentParser(description="Parser news from rss news cites")
# Positional arguments
parser.add_argument("source", type=str, help="Link of the news portal", default=None, nargs="?")

# Optional arguments
parser.add_argument("--version", required=False, help="Version of app", action="store_true")
parser.add_argument("--limit", type=int, required=False, help="Limit of articles", default=math.inf)
parser.add_argument("--json", required=False, help="News in JSON format", action="store_true")
parser.add_argument("--verbose", required=False, help="Outputs verbose status messages", action="store_true")
parser.add_argument("--date", type=str, required=False, help="Version of app", default=None)
parser.add_argument("--to-pdf", type=str, help="Convert news to pdf format, need path, where the file will be saved")
parser.add_argument("--to-epub", type=str, help="Convert news to pdf format, need path, where the file will be saved")
args = vars(parser.parse_args())
