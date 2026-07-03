from app.tools.sql_tool import SQLQueryTool

sql_agent = Agent(

    role="Senior SQL Engineer",

    goal="Generate and execute SQL",

    tools=[SQLQueryTool()],

    llm=llm,

    verbose=True
)