#!/usr/bin/env python3

import logging
import os

from pyrogram import Client, filters, types

import config

app = Client(
    name="Reaction Userbot Session",
    api_id=config.api_id,
    api_hash=config.api_hash,
)


@app.on_message(filters=filters.user(config.users), group=config.chat)
async def reaction_handler(client: Client, message: types.Message):
    logging.info(f"New {config.reaction}: {message}")
    await client.send_reaction(message.chat.id, message.id, config.reaction)


if __name__ == "__main__":
    logging.basicConfig(
        handlers=[
            logging.StreamHandler(),
        ],
        level=os.getenv("LOGLEVEL", "INFO").upper(),
        format="[%(asctime)s.%(msecs)03d] [%(name)s] [%(levelname)s]: %(message)s",
        datefmt=r"%Y-%m-%dT%H-%M-%S",
    )

    app.run()
