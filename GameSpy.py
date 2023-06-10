import socket

class Query:
    def __init__(self):
        self.timeout = 5.0

    def info(self, ip, port):
        response = self._send_query(ip, port, b'\\info\\')
        info_dict = self._process_response(response)
        return info_dict

    def players(self, ip, port):
        players = []
        page = 0
        previous_players = set()
    
        while True:
            response = self._send_query(ip, port, f'\\players\\{page}\\'.encode())
            page_players = self._process_players_response(response)
            if not page_players or all(player in previous_players for player in page_players):
                break
            players.extend(player for player in page_players if player not in previous_players)
            previous_players.update(page_players)
            page += 1
    
        return players

    def rules(self, ip, port):
        response = self._send_query(ip, port, b'\\rules\\')
        info_dict = self._process_response(response)
        return info_dict

    def _send_query(self, ip, port, query_packet):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            sock.settimeout(float(self.timeout))
        except ValueError:
            print("Variable 'timeout' must be a float")
            return None

        sock.sendto(query_packet, (ip, port))

        try:
            response, _ = sock.recvfrom(65536)
            return response

        except (socket.timeout, TimeoutError):
            raise TimeoutError("Server is offline or can't be reached")

        finally:
            sock.close()

    def _process_response(self, response):
        response_str = response.decode('utf-8', errors='replace')
        response_str = response_str.strip('\\')

        pairs = response_str.split('\\')
        info_dict = {}
        for i in range(0, len(pairs), 2):
            key = pairs[i]
            value = pairs[i + 1] if i + 1 < len(pairs) else None
            info_dict[key] = value

        return info_dict

    def _process_players_response(self, response):
        response_str = response.decode('utf-8', errors='replace')
        response_str = response_str.strip('\\')
    
        pairs = response_str.split('\\')
        players = []
        added_players = set()  # Track added players to eliminate duplicates
    
        for pair in pairs:
            if pair.startswith('player_') and not pair.startswith('player_flags'):
                _, player_index = pair.split('_', 1)
                player_name = pairs[pairs.index(pair) + 1]
    
                if player_name.isdigit():
                    continue
                
                if player_name not in added_players:  # Check for duplicates
                    players.append(player_name)
                    added_players.add(player_name)
    
        return players

class TimeoutError(Exception):
    pass