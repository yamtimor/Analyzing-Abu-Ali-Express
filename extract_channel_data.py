from telethon import TelegramClient
import asyncio
import json
from tqdm import tqdm

# Your API details and phone number
api_id = ''
api_hash = ''
phone = ''
channel_url = ''  # Use the username of the channel


async def fetch_messages(api_id, api_hash, channel_url):
    async with TelegramClient('session_name', api_id, api_hash) as client:
        print("Starting the Telegram client...")
        await client.start(phone)

        print(f"Fetching messages from the channel '{channel_url}'...")
        all_messages = await client.get_messages(channel_url, limit=None)

        print("Processing messages...")
        messages_data = []
        for message in tqdm(all_messages, desc="Processing Messages"):
            messages_data.append({
                'message_id': message.id,
                'sender_id': getattr(message.sender, 'id', None),
                'date': message.date.isoformat(),
                'content': message.text
            })

        return messages_data


async def main():
    messages = await fetch_messages(api_id, api_hash, channel_url)
    print("Saving messages to JSON file...")
    with open('abualiexpress_messages.json', 'w', encoding='utf-8') as file:
        json.dump(messages, file, ensure_ascii=False, indent=4)
    print("Script completed. Messages saved to abualiexpress_messages.json")


# Running the script
asyncio.run(main())
