

# agents/usecase_agent.py
from langchain.prompts import PromptTemplate

class UseCaseAgent:
    def __init__(self, industry_data):
        self.industry_data = industry_data

    def generate_use_cases(self):
        """
        Generates AI use cases based on industry trends and competitors,
        including feasibility ratings and references to trends.
        """
        template = """
        Based on the trends and competitors provided, generate specific AI/GenAI use cases 
        for the {industry} sector. Each use case should include a brief description, 
        a feasibility rating (High, Medium, Low), and a reference to relevant trends or competitors.
        """
        prompt = PromptTemplate(input_variables=["trends", "industry"], template=template)
        prompt_text = prompt.format(
            trends=", ".join(self.industry_data["key_trends"]),
            industry=self.industry_data["industry"]
        )

        # Sample use cases with trend references
        use_cases = [
            {
                "use_case": "Predictive Maintenance for Electric Vehicles",
                "description": "AI-driven diagnostics for early vehicle maintenance.",
                "feasibility": "High",
                "reference": f"Trend: {self.industry_data['key_trends'][0]}"
            },
            {
                "use_case": "AI-driven Supply Chain Optimization",
                "description": "Optimizing supply chain logistics using AI models.",
                "feasibility": "Medium",
                "reference": f"Competitor: {self.industry_data['competitors'][1]}"
            },
            {
                "use_case": "Customer Sentiment Analysis on Social Media",
                "description": "Analyzing social media feedback for customer insights.",
                "feasibility": "Medium",
                "reference": f"Trend: {self.industry_data['key_trends'][2]}"
            }
        ]
        return use_cases
