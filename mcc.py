# Modules
import requests
import json
import keyboard

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

print("This code is made for the purpose of learning how to use API's.\n")

# Functions
def check_status(ip):
    url = 'https://api.mcsrvstat.us/3/' + ip
    response = requests.get(url)
    data = json.loads(response.text)
    return data

data = check_status
ip = input("Enter the ip: ")

# Server status
print("\nSome information about " + ip)
if "online" in data(ip):
    if data(ip)["online"] == True:
        print("\nThe server is online")
    elif data(ip)["online"] == False:
        print("\nThe server is offline")
    else:
        print("\nSomething went wrong...")

# IP
if "ip" in data(ip):
    print("\nThe ip of the server is: " + str(data(ip)["ip"]))

# Port
if "port" in data(ip):
    print("\nThe port of the server is: " + str(data(ip)["port"]))

# Online players
if "players" in data(ip) and "online" in data(ip):
    online_players = str(data(ip)["players"]["online"])
    print("\nThe number of online players is: " + online_players)
else:
    print("\nPlayers: Something went wrong while trying to get the number of players...")

# Maximum players
if "players" in data(ip) and "max" in data(ip)["players"]:
    max_players = str(data(ip)["players"]["max"])
    print("\nThe maximum number of players is: " + max_players)
else:
    print("\nPlayers: Something went wrong while trying to get the maximum number of players...")


# Get the version
if "protocole" in data(ip) and "name" in data(ip)["version"]:
    version = str(data(ip)["version"]["name"])
    print("\nThe version of the server is: " + version)
else:
    print("\nSomething went wrong while trying to figure out the version...")

# Protocol version
if "protocol" in data(ip) and "version" in data(ip)["protocol"]:
    protocol_version = str(data(ip)["protocol"]["version"])
    print("\nThe protocol version of the server is: " + protocol_version)
else:
    print("\nSomething went wrong while trying to figure out the protocol version...")

# Software information
if "software" in data(ip):
    print("\nThe software of the server is: " + str(data(ip)["software"]))
else:
    print("\nSoftware: Software is undetected...")

# Gamemode
if "gamemode" in data(ip):
    print("\nThe gamemode of the server is: " + str(data(ip)["gamemode"]))
else:
    print("\nSomething went wrong while trying to get the gamemode...")

# Server ID
if "serverid" in data(ip):
    print("\nThe serverid of the server is: " + str(data(ip)["serverid"]))
else:
    print("\nServer ID: Server ID is undetected...")

# Motd
if "motd" in data(ip) and "clean" in data(ip)["motd"]:
    clean_motd = str(data(ip)["motd"]["clean"])
    print("\nThe clean motd of the server is: " + clean_motd)
else:
    print("\nMotd: Something went wrong while checking the motd...")

# Plugins
q1 = input("Would you like to see a list of all the plugins? (y/n): ")

if q1 == "y":
    if "plugins" in data(ip):
        print("\nThe plugins of the server are: " + str(data(ip)["plugins"]))
    else:
        print("\nPlugins: Plugins are undetected...")

# Mods
q2 = input("\nWould you like to see a list of all the mods? (y/n): ")

if q2 == "y":
    if "mods" in data(ip):
        print("\nThe mods of the server are: " + str(data(ip)["mods"]))
    else:
        print("\nMods: Mods are undetected...")

# Credits
        
print("\nMade with love by sidney :)")
print("Github: https://github.com/Bink-lab\n")

print("Press 'esc' to exit")
keyboard.wait("esc")


