import GameSpy
import time

#server_ip = '51.81.48.224'      # Set the server IP
#server_port = 23000             # Set the server Query Port

server_ip = '74.91.125.111'    # Set the server IP
server_port = 2302             # Set the server Query Port

##################### Server Info Query #####################

# Create an instance of the query class
info = GameSpy.Query()  

start_time = time.time()               # This is only for the query time execution

# Query the server
server_info = info.info(server_ip, server_port)

end_time = time.time()                 # This is only for the query time execution
execution_time = end_time - start_time # This is only for the query time execution

print("\nServer Info Query\n")

print("\nAll Server Info\n")
# Print the extracted key-value pairs
for key, value in server_info.items():
    print(f"{key}: {value}")

try:
    print(f"\nServer Name: {server_info['hostname']}")
    print(f"Server Map: {server_info['mapname']}")
    print(f"Server Max Players: {server_info['maxplayers']}")
    print(f"Server Players: {server_info['numplayers']}")
except KeyError:
    pass

print(f"\nQuery Execution Time: {execution_time:.2f} seconds")

##################### Player Info Query #####################

print("\n##################### Player Info Query #####################\n")
# Some games do not allow you to see all player names... 
# Its annoying, I tried everything I could think of to get it to work

# Create an instance of the query class
players = GameSpy.Query()  

start_time = time.time()               # This is only for the query time execution

# Query the server
server_players = players.players(server_ip, server_port)

end_time = time.time()                 # This is only for the query time execution
execution_time = end_time - start_time # This is only for the query time execution

print("\nAll Player Info\n")

player_index = 1

# Print the player names
for player in server_players:
    print(f"{player_index}. {player}")
    player_index += 1

# I'm not happy with not being able to access the other player info
# so this may be changed to a dictionary later
# for now, you can only access player names

try:
    print(f"\nPlayer #1: {server_players[0]}")
    print(f"Player #2: {server_players[1]}")
    print(f"Player #3: {server_players[2]}")
    print(f"Player #4: {server_players[3]}")
except IndexError:
    pass

print(f"\nQuery Execution Time: {execution_time:.2f} seconds")

##################### Server Rules Query #####################

print("\n##################### Server Rules Query #####################\n")

# Create an instance of the query class
rules = GameSpy.Query()  

start_time = time.time()               # This is only for the query time execution

# Query the server
server_rules = rules.rules(server_ip, server_port)

end_time = time.time()                 # This is only for the query time execution
execution_time = end_time - start_time # This is only for the query time execution

print("\nAll Server Rules\n")

# Print the extracted key-value pairs
for key, value in server_info.items():
    print(f"{key}: {value}")

# All servers wont have the same rules, but this is how you retrieve rules
#print(f"\nFree Camera: {server_rules['free_camera']}")

print(f"\nQuery Execution Time: {execution_time:.2f} seconds")