from fastmcp import FastMCP
import asyncio

mcp = FastMCP(name="Blog_Automation")


@mcp.tool
async def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    mcp.run()
