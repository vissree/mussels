import bluetooth
import subprocess


# leave empty to use the default interface
server_address = ""
port = 0x1001

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind((server_address, port))
server_sock.listen(1)

try:
    client_sock, address = server_sock.accept()
    print(f"Accepted connection from {address}")

    try:
        while True:
            # receive the command from client
            cmd = client_sock.recv(1024).decode()

            if cmd:
                if cmd.lower() == "exit":
                    break

                # execute the command
                print(f"Executing: {cmd}")
                output = subprocess.getoutput(cmd)

                # send output back
                client_sock.send(output.encode())
    finally:
        client_sock.close()
finally:
    server_sock.close()
