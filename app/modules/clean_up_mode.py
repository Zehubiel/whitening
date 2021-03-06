import asyncio
from typing import Union

from pyrogram import Client
from pyrogram.errors import RPCError

from storage import json_settings


async def clean_up(client: Client, chat_id: Union[int, str], message_id: int, clear_after: int = 3.5) -> None:
    """
    Delete a message shortly after editing if cleaning up is enabled.

    :param client: Running pyrogram client
    :param chat_id: Chat ID
    :param message_id: Message ID
    :param clear_after: Time in seconds to wait before deleting
    :return:
    """
    if clear_after > 0 and json_settings.data.get('clean_up', False) is True:
        await asyncio.sleep(clear_after)
        try:
            await client.delete_messages(chat_id, message_id)
        except RPCError:
            return
