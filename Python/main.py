# Modules
import requests
import json
import keyboard
from colorama import Fore, Style

#################################################################################################################
# Functions
def check_user(id):
    url = "https://users.roblox.com/v1/users/" + id
    response = requests.get(url)
    data = json.loads(response.text)
    return data
def check_friends(id):
    url = 'https://friends.roblox.com/v1/users/' + id + '/friends/count'
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def check_premium(id):
    url = 'https://premiumfeatures.roblox.com/v1/users/' + id + '/validate-membership'
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def check_followers(id):
    url = 'https://friends.roblox.com/v1/users/' + id + '/followings/count'
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def print_colored(text, color):
    colored_text = f"{color}{text}{Style.RESET_ALL}"
    print(colored_text)

#################################################################################################################

print("""
 ▄▄▄▄    ██▓ ███▄    █  ██ ▄█▀ ██▓    ▄▄▄       ▄▄▄▄   
▓█████▄ ▓██▒ ██ ▀█   █  ██▄█▒ ▓██▒   ▒████▄    ▓█████▄ 
▒██▒ ▄██▒██▒▓██  ▀█ ██▒▓███▄░ ▒██░   ▒██  ▀█▄  ▒██▒ ▄██
▒██░█▀  ░██░▓██▒  ▐▌██▒▓██ █▄ ▒██░   ░██▄▄▄▄██ ▒██░█▀  
░▓█  ▀█▓░██░▒██░   ▓██░▒██▒ █▄░██████▒▓█   ▓██▒░▓█  ▀█▓
░▒▓███▀▒░▓  ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒░ ▒░▓  ░▒▒   ▓▒█░░▒▓███▀▒
▒░▒   ░  ▒ ░░ ░░   ░ ▒░░ ░▒ ▒░░ ░ ▒  ░ ▒   ▒▒ ░▒░▒   ░ 
 ░    ░  ▒ ░   ░   ░ ░ ░ ░░ ░   ░ ░    ░   ▒    ░    ░ 
 ░       ░           ░ ░  ░       ░  ░     ░  ░ ░      
      ░                                              ░ \n""")

print("This code is made for the purpose of learning how to use the roblox API.\n")

#################################################################################################################
# Get data
id = input("Enter the id: ")
user_data = check_user(id)
friends_data = check_friends(id)
check_premium = check_premium(id)
check_followers = check_followers(id)

print_colored("\nSome user information", Fore.GREEN)

if "name" in user_data:
    print("\nThe name of this user is: " + user_data["name"])

if "description" in user_data:
    print("\nThe description of this user is: " + user_data["description"])

if "count" in friends_data:
    print("\nThe user has " + str(friends_data["count"]) + " friends")

if "count" in check_followers:
    print("\nThe user has " + str(check_followers["count"]) + " followers")

if "created" in user_data:
    print("\nThe creation date of this user is: " + user_data["created"])

if "isBanned" in user_data:
    print("\nBan status of this user is: " + str(user_data["isBanned"]))

# Check for premium subscription
print_colored("\nPremium subscription?", Fore.YELLOW)
if check_premium:
    print("\nThis user has a premium subscription (might be broken)\n")
elif not check_premium:
    print("\nThis user does not have a premium subscription (might be broken)\n")
else:
    print("\nSomething went wrong...\n")
#################################################################################################################

# Credits :)
print("Made with love by sidney :)")
print("Github: https://github.com/Bink-lab\n")
print("Press 'esc' to exit")
keyboard.wait("esc")
