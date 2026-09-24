from fastmcp import Client
import asyncio


async def main():
    client = Client("src/blog_automation/server/server.py")

    async with client:
        print("server and client is connected")


if __name__ == "__main__":
    asyncio.run(main())
