**ReAct Web Research Agent**

A professional Python agent that leverages BrightData SERP and Google Gemini LLM to perform intelligent web searches and summarize results in a concise, structured way. Built using LangChain and LangGraph with full ReAct reasoning support.

**Features**

Uses ReAct pattern: Reason → Act → Observe → Respond.

Integrates BrightData SERP to fetch web results programmatically.

Powered by Google Gemini LLM for natural language understanding and summarization.

Streams step-by-step reasoning, showing thoughts, tool actions, and observations.

Simple, modular, and production-ready Python code.


**Requirements**

Python 3.10+

pip packages (install via requirements.txt):

pip install langchain_brightdata langchain_google_genai langgraph python-dotenv


**Environment variables:**

GOOGLE_API_KEY=<your_google_api_key>
BRIGHT_DATA_ZONE=<your_brightdata_zone>
Store these in a .env file at the project root.

**Installation**

Clone the repository:
git clone https://github.com/sak-2025/webcrawl_agent_langgraph.git
cd react-web-scraper


**Create a virtual environment:**

python -m venv myenv
myenv\Scripts\activate     # Windows


**Install dependencies:**
pip install -r requirements.txt

**Create a .env file:**

GOOGLE_API_KEY=your_google_api_key_here
BRIGHT_DATA_ZONE=your_brightdata_zone_here

**Usage**
Run the Agent
python web_crawl.py


**By default, the script runs a sample query:**

Thought: I need to search for recent healthcare developments in Dubai, UAE.
Action: BrightDataSERP
Action Input: {"query": "latest healthcare developments in Dubai", "country": "ae", "language": "en", "num_results": 10}

Observation: Retrieved multiple results including news from Gulf News, Khaleej Times, and Dubai Health Authority updates. Key points include new hospital openings, digital health initiatives, and medical research collaborations.

Thought: Summarize these findings concisely for the user.
Final Answer:

Healthcare in Dubai, UAE, has seen several recent developments:

**File Structure**
.
├── web_crawl.py        # Main script
├── requirements.txt    # Python dependencies
├── .env                # API keys not included
└── README.md

**Notes**

BrightData SERP must have a valid Zone configured in .env.
The agent  uses the ReAct workflow internally.
Step-by-step reasoning helps debug or understand how the agent reaches its conclusions.
