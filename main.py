import disnake
from disnake.ext import commands

# Creating and initializing the bot
bot = commands.Bot(command_prefix = "//", help_command = None, intents=disnake.Intents.all())

# Insert your bot token here
TOKEN = "your_token"

# List of censored words
CENSORED_WORD = ["bad", "cook", "python"]

# Message displayed when the bot starts up
@bot.event
async def on_ready():
    print(">>> Bot is ready to work")

# Event handler for incoming messages
@bot.event
async def on_message(message):

    # If the message is sent by the bot itself, ignore it
    if message.author.bot:
        return
    
    # List of forbidden words in the message (if any)
    all_word = []

    # Split the message into words
    for word in message.content.split():

        # Convert each word to lowercase for easier checking
        if word.lower() in CENSORED_WORD:
            # If the word is not already in the list, add it
            if word.lower() not in all_word:
                all_word.append(word)

    # If there are forbidden words, delete the message
    if all_word:
        try:
            # Create a string of the forbidden words, separated by commas
            after_check = ", ".join(all_word)

            # Save the author's name
            author = message.author

            # Delete the message
            await message.delete()

            # Log the deletion in the console
            print(f"Message has been deleted. Words: {after_check}. Author: {author.name}")

            # Send a message to the Discord chat notifying the author and the reason for deletion
            await message.channel.send(f"{author.mention}, *your message has been deleted.* \n          *Reason: use of the word:* **{after_check}**")
            
        # If deletion failed due to insufficient permissions, send an error message
        except disnake.Forbidden:
            await message.channel.send(f"**Message deletion error. The bot does not have sufficient permissions. Fix this so that the bot can work correctly.**")
            print(f"Message deletion error. The bot does not have sufficient permissions. Fix this so that the bot can work correctly. Word: {after_check}. Author: {author.name}")

bot.run(TOKEN)
