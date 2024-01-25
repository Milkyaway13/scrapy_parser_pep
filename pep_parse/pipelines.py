import pandas as pd

from pep_parse.settings import BASE_DIR, NOW_FORMATTED, UTF_8

from pep_parse.spiders.pep import PepSpider


class PepParsePipeline:

    def open_spider(self, spider: PepSpider):
        self.status_summary = {
            'Accepted': 0, 'Active': 0, 'Deferred': 0, 'Draft': 0,
            'Final': 0, 'Provisional': 0, 'Rejected': 0, 'Superseded': 0,
            'Withdrawn': 0, 'Total': 0
        }

    def process_item(self, item, spider):
        if item['status'] in self.status_summary:
            self.status_summary[item['status']] += 1
            self.status_summary['Total'] += 1
        return item

    def close_spider(self, spider):
        RESULTS_DIR = BASE_DIR / 'results'
        FILE_NAME = f'status_summary_{NOW_FORMATTED}.csv'
        FILE_PATH = RESULTS_DIR / FILE_NAME
        df = pd.DataFrame(list(
            self.status_summary.items()), columns=['Статус', 'Количество'])
        df.to_csv(FILE_PATH, sep='\t', index=False, encoding=UTF_8)
