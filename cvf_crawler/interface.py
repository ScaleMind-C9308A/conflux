import os
from typing import List
from .core import CvF_Crawler
from datetime import datetime


class CvF_Crawler_Interface(CvF_Crawler):
    def __init__(self) -> None:
        super().__init__()
        
        self.main_url = "https://openaccess.thecvf.com/{}"
        
    def __call__(self, save_dir: str = None, conf: str = 'cvpr', year: str = "2023") -> None:
        if conf != "*":
            self.conf_lst = [str.upper(conf)]
        else:
            self.conf_lst = ['CVPR', 'ICCV']
        
        if year != "*":
            self.years = [year]
        else:
            self.years = [str(x) for x in range(2013, datetime.now().year + 1)]
        
        if save_dir is None:
            raise ValueError("save_dir cannot be None")
        elif not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        for _conf in self.conf_lst:
            for _year in self.years:
                conf_name = f"{_conf}{_year}"
                
                conf_url = self.main_url.format(conf_name)
                
                html_text = self._CvF_Crawler__download_url(conf_url)
                
                if html_text is None:
                    continue
                
                print(f"Crawling {conf_name} from {conf_url}")
                
                all_paper_url = conf_url + "?day=all"
                
                all_day_text = self._CvF_Crawler__download_url(all_paper_url)
                
                html_parser = self._CvF_Crawler__get_parser(html=all_day_text)
                
                urls = [x.find_all('a', href=True)[0]['href'][1:] for x in html_parser.find_all("dt")]
                
                links = [self.main_url.format(x) for x in urls]
                
                sub_save_dir = save_dir + f"/{conf_name}"
                if not os.path.exists(sub_save_dir):
                    os.mkdir(sub_save_dir)
                
                super().__call__(links=links, save_dir = sub_save_dir)