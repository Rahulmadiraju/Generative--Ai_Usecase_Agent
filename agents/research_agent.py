

# agents/research_agent.py
import os
import requests

class ResearchAgent:
    def __init__(self, industry):
        self.industry = industry
        # Fetch Google API key and Custom Search Engine ID from environment variables
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.google_cse_id = os.getenv("GOOGLE_CSE_ID")

    def google_search(self, query):
        """
        Performs a search using Google Custom Search API and returns top results.
        """
        url = f"https://www.googleapis.com/customsearch/v1?key={self.google_api_key}&cx={self.google_cse_id}&q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            results = response.json().get("items", [])
            return [result["title"] for result in results[:5]]
        else:
            print("Google Custom Search API failed.")
            return []

    def fetch_industry_trends(self):
        """
        Searches for AI trends in the specified industry using Google Custom Search API.
        """
        query = f"{self.industry} AI trends"
        trends = self.google_search(query)
        return trends if trends else ["Electric Vehicles", "Autonomous Driving", "Supply Chain Optimization"]

    def gather_competitor_data(self):
        """
        Searches for top companies in the specified industry using Google Custom Search API.
        """
        query = f"{self.industry} top companies"
        competitors = self.google_search(query)
        return competitors if competitors else ["Competitor A", "Competitor B", "Competitor C"]

    def gather_industry_data(self):
        """
        Collects industry trends and competitor information and returns it as a dictionary.
        """
        trends = self.fetch_industry_trends()
        competitors = self.gather_competitor_data()
        industry_info = {
            "industry": self.industry,
            "key_trends": trends,
            "competitors": competitors
        }
        return industry_info


# New function to be imported in app.py
def fetch_industry_research(industry):
    """
    Function to instantiate the ResearchAgent class and fetch industry data.
    """
    agent = ResearchAgent(industry)
    return agent.gather_industry_data()