


# agents/resource_agent.py
import kaggle
from huggingface_hub import HfApi

class ResourceAgent:
    def __init__(self, use_cases):
        self.use_cases = use_cases
        self.hf_api = HfApi()

    def fetch_resources(self):
        """
        Retrieves datasets from HuggingFace and Kaggle for each use case and returns resource links.
        """
        resources = []
        for use_case in self.use_cases:
            hf_datasets = list(self.hf_api.list_datasets(search=use_case["use_case"]))
            hf_links = [f"https://huggingface.co/datasets/{dataset.id}" for dataset in hf_datasets[:2]]
            
            kaggle_datasets = kaggle.api.dataset_list(search=use_case["use_case"])
            kaggle_links = [f"https://www.kaggle.com/{dataset.ref}" for dataset in kaggle_datasets[:2]]
            
            dataset_links = hf_links + kaggle_links if hf_links or kaggle_links else ["https://huggingface.co/datasets"]
            
            resources.append({
                "use_case": use_case["use_case"],
                "feasibility": use_case["feasibility"],
                "resource_links": dataset_links
            })
        return resources
