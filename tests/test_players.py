import socket

# Example usage: querying a game server
#   Server Name: MoonGamers.com | Est. 2004
#   IP: 51.81.48.224
#   Default Query Port: 23000
server_ip = '139.162.235.20'
server_port = 7778
timeout = 5.0

def query_players(ip, port):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Set a timeout for the socket (e.g., 5 seconds)
    try:
        sock.settimeout(float(timeout))
    except ValueError:
        print("Variable 'timeout' must be a float")# Craft the query packet
    packet = bytearray()
    packet += b'\\players\\'  # GameSpy query magic bytes
    # Send the packet to the server
    sock.sendto(packet, (ip, port))

    player_names = []  # List to store player names

    try:
        # Receive the response
        response, server_address = sock.recvfrom(4096)

        # Decode the response bytes into a string
        response_str = response.decode('utf-8')

        # Remove the leading and trailing backslashes
        response_str = response_str.strip('\\')

        # Split the response string into key-value pairs
        pairs = response_str.split('\\')

        print(f"Player Info = \n{pairs}\n\n")

        # Extract the player names
        for pair in pairs:
            if pair.startswith('player'):
                _, player_index = pair.split('_', 1)
                player_name = pairs[pairs.index(pair) + 1]
                player_names.append(player_name)

    except socket.timeout:
        print("Socket timed out. No response received from the server.")

    # Close the socket
    sock.close()

    return player_names

# Example usage: querying a game servers players
#   playername_0: Player Name

players = query_players(server_ip, server_port)

print(f"\n\n{players} \n\n")
# Print the player names
for player in players:
    print(player)

print(f"\nPlayer #4: {players[0]}")
