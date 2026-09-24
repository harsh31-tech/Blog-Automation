from fastmcp import Client
import asyncio


async def main():
    client = Client("src/blog_automation/server/server.py")

    async with client:
        print("Client connected to MCP server")

        result = await client.list_tools()
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
