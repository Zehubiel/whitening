from pyrogram import Client, Filters, Message

import config


app = Client(
    session_name=config.USER_PHONE[1:],
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    phone_number=config.USER_PHONE,
)


@app.on_message(Filters.me & Filters.command(['start', 'help'], prefixes='.'))
async def help_handler(_, message: Message):
    args = message.text.split(maxsplit=2)
    if 'ru' in args:
        text = f'**Telecharm v{config.TELECHARM_VERSION}**:\n\n`.help` - Показать это сообщение.\n' \
               '`.stats` - Статистика моего профиля.\n`.flood` - Флуд сообщениями.\n`.purge` - Очистка сообщений\n' \
               '`.name` - Сменить моё имя\n`.username` - Сменить мой юзернейм\n`.bio` - Отредактировать "О себе"\n' \
               f'`.mention` - Текстовое упоминание\n\n__[Подробнее о командах]({config.GUIDE_LINK_RU})\n' \
               f'[Telecharm на GitHub]({config.GITHUB_LINK})__'
    else:
        text = f'**Telecharm v{config.TELECHARM_VERSION}**:\n`.help ru` for Russian\n\n`.help` - Show this message.\n' \
               '`.stats` - My profile stats.\n`.flood` - Flood messages.\n`.purge` - Purge messages\n' \
               '`.name` - Change my name\n`.username` - Change my username\n`.bio` - Edit my about info\n' \
               f'`.mention` - Text mention\n\n__[More on commands]({config.GUIDE_LINK_EN})\n' \
               f'[Telecharm on GitHub]({config.GITHUB_LINK})__'

    await message.edit_text(text, disable_web_page_preview=True)


if __name__ == '__main__':
    app.run()
