import socket
alamat = ('localhost', 12345)
recv = 1024

def main():
    message = input('masukkan pesan: ')
    while message == 'connme':
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (alamat)
        client_socket.connect(server_address)
        loopMessage(client_socket)

def loopMessage(client_socket):
    while True:
        data = client_socket.recv(recv)
        print(f'{data.decode()}')
        message = input('Masukkan Pesan: ')
        client_socket.sendall(message.encode())
        if message == 'byebye':
            client_socket.close()
            break
        elif message == 'ls':
            ls = client_socket.recv(recv)
            print(ls)
        perintah = message.split()
        if len(perintah) == 2 :
            menu, file = perintah
            if menu == 'download':
                download(client_socket)
            elif menu == 'upload':
                upload(client_socket)
            elif menu == 'size':
                size(client_socket)
            elif message == 'rm':
                rm(client_socket)

def download(client_socket):
    pesan = client_socket.recv(recv)
    print(pesan.decode())

def upload(client_socket):
    pesan = client_socket.recv(recv)
    print(pesan.decode())

def size(client_socket):
    pesan = client_socket.recv(recv)
    print(pesan.decode())

def rm(client_socket):
    pesan = client_socket.recv(recv)
    print(pesan.decode())
if __name__ == '__main__':
    main()
