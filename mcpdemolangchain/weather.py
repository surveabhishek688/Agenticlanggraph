from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """Get the Weather Location."""
    return "Its always raining in Bangalore"

if __name__=="__main__":
    mcp.run(transport="streamable-http")