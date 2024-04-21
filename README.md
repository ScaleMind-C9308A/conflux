ConfluxPapers (conflux) - Crawling all paper you want

# Updates
- v0.0.1 (29th Dec 2024): CVPR, ICCV conference papers crawling all or by year or by conference

# Installation
First you need to clone the repo as currently ```conflux``` is not available on ```Pypi```
```
git clone https://github.com/KhoiDOO/cvf_crawler.git
cd /path/to/cvf_crawler/
pip install -e .
```

# Usage
## Crawling a list of paper links
Use the following source code to crawl ```.pdf``` files from provided links by simply ```Cvf_Crawler```
```Python
import os, sys
from cvf_crawler import CvF_Crawler

if __name__ == "__main__":
    cvpr_2023 = [
        "https://openaccess.thecvf.com/content/CVPR2023/html/Chen_Transfer_Knowledge_From_Head_to_Tail_Uncertainty_Calibration_Under_Long-Tailed_CVPR_2023_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2023/html/Zhou_Class-Conditional_Sharpness-Aware_Minimization_for_Deep_Long-Tailed_Recognition_CVPR_2023_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2023/html/Du_No_One_Left_Behind_Improving_the_Worst_Categories_in_Long-Tailed_CVPR_2023_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2023/html/Du_Global_and_Local_Mixture_Consistency_Cumulative_Learning_for_Long-Tailed_Visual_CVPR_2023_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2023/html/Wang_Balancing_Logit_Variation_for_Long-Tailed_Semantic_Segmentation_CVPR_2023_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2023/html/Gou_Rethinking_Image_Super_Resolution_From_Long-Tailed_Distribution_Learning_Perspective_CVPR_2023_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2023/html/Wei_Towards_Realistic_Long-Tailed_Semi-Supervised_Learning_Consistency_Is_All_You_Need_CVPR_2023_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2023/html/Li_FCC_Feature_Clusters_Compression_for_Long-Tailed_Visual_Recognition_CVPR_2023_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2023/html/Jin_Long-Tailed_Visual_Recognition_via_Self-Heterogeneous_Integration_With_Knowledge_Excavation_CVPR_2023_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2023/html/Aimar_Balanced_Product_of_Calibrated_Experts_for_Long-Tailed_Recognition_CVPR_2023_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2023/html/Ma_Curvature-Balanced_Feature_Manifold_Learning_for_Long-Tailed_Classification_CVPR_2023_paper.html",
    ]

    crawler = CvF_Crawler()
    
    save_dir = os.getcwd() + "/cvpr_2023"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    crawler(links=cvpr_2023, save_dir=save_dir)
```

## Crawling all papers from a specific conference (i.e. CVPR, ICCV) in a year or everything
### Crawling everything
The following code allow you to crawl all papers from CVPR and ICCV from 2013 until current year.
```Python
from cvf_crawler import CvF_Crawler_Interface

if __name__ == "__main__":
    
    cvf_interface = CvF_Crawler_Interface()
    
    cvf_interface(
        save_dir=os.getcwd() + "/clone",
        conf='*',
        year='*'
    )
```
### Crawling all papers from specific conference from 2013 until current year
If you would like to crawl only papers from CVPR use the following code
```Python
from cvf_crawler import CvF_Crawler_Interface

if __name__ == "__main__":
    
    cvf_interface = CvF_Crawler_Interface()
    
    cvf_interface(
        save_dir=os.getcwd() + "/clone",
        conf='cvpr',
        year='*'
    )
```

### Crawling all papers from specific conference in one year
More specifically, all papers from CVPR in 2023 can be crawled by the following code:
```Python
from cvf_crawler import CvF_Crawler_Interface

if __name__ == "__main__":
    
    cvf_interface = CvF_Crawler_Interface()
    
    cvf_interface(
        save_dir=os.getcwd() + "/clone",
        conf='cvpr',
        year='2023'
    )
```
