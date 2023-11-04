from telethon.sync import TelegramClient

# Replace with your API ID and API hash
api_id = 'your_api_id'
api_hash = 'your_api_hash'
# Replace with your bot's API token
bot_token = 'your bot API token'


# Replace with your preferred session file name
session_name = 'my_telegram_session'  # You can choose any name you like

# Replace with the target group's username or chat ID for example : @my_group
target_group_username = '@my_group'

# Define the message ID of the specific post you want to forward
message_id = 5  # Change this to the actual message ID you want to forward
# Replace with the target channel's id for example : @my_channel

async def forward_message():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        await client.start(bot_token=bot_token)

        try:
            # Fetch the message by its ID
            message = await client.get_messages('@my_channel', ids=message_id)

            # Send the message to the target group
            await client.send_message(target_group_username, message)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(forward_message())
