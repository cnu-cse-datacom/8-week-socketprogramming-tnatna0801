import socket
import os
FLAGS = None

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', type=str, default = 'localhost')
parser.add_argument('-p', '--post', type=int, default = '9100')
FLAGS, _ = parser.parse_known_args()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((FLAGS.ip, FLAGS.post))

filename, addr = server_socket.recvfrom(1024)
size, addr = server_socket.recvfrom(1024)
file_size = int(size.decode())
#file_size = size.decode()

print("file recv start from", addr[0])
print("FILE NAME : ", filename.decode()) #decode()
print("FILE SIZE : ", file_size) #decode()

f = open(filename.decode(), 'wb')

current_size = 0

while current_size < file_size:

    data, addr = server_socket.recvfrom(1024)
    current_size = min(current_size + 1024, file_size)
    f.write(data)

    print("current_size / total_size = ", current_size, "/", file_size, ", ", (current_size/file_size) * 100, "%",)
    #print("\n")

f.close()
print("yeah")
server_socket.sendto("ok".encode(), addr)
server_socket.sendto("file_send_end".encode(), addr)
server_socket.close()
