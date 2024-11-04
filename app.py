

# app.py

import streamlit as st
from pathlib import Path
import sys

# Add the project root to sys.path to ensure submodules can be found
project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

try:
    # Import agents and utils based on your project structure
    from agents.research_agent import fetch_industry_research  # Matches research_agent.py
    from agents.usecase_agent import UseCaseAgent              # Updated class import
    from agents.resource_agent import ResourceAgent            # Updated class import
    from agents.genai_recommendation_agent import GenAIRecommendationAgent  # Updated class import
    from utils.helpers import format_report                    # Now exists in helpers.py
except ModuleNotFoundError as e:
    st.error(f"Module import failed: {e}")
    st.stop()

# Streamlit UI elements
st.title("AI Use Case Generation for the Automotive Industry")

industry = st.text_input("Enter Industry", value="Automotive")
if st.button("Generate Report"):
    with st.spinner("Generating report..."):
        # Fetch industry research
        st.write("Industry research in progress...")
        industry_research = fetch_industry_research(industry)
        st.write("Industry research complete.")

        # Initialize agents
        use_case_agent = UseCaseAgent(industry_research)
        resource_agent = ResourceAgent(use_case_agent.generate_use_cases())
        recommendation_agent = GenAIRecommendationAgent(industry_research)

        # Generate use cases
        st.write("Generating use cases...")
        use_cases = use_case_agent.generate_use_cases()
        st.write("Use case generation complete.")

        # Fetch relevant resources
        st.write("Fetching resources...")
        resources = resource_agent.fetch_resources()
        st.write("Resource fetching complete.")

        # Generate GenAI recommendations
        st.write("Generating GenAI recommendations...")
        recommendations = recommendation_agent.generate_recommendations()
        st.write("GenAI recommendations complete.")

        # Format report
        st.write("Formatting report...")
        report_content = format_report(industry_research, use_cases, resources, recommendations)

        # Save report to output directory
        output_dir = project_root / "output"
        output_dir.mkdir(exist_ok=True)
        with open(output_dir / "report.md", "w") as file:
            if report_content:
                file.write(report_content)
            else:
                file.write("No report content generated.")

        # Display report content in Streamlit
        st.subheader("Generated Report")
        st.markdown(report_content if report_content else "None")

        st.success("Report generation complete!")
