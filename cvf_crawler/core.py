import os, sys
from typing import List
import requests

from bs4 import BeautifulSoup
from rich.progress import track

class CvF_Crawler:
    def __init__(self) -> None:
        pass

    def __call__(self, links: List | str = None, save_dir: str = None) -> None:
        if links == "*":
            raise NotImplementedError("Crawling all papers is under implementation")

        elif links is None:
            raise ValueError("links cannot be None")
        
        if save_dir is None:
            raise ValueError("save_dir cannot be None")
    
        for link in track(links):
            html_text = self.__download_url(url=link)
            
            html_parser = self.__get_parser(html=html_text)
            
            meta_url = html_parser.find_all('meta')[-1].get('content')
            
            filename = meta_url.split("/")[-1]
            
            savepath = save_dir + f"/{filename}"
            
            source = requests.get(meta_url)
            
            with open(savepath, 'wb') as f:
                f.write(source.content)
        
    def __download_url(self, url: str):
        return requests.get(url).text        

    def __get_parser(self, html: str):
        return BeautifulSoup(html, 'html.parser')