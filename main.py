import re
import discord

import command

client = discord.Client()  # Creates a client instance
prefix = '?'
commands = [command.Info, command.Help]  # List of modules (commands)
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
	# Don't do anything if message doesn't starts with the prefix
	if message.content[0] != prefix:
		return

	global event
	event = message
	msg = message.content
	msg = msg[len(prefix):]  # Prefix gets stripped from the message
	command_found = False  # Checks if command is found

	if len(re.split('\\s+', msg)[0]) > 0:
		# the name of the command (the first argument without the prefix)
		command_name = re.split('\\s+', msg)[0]

		# Iterates through list of commands
		for c in commands:
			# Finds command matching command_name
			if c.name == command_name:
				# Calls on_command function in the child with the matching name
				c.on_command(args=re.split('\\s+', msg)[0:len(re.split('\\s+', msg))], command=msg)
				command_found = True  # Command is found
				break

	# Command is not found after iterating through the array of commands
	if not command_found:
		await message.channel.send("Command not found")


client.run(get_token())
