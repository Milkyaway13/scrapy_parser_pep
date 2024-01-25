import datetime as dt
from pathlib import Path


ALLOWED_DOMAINS = 'peps.python.org'
BASE_DIR = Path(__file__).parent.parent
BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True
UTF_8 = 'utf-8'
NOW_FORMATTED = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
RESULTS_DIR = BASE_DIR / 'results'
FILE_NAME = f'status_summary_{NOW_FORMATTED}.csv'
FILE_PATH = RESULTS_DIR / FILE_NAME


FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
