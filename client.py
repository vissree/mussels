import sys
import bluetooth


if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <SERVER_ADDR>")
    sys.exit(1)

server_address = sys.argv[1]
port = 0x1001

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print(f"Trying to connecto to {server_address} on 0x{port}...")
sock.connect((server_address, port))
print("Connected...")

try:
    while True:
        data = input()
        sock.send(data.encode())
        data = sock.recv(1024).decode()
        print(f"Data received: {data}")
finally:
    sock.close()
