from crewai import Agent

from app.crew.llm import llm

sql_agent = Agent(

    role="Senior SQL Engineer",

    goal="""
Generate efficient SQL queries
for MySQL databases.
""",

    backstory="""
You are an expert database engineer.

You understand joins,
aggregations,
group by,
window functions,
CTEs,
date filtering,
optimization,
indexes,
and analytics.
""",

    verbose=True,

    allow_delegation=False,

    llm=llm
)