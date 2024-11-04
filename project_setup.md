# AI Use Case Generation for the Automotive Industry

This project uses a multi-agent architecture to generate relevant AI and Generative AI use cases for the **Automotive Industry**. The system consists of multiple agents that work together to conduct industry research, generate use cases, identify resources, and provide solution recommendations.

## Project Structure
- **agents/**: Contains individual agents responsible for each specific task.
- **utils/**: Contains helper functions.
- **output/**: Directory where generated reports and resource links are saved.
- **app.py**: Streamlit application to interactively generate reports.

## Setup Instructions

### Prerequisites
- Python 3.7 or later
- `pip` package manager

### Step 1: Clone the Repository
First, clone the project repository to your local machine:
```bash
git clone https://github.com/Rahulmadiraju/Generative--Ai_Usecase_Agent.git
cd <your-repo-folder>
```

### Step 2: Create a Virtual Environment
To keep dependencies isolated, create a virtual environment:
```bash
python -m venv env
```

### Step 3: Activate the Virtual Environment
Activate the virtual environment you just created:
- **On Windows:**
```bash
.\env\Scripts\activate
```
- **On MacOS/Linux:**
```bash
source env/bin/activate
```

### Step 4: Install the Required Packages:
```bash
pip install langchain llama_index huggingface_hub requests beautifulsoup4
pip install kaggle
pip install streamlit
```
### Step 5: Set Up API Keys
Ensure you have set up the necessary API keys for Google Custom Search API. Replace any API key placeholders in the agents directory files (e.g., ResearchAgent) with your own API keys.
### Step 6: Run the Streamlit Application
Start the Streamlit app by running:
```bash
streamlit run app.py
```
This command will open a web interface at http://localhost:8501.

### Usage Instructions
1. In the Streamlit interface, enter the industry name (e.g., "Automotive") into the text input field.
2. Click on Generate Report.
3. The app will display progress messages as each agent completes its task.
4. After completion, the generated report will be displayed under "Generated Report".
5. The full report is saved as ```output/report.md```, and resource links are saved in ```output/resource_links.md```.
