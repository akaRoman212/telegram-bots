import telegram

def send_telegram_notification(token, chat_id, message):
    try:
        bot = telegram.Bot(token=token)
        response = bot.send_message(chat_id=chat_id, text=message)
        print("Notification sent successfully:", response)
    except Exception as e:
        print("Error sending notification:", e)

if __name__ == "__main__":
    bot_token = "6756284122:AAGQMQBKhhVII_SQJpXe1GBQ8zLbjUSSO38"
    chat_id = "-4038816099"
    notification_message = 'Hello, this is a notification from your Python script!'

    send_telegram_notification(bot_token, chat_id, notification_message)



# import asyncio

# import telegram
# async def send_telegram_notification(token, chat_id, message):
#     try:
#         bot = telegram.Bot(token=token)
#         response = await bot.send_message(chat_id=chat_id, text=message)
#         print("Notification sent successfully:", response)
#     except Exception as e:
#         print("Error sending notification:", e)

# async def main(msg):
#     bot_token = "6756284122:AAGQMQBKhhVII_SQJpXe1GBQ8zLbjUSSO38"
#     chat_id = "-4038816099"
    

#     await send_telegram_notification(bot_token, chat_id, msg)

# if __name__ == "__main__":
#    asyncio.get_event_loop().run_until_complete(main())
