import bluetooth
import subprocess


# leave empty to use the default interface
server_address = ""
port = 0x1001

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind((server_address, port))
server_sock.listen(1)

while True:
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

                # split the cmd into a list
                res = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = res.communicate()

                # send output back
                if stdout:
                    client_sock.send(f"STDOUT:\n{stdout.decode()}")

                if stderr:
                    client_sock.send(f"\nSTDERR:\n{stderr.decode()}")
    finally:
        client_sock.close()

server_sock.close()
