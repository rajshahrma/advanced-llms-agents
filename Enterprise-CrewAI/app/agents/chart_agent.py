from crewai import Agent

from app.crew.llm import llm

chart_agent = Agent(

    role="Visualization Expert",

    goal="""
Recommend
the best chart.

Bar

Pie

Line

Scatter

Heatmap
""",

    verbose=True,

    llm=llm
)