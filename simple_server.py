# ripoff from bluez examples
import bluetooth


# leave blank to use the default interface
server_address = ""
port = 0x1001

server_sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
server_sock.bind((server_address, port))
server_sock.listen(1)

try:
    client_sock, address = server_sock.accept()
    print(f"Accepted connection from {address}")

    try:
        data = client_sock.recv(1024)
        print(f"Data received: {str(data)}")

        while data:
            client_sock.send(f"Echo => {str(data)}")
            data = client_sock.recv(1024)
            print(f"Data received: {str(data)}")
    finally:
        client_sock.close()

finally:
    server_sock.close()
