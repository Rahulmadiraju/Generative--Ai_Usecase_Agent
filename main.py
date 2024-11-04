

# main.py
from agents.research_agent import ResearchAgent
from agents.usecase_agent import UseCaseAgent
from agents.resource_agent import ResourceAgent
from agents.genai_recommendation_agent import GenAIRecommendationAgent
from utils.helpers import save_resources_to_markdown, generate_detailed_report

def main():
    industry = "Automotive"  # Specify the industry of interest

    # Initialize agents
    research_agent = ResearchAgent(industry)
    industry_data = research_agent.gather_industry_data()

    use_case_agent = UseCaseAgent(industry_data)
    use_cases = use_case_agent.generate_use_cases()

    resource_agent = ResourceAgent(use_cases)
    resources = resource_agent.fetch_resources()

    recommendation_agent = GenAIRecommendationAgent(industry_data)
    recommendations = recommendation_agent.generate_recommendations()

    # Save results to markdown files
    save_resources_to_markdown(resources)
    generate_detailed_report(industry_data, use_cases, resources, recommendations)
    print("Detailed report saved to output/report.md and resources saved to output/resource_links.md")

if __name__ == "__main__":
    main()
