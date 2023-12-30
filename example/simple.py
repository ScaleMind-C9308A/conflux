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
    
    
    cvpr_2022 = [
        "https://openaccess.thecvf.com/content/CVPR2022/html/He_Relieving_Long-Tailed_Instance_Segmentation_via_Pairwise_Class_Balance_CVPR_2022_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2022/html/Alshammari_Long-Tailed_Recognition_via_Weight_Balancing_CVPR_2022_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2022/html/Li_Equalized_Focal_Loss_for_Dense_Long-Tailed_Object_Detection_CVPR_2022_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2022/html/Li_Targeted_Supervised_Contrastive_Learning_for_Long-Tailed_Recognition_CVPR_2022_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2022/html/Zhu_Balanced_Contrastive_Learning_for_Long-Tailed_Visual_Recognition_CVPR_2022_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2022/html/Li_Trustworthy_Long-Tailed_Classification_CVPR_2022_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2022/html/Li_Nested_Collaborative_Learning_for_Long-Tailed_Visual_Recognition_CVPR_2022_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2022/html/Park_The_Majority_Can_Help_the_Minority_Context-Rich_Minority_Oversampling_for_CVPR_2022_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2022/html/Li_Adaptive_Hierarchical_Representation_Learning_for_Long-Tailed_Object_Detection_CVPR_2022_paper.html",
        "https://openaccess.thecvf.com/content/CVPR2022/html/Li_Long-Tailed_Visual_Recognition_via_Gaussian_Clouded_Logit_Adjustment_CVPR_2022_paper.html",
    ]
    
    
    iccv_2021 = [
        "https://openaccess.thecvf.com/content/ICCV2021/html/Feng_Exploring_Classification_Equilibrium_in_Long-Tailed_Object_Detection_ICCV_2021_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2021/html/He_Distilling_Virtual_Examples_for_Long-Tailed_Recognition_ICCV_2021_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2021/html/Zang_FASA_Feature_Augmentation_and_Sampling_Adaptation_for_Long-Tailed_Instance_Segmentation_ICCV_2021_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2021/html/Cai_ACE_Ally_Complementary_Experts_for_Solving_Long-Tailed_Recognition_in_One-Shot_ICCV_2021_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2021/html/Zhang_VideoLT_Large-Scale_Long-Tailed_Video_Recognition_ICCV_2021_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2021/html/Zhang_MosaicOS_A_Simple_and_Effective_Use_of_Object-Centric_Images_for_ICCV_2021_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2021/html/Liu_GistNet_A_Geometric_Structure_Transfer_Network_for_Long-Tailed_Recognition_ICCV_2021_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2021/html/Li_Self_Supervision_to_Distillation_for_Long-Tailed_Visual_Recognition_ICCV_2021_paper.html",
    ]
    
    
    iccv_2023 = [
        "https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Learning_in_Imperfect_Environment_Multi-Label_Classification_with_Long-Tailed_Distribution_and_ICCV_2023_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2023/html/Chen_AREA_Adaptive_Reweighting_via_Effective_Area_for_Long-Tailed_Classification_ICCV_2023_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2023/html/Hou_Subclass-balancing_Contrastive_Learning_for_Long-tailed_Recognition_ICCV_2023_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2023/html/Dong_Boosting_Long-tailed_Object_Detection_via_Step-wise_Learning_on_Smooth-tail_Data_ICCV_2023_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2023/html/Tao_Local_and_Global_Logit_Adjustments_for_Long-Tailed_Learning_ICCV_2023_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2023/html/Tao_Local_and_Global_Logit_Adjustments_for_Long-Tailed_Learning_ICCV_2023_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2023/html/Lu_Label-Noise_Learning_with_Intrinsically_Long-Tailed_Data_ICCV_2023_paper.html",
        "https://openaccess.thecvf.com/content/ICCV2023/html/Zeng_Global_Balanced_Experts_for_Federated_Long-Tailed_Learning_ICCV_2023_paper.html",
    ]
    
    crawler = CvF_Crawler()
    
    save_dir = os.getcwd() + "/save"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    
    for links, folder in zip(
        [cvpr_2023, cvpr_2022, iccv_2021, iccv_2023],
        ["cvpr_2023", "cvpr_2022", "iccv_2021", "iccv_2023"]
    ):
        sub_save_dir = save_dir + f"/{folder}"
        if not os.path.exists(sub_save_dir):
            os.mkdir(sub_save_dir)
        
        crawler(links=cvpr_2023, save_dir=sub_save_dir)