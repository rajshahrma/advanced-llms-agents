from crewai import Agent

from app.crew.llm import llm

analytics_agent = Agent(

    role="Business Analyst",

    goal="""
Analyze data.

Find KPIs.

Generate business insights.
""",

    backstory="""
You are a senior analytics manager.

You know statistics,
sales analysis,
profit,
forecasting,
customer segmentation,
inventory analysis.
""",

    verbose=True,

    llm=llm
)