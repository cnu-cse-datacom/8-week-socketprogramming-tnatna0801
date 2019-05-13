import socket
import os

FLAGS = None

class ClientSocket():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def socket_send(self):
        file_name = input("Input your file name : ")
        file_size = os.path.getsize(file_name)
        file_size = str(file_size)

        self.socket.sendto(file_name.encode(), (FLAGS.ip, FLAGS.port))
        self.socket.sendto(file_size.encode(), (FLAGS.ip, FLAGS.port))

        file_size = int(file_size)

        f = open(file_name, 'rb')

        print("File Transimit Start......")
        
        current_size = 0
        while current_size < file_size:

            data = f.read(1024)
            self.socket.sendto(data, (FLAGS.ip, FLAGS.port))
            current_size = min(current_size+1024, file_size)

            print("current_size / total_size = ",current_size,"/",file_size,", ", current_size/file_size*100,"%")

        data2, addr = self.socket.recvfrom(2000)
        print(data2.decode())
        data2, addr = self.socket.recvfrom(2000)
        print(data2.decode())
        f.close()
        self.socket.close()

    def main(self):
        self.socket_send()

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', type=str, default = 'localhost')
    parser.add_argument('-p', '--port', type=int, default = '9100')
    FLAGS, _ = parser.parse_known_args()
    
    client_socket = ClientSocket()
    client_socket.main()



