import requests
import json
import keyboard
import webbrowser
import time

def n():
    print("")

print(""" ______  _________ _        _             _        _______  ______  
(  ___ \ \__   __/( (    /|| \    /\     ( \      (  ___  )(  ___ \ 
| (   ) )   ) (   |  \  ( ||  \  / /     | (      | (   ) || (   ) )
| (__/ /    | |   |   \ | ||  (_/ /_____ | |      | (___) || (__/ / 
|  __ (     | |   | (\ \) ||   _ ((_____)| |      |  ___  ||  __ (  
| (  \ \    | |   | | \   ||  ( \ \      | |      | (   ) || (  \ \ 
| )___) )___) (___| )  \  ||  /  \ \     | (____/\| )   ( || )___) )
|/ \___/ \_______/|/    )_)|_/    \/     (_______/|/     \||/ \___/ 
                                                                    \n""")

print("This code is made for the purpose of learning how to use the roblox API\n")
print("Please dont abuse :)\n")

def check(id):
    url = "https://users.roblox.com/v1/users/" + id
    response = requests.get(url)
    data = json.loads(response.text)
    return data


id = input("Enter the id: ")
data = check(id)
if "name" in data:
    n()
    print("The name of this user is: " + data["name"])
n()
if "description" in data:
    print("The description of this user is: " + data["description"])
n()
if "created" in data:
    print("The creation date of this user is: " + data["created"])
n()
if "isBanned" in data:
    print("Ban status of this user is: " + str(data["isBanned"]))
n()

print("Made with love by sidney :)")
print("Github: https://github.com/Bink-lab")
n()
print("Press 'esc' to exit")
keyboard.wait("esc")
exit()
