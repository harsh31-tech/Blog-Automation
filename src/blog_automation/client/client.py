from fastmcp import Client
import asyncio


async def main():
    client = Client("src/blog_automation/server/server.py")

    async with client:
        print("Client connected to MCP server")

        # result = await client.list_tools()
        # print(result)
        
        resource = await client.list_resources()
        read_resource = await client.read_resource("resource://blog_template")
        print(resource)
        print(read_resource[0].text)


if __name__ == "__main__":
    asyncio.run(main())
