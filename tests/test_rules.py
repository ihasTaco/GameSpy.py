import socket

# Example usage: querying a game server
#   Server Name: MoonGamers.com | Est. 2004
#   IP: 51.81.48.224
#   Default Query Port: 23000
server_ip = '51.81.48.224'
server_port = 23000
timeout = 5.0

def query_info(ip, port):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Set a timeout for the socket (e.g., 5 seconds)
    try:
        sock.settimeout(float(timeout))
    except ValueError:
        print("Variable 'timeout' must be a float")

    # Craft the query packet
    packet = bytearray()
    packet += b'\\rules\\'  # GameSpy query magic bytes
    # Send the packet to the server
    sock.sendto(packet, (ip, port))

    try:
        # Receive the response
        response, server_address = sock.recvfrom(4096)

        # Decode the response bytes into a string
        response_str = response.decode('utf-8')

        # Remove the leading and trailing backslashes
        response_str = response_str.strip('\\')

        # Split the response string into key-value pairs
        pairs = response_str.split('\\')

        # Extract the key-value pairs
        info_dict = {}
        for i in range(0, len(pairs), 2):
            key = pairs[i]
            value = pairs[i + 1]
            info_dict[key] = value

    except socket.timeout:
        print("Socket timed out. No response received from the server.")

    # Close the socket
    sock.close()

    return info_dict

# Testing Use Only! #
info_dict = query_info(server_ip, server_port)

# Print the extracted key-value pairs
for key, value in info_dict.items():
    print(f"{key}: {value}")

#print(f"\n\nServer Name: {info_dict['hostname']}")
#print(f"Server Map: {info_dict['mapname']}")
#print(f"Server Max Players: {info_dict['maxplayers']}")
#print(f"Server Players: {info_dict['numplayers']}")