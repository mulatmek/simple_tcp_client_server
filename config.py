import socket
import re
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT =  'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

def parse_version(s: str):
    parts = s.split('-')
    nums = []
    for token in reversed(parts):
        if token.isdigit():
            nums.append(int(token))
            if token == "8":   # stop once we hit major version 8
                break
        else:
            break
    return tuple(reversed(nums))

print(parse_version("k2c-cnode-latest-2025-09-25-2026-8-5-98-10"))
# (8, 6, 10)

print(parse_version("k2c-cnode-latest-2025-09-25-2026-8-6-19"))