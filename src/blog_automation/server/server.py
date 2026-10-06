from fastmcp import FastMCP
from pathlib import Path
import asyncio

mcp = FastMCP(name="Blog_Automation")


@mcp.resource(
    "resource://blog_template",
    description="use this blog template to generate the blog structure",
)
async def blog_template():
    file_path = Path("resources/blog_template.md")
    return file_path.read_text(encoding="utf-8")

@mcp.resource(
    "resource://writing_guidelines",
    description="use this writing guideline to generate the blog content",
)
async def writing_guidelines():
    file_path = Path("resources/writing_guidelines.md")
    return file_path.read_text(encoding="utf-8")

@mcp.resource(
    "resource://examples/triz-problem-solving",
    description="use this example to take reference for generating the blog",
)
async def example1():
    file_path = Path("resources/examples/triz-problem-solving.md")
    return file_path.read_text(encoding="utf-8")
@mcp.resource(
    "resource://examples/mcp-automation-architecture",
    description="use this example to take reference for generating the blog",
)
async def example2():
    file_path = Path("resources/examples/mcp-automation-architecture.md")
    return file_path.read_text(encoding="utf-8")
@mcp.resource(
    "resource://examples/llm-prompt-engineering",
    description="use this example to take reference for generating the blog",
)
async def example3():
    file_path = Path("resources/examples/llm-prompt-engineering.md")
    return file_path.read_text(encoding="utf-8")



@mcp.prompt
def blog_generation(topic: str) -> str:
    return f"""  Generate a technical blog about the provided topic.
 {topic}
Use:
- the blog template
- the writing guidelines
- the example blogs

Follow the required Markdown structure and writing style.
Keep technical claims accurate.
Return only the completed blog."""


if __name__ == "__main__":
    mcp.run()
