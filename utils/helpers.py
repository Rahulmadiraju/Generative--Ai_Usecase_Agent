

# utils/helpers.py

def save_resources_to_markdown(resources, filename="output/resource_links.md"):
    """
    Saves the resource links to a markdown file.
    """
    with open(filename, "w") as file:
        file.write("# Resource Links\n\n")
        for resource in resources:
            file.write(f"- **{resource['use_case']}** (Feasibility: {resource['feasibility']}):\n")
            for link in resource["resource_links"]:
                file.write(f"  - {link}\n")


def generate_detailed_report(industry_data, use_cases, resources, recommendations, filename="output/report.md"):
    """
    Generates a detailed report in markdown format and saves it.
    """
    with open(filename, "w") as file:
        file.write("# Industry Analysis and Use Case Report\n\n")
        file.write(f"## Industry: {industry_data['industry']}\n")
        
        file.write("### Key Trends:\n")
        for trend in industry_data["key_trends"]:
            file.write(f"- {trend}\n")
        
        file.write("\n### Competitors:\n")
        for competitor in industry_data["competitors"]:
            file.write(f"- {competitor}\n")
        
        file.write("\n## Generated Use Cases (Prioritized):\n")
        for resource in resources:
            file.write(f"- **{resource['use_case']}** (Feasibility: {resource['feasibility']}):\n")
            for link in resource["resource_links"]:
                file.write(f"  - {link}\n")
        
        file.write("\n## GenAI Solution Recommendations:\n")
        for recommendation in recommendations:
            file.write(f"- {recommendation}\n")


def format_report(industry_research, use_cases, resources, recommendations):
    """
    Formats a detailed report as a string in markdown format.
    """
    report = "# AI Use Case and Resource Report\n\n"
    
    report += "## Industry Research\n"
    report += "- Industry: {}\n".format(industry_research['industry'])
    report += "- Key Trends:\n"
    for trend in industry_research['key_trends']:
        report += f"  - {trend}\n"
    
    report += "\n## Competitors:\n"
    for competitor in industry_research['competitors']:
        report += f"  - {competitor}\n"
    
    report += "\n## Generated Use Cases:\n"
    for use_case in use_cases:
        report += f"  - **{use_case['use_case']}** (Feasibility: {use_case['feasibility']}): {use_case['description']}\n"
    
    report += "\n## Resources for Use Cases:\n"
    for resource in resources:
        report += f"  - **{resource['use_case']}**: Feasibility: {resource['feasibility']}\n"
        for link in resource['resource_links']:
            report += f"    - {link}\n"
    
    report += "\n## GenAI Recommendations:\n"
    for recommendation in recommendations:
        report += f"  - {recommendation}\n"
    
    return report
