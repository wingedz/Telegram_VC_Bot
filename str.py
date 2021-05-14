import asyncio

from pyrogram import Client

TG = """
Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
and is released under the "GNU v3.0 License Agreement".
Please see < https://github.com/DevsExpo/blob/master/LICENSE >
All rights reserved.
"""

print(TG)
api_id = input("Enter Your API ID: \n")
api_hash = input("Enter Your API HASH : \n")


async def main():
    async with Client(":memory:", api_id=int(input("API ID:")), api_hash=input("API HASH:")) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
