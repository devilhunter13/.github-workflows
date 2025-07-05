from telethon import TelegramClient, events

# Ваши данные
api_id = '23362625'
api_hash = 'cacf51a73906a4d0e6b9cb2b5d151e50'
phone = '+79109838573'  # номер вашего аккаунта

# Канал(ы), из которых нужно пересылать сообщения
source_channels = ['@cashback_tyt', '@cash_wbb','https://t.me/+MoQXCLxvAO4xNDIy']
# Канал или чат, куда пересылать сообщения
destination_chat = 'https://t.me/+btpMy1KKyaIyNWRi'
# Фраза для фильтрации сообщений
keywords = ['Кэшбек 100 %',"Кешбек 100%",'кеш 100%','кэш 100%']  # замените на нужную вам фразу

session_name = 'my_session'
client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    message_text = event.message.message or ""
    # Проверяем наличие ключевой фразы в сообщении
    for keyword in keywords:
        if keyword.lower() in message_text.lower():
            await event.forward_to(destination_chat)
            print(f"Переслано сообщение из {event.chat.title}")
        else:
            print("Сообщение не содержит ключевую фразу, пропущено.")

async def main():
    await client.start()
    print("Бот запущен и слушает новые сообщения...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
