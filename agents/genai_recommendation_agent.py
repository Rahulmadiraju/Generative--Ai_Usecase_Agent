

# agents/genai_recommendation_agent.py
from langchain.prompts import PromptTemplate

class GenAIRecommendationAgent:
    def __init__(self, industry_data):
        self.industry_data = industry_data

    def generate_recommendations(self):
        """
        Suggests GenAI solutions for the specified industry, such as chatbots and document search.
        """
        template = """
        Based on industry trends, suggest GenAI solutions for the {industry} sector. 
        Consider AI-driven document search, automated reporting, and customer service chatbots.
        """
        prompt = PromptTemplate(input_variables=["industry"], template=template)
        prompt_text = prompt.format(industry=self.industry_data["industry"])

        recommendations = [
            "AI-powered chatbot for vehicle maintenance inquiries",
            "Automated report generation on vehicle health and maintenance needs",
            "Document search for internal parts inventory and diagnostics"
        ]
        return recommendations
