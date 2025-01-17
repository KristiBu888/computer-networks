import socket
import threading

# Connection Data
HOST = "127.0.0.1"
PORT = 55555

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket()
client.connect((HOST, PORT))


# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode("UTF-8")
            if message == "NICK":
                client.send(nickname.encode("UTF-8"))
            else:
                print(f"\033[32m {message} \033[0m")
        except Exception:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        message = f"{nickname}: {input("")}"
        client.send(message.encode("UTF-8"))


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
