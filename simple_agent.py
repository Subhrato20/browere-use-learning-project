from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")

task ="""
Pick an ATS platform that many startups use, like greenhouse.io, lever.co, or workable.com.

Go to Google and type:
site:greenhouse.io
(This tells Google to only show results from that ATS website.)

Use Boolean search to filter job titles, levels, and locations:

Use " " to search for exact phrases

Use - to exclude unwanted terms

Use keywords like "software engineer" "entry" or "machine learning" etc.

Example search query:
site:greenhouse.io "software engineer" "entry" -senior -staff -lead -principal
(This finds entry-level SWE jobs and filters out senior roles.)

Scroll through results and click on listings directly from company ATS pages—these often aren’t posted on LinkedIn or other boards.
"""


async def main():
    agent = Agent(
        task=task,
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())