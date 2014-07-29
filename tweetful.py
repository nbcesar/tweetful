import requests
import sys
import argparse
import json
import authorize
from urls import *
 
def make_parser():
	''' Construct the command line parser '''
	description = 'Twitter App'
	parser = argparse.ArgumentParser(description = description)

	subparsers = parser.add_subparsers(help="Available commands")

	# Subparsers for the timeline command
	timeline_parser = subparsers.add_parser("timeline", help="Retrieve timeline")
	timeline_parser.set_defaults(command="timeline")

	# Subparsers for friends
	friends_parser = subparsers.add_parser('friends', help="Get a list of friends")
	friends_parser.set_defaults(command="friends")

	# Subparsers for friends
	followers_parser = subparsers.add_parser('followers', help="Get a list of followers")
	followers_parser.set_defaults(command="followers")

	return parser

def getFriends():
	friends = []
	users = response.users
	for user in users:
		print user

def main():
	""" Main function """
	parser = make_parser()
	arguments = parser.parse_args(sys.argv[1:])
	arguments = vars(arguments)
	command = arguments.pop('command')

	auth = authorize.authorize()
 	
	if command == 'timeline':
		response = requests.get(TIMELINE_URL, auth=auth)
		print response.json()

	if command == 'friends':
		response = requests.get(FRIENDS_URL, auth=auth)
		#print response.json()
		for c in response.json()['users']:
			print c['name']

	if command == 'followers':
		response = requests.get(FOLLOWERS_URL, auth=auth)
		#print response.json()
		for c in response.json()['users']:
			print c['name']

if __name__ == "__main__":
	main()