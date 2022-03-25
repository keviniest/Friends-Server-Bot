import re
import discord

import command

client = discord.Client()  # Creates a client instance
prefix = '?'  # The bot prefix
# List of modules (commands)
commands = [
	command.Info('info'),
	command.Help('help')
]
event = None


# reads and returns content of file called "token.txt"
# (which is usually the bot's authentication token)
def get_token() -> str:
	with open('token.txt', 'r') as f:
		return f.read()


# This method is called everytime the bot starts up
@client.event
async def on_ready():
	print(f'Logged in as {client.user}')
	# Sets the bot's rich presence ("watching 💌 friends!")
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='💌 friends!'))


# This method is called everytime message is received from any of the server that the bot is in.
@client.event
async def on_message(message):
	# Don't do anything if message was sent by this bot itself or doesn't start with the prefix
	if message.author == client.user or list(message.content)[0] != prefix:
		return

	global event
	event = message
	msg = message.content
	msg = msg[len(prefix):]  # Prefix gets stripped from the message

	if len(re.split('\\s+', msg)[0]) > 0:
		# the name of the command (the first argument without the prefix)
		command_name = re.split('\\s+', msg)[0]

		# Iterates through list of commands
		for c in commands:
			# Finds command matching command_name
			if c.name == command_name:
				# Calls on_command function in the child with the matching name
				await c.on_command(re.split('\\s+', msg)[0:len(re.split('\\s+', msg))], msg, message)
				break


client.run(get_token())
