from fastmcp import FastMCP
from pathlib import Path
import asyncio

mcp = FastMCP(name="Blog_Automation")


@mcp.tool
async def add(a: int, b: int) -> int:
    return a + b


@mcp.resource(
    "resource://blog_template",
    description="use this blog template to generate the blog structure",
)
async def blog_template():
    file_path = Path("resources/blog_template.md")
    return file_path.read_text(encoding="utf-8")


if __name__ == "__main__":
    mcp.run()
