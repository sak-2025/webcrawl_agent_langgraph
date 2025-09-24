"""
Professional Web Scraper Agent using BrightData SERP + Google Gemini LLM

Features:
- Uses ReAct agent to query SERP
- Shows verbose ReAct steps (Thoughts → Actions → Observations → Final Answer)
- Clean logging and structured output
"""

import logging
import os
from dotenv import load_dotenv
from langchain_brightdata import BrightDataSERP
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

# ---------- Logging ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("web_scraper")

# ---------- Load Environment Variables ----------
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
BRIGHTDATA_ZONE = os.getenv("BRIGHT_DATA_ZONE")

if not GOOGLE_API_KEY:
    logger.error("GOOGLE_API_KEY not found in environment variables.")
    #print("Hi Hamudi")
    exit(1)

if not BRIGHTDATA_ZONE:
    logger.warning("BRIGHT_DATA_ZONE not found. BrightData SERP may not work correctly.")

# ---------- User Query ----------
user_query = "Latest developments Healthcare in Dubai"


# ---------- Initialize LLM ----------
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    api_key=GOOGLE_API_KEY,
    temperature=0.1
)


# ---------- Initialize BrightData SERP Tool ----------
serp_tool = BrightDataSERP(
    search_engine="google",
    country="ae",
    language="en",
    results_count=10,
    parse_results=True,
    zone=BRIGHTDATA_ZONE
)

logger.info("BrightData SERP tool configured successfully.")
logger.info(f"Search Engine: {serp_tool.search_engine} | Country: {serp_tool.country} | Language: {serp_tool.language} | Results Count: {serp_tool.results_count}")

# ---------- Create ReAct Agent ----------
agent = create_react_agent(
    model=llm,
    tools=[serp_tool],
    prompt="""You are a web researcher agent with access to BrightData SERP. 
Use the tool for the user's query, selecting appropriate country, language, 
search engine, or vertical if not specified.If you cannot find relevant information or the tool returns no results, respond with: "I don’t know.
"""
)

logger.info("ReAct Web Scraper Agent created successfully.")
logger.info("Agent is ready to search and analyze web content!")



# ---------- Run Agent and Stream Results ----------
logger.info(f"Running agent for query: {user_query}")
print("\n=== ReAct Agent Response ===")
print("="*100)

for step in agent.stream(
    {"messages": [("human", user_query)]},
    stream_mode="values",
):
    # Pretty-print each step (Thoughts → Actions → Observations → Partial Answer)
    step["messages"][-1].pretty_print()
