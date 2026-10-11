from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio


async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mcpdemolangchain/mathserver.py"], ## Ensure correct absolute path
                "transport":"stdio",
            },
            "weather":{
                "url":"http://localhost:8000/mcp", #Ensure server is running
                "transport":"streamable_http"
            }

        }
    )

    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    tools=await client.get_tools()
    model=ChatGroq(model="openai/gpt-oss-120b")
    agent=create_agent(model,tools)
    math_response=await agent.ainvoke(
        {"messages":"Whats (3+5)*12"}
    )

    print("Math Reponse:", math_response["messages"][-1].content)

    weather_response=await agent.ainvoke(
            {"messages":"Whats weather in the bangalore"}
        )
    
    print("Weather Reponse:", weather_response["messages"][-1].content)

asyncio.run(main())