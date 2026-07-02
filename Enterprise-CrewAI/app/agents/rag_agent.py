from crewai import Agent

from app.crew.llm import llm

rag_agent = Agent(

    role="Knowledge Assistant",

    goal="""
Answer questions using
company documents.

Policies

Invoices

Manuals

Knowledge Base
""",

    verbose=True,

    llm=llm
)