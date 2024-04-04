# Pemrograman Jaringan Week 6
## Tugas 2 Pemrograman FTP on Python

ini adalah server.py
```python
import socket
import os

alamat = ('localhost', 12345)
recv = 1024

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = alamat
    server_socket.bind(server_address)
    server_socket.listen(1)
    print('Waiting for a connection...')
    client_socket, client_address = server_socket.accept()
    print(f'Connected by {client_address}')
    loopMessage(client_socket)

def loopMessage(client_socket):
    menu = '| ls        | \n| rm        | \n| download  | \n| upload    | \n| size      | \n| byebye    |'
    client_socket.sendall(menu.encode())
    while True:
        message = client_socket.recv(recv).decode()
        if message == 'byebye':
            break
        else:
            process_message(client_socket, message)

def process_message(client_socket, message):
    print(f"Received: {message}")
    response = "Apakah ada yang bisa dibantu? "
    client_socket.sendall(response.encode())
    perintah = message.split()
    if len(perintah) == 2 :
        menu, file = perintah
        print(menu)
        print(file)
        if menu == 'download':
            download(client_socket, file)
        elif menu == 'upload':
            upload(client_socket, file)
        elif menu == 'size':
            size(client_socket, file)
        elif message == 'rm':
            rm(client_socket, file)
    else:
        if message == 'ls':
            ls(client_socket)
        elif message == 'byebye':
            client_socket.close()

def ls(client_socket):
    path = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//server"
    dirList = os.listdir(path)
    print(dirList)
    client_socket.sendall(str(dirList).encode())

def download(client_socket, file):
    server_dir = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//server"
    client_dir = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//client"
    
    server_file_path = os.path.join(server_dir, file)
    
    client_file_path = os.path.join(client_dir, file)
    
    if os.path.exists(server_file_path):
        with open(server_file_path, 'rb') as server_file:
            file_content = server_file.read()
            
            with open(client_file_path, 'wb') as client_file:
                client_file.write(file_content)
        pesan = 'file berhasil didownload'
        client_socket.sendall(pesan.encode())

def upload(client_socket ,file):
    server_dir = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//server"
    client_dir = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//client"

    server_file_path = os.path.join(server_dir, file)
    client_file_path = os.path.join(client_dir, file)

    if os.path.exists(client_file_path):
        with open(client_file_path, 'rb') as client_file:
            file_content = client_file.read()

            with open(server_file_path, 'wb') as server_file:
                server_file.write(file_content)
            pesan = 'file berhasil diupload'
            client_socket.sendall(pesan.encode())

def size(client_socket, file):
    server_path = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//server"
    serverFile = os.path.join(server_path, file)
    
    if os.path.exists(serverFile):
        file_size_bytes = os.path.getsize(serverFile)
        file_size_kb = file_size_bytes / 1024
        size_message = f"Ukuran file {file}: {file_size_kb:.2f} kB"
        client_socket.sendall(size_message.encode())
    else:
        not_found_message = 'File tidak ditemukan'
        client_socket.sendall(not_found_message.encode())

def rm(client_socket, file):
    server_path = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//server"
    serverFile = os.path.join(server_path, file)
    
    if os.path.exists(serverFile):
        os.remove(serverFile)
        pesan = 'file berhasil dihapus'
        client_socket.sendall(pesan.encode())
    else:
        pesan = 'file tidak ditemukan'
        client_socket.sendall(pesan.encode())

if __name__ == '__main__':
    main()
```
Terdapat 8 fungsi utama yang akan dijalankan oleh program python :
# 1 . Fungsi Main()
```python
def main():
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = alamat
server_socket.bind(server_address)
server_socket.listen(1)
print('Waiting for a connection...')
client_socket, client_address = server_socket.accept()
print(f'Connected by {client_address}')
loopMessage(client_socket
```
kode di atas digunakan untuk membangun koneksi ke klien menggunakan protokol TCP. Setelah terkoneksi, maka akan di arahkan ke fungsi LoopMessage

# 2. Fungsi Loop Message
```python
def loopMessage(client_socket):
menu = '| ls        | \n| rm        | \n| download  | \n| upload    | \n| size      | \n| byebye    |'
client_socket.sendall(menu.encode())
while True:
    message = client_socket.recv(recv).decode()
    if message == 'byebye':
        break
    else:
        process_message(client_socket, message)
```
Fungsi di atas akan menerima parameter client_socket yang nantinya digunakan untuk mengirimkan pesan kepada client saat fungsi LoopMessage() dijalankan, maka akan mengirimkan pesan berupa menu layanan yang tersedia di server 

# 3. Fungsi Process_message()
```python
def process_message(client_socket, message):
print(f"Received: {message}")
response = "Apakah ada yang bisa dibantu? "
client_socket.sendall(response.encode())
perintah = message.split()
if len(perintah) == 2 :
    menu, file = perintah
    print(menu)
    print(file)
    if menu == 'download':
        download(client_socket, file)
    elif menu == 'upload':
        upload(client_socket, file)
    elif menu == 'size':
        size(client_socket, file)
    elif message == 'rm':
        rm(client_socket, file)
else:
    if message == 'ls':
        ls(client_socket)
    elif message == 'byebye':
        client_socket.close()
```
Fungsi process_message() menerima pesan dari klien, memproses dan memberikan respon. Jika pesan terdiri dari dua kata dipisahkan menjadi perintah dan nama file. Jika perintah adalah 'download', 'upload', 'size', atau 'rm' fungsi akan memanggil fungsi yang telah ditentukan. Jika hanya satu kata dan itu adalah 'ls' atau 'byebye' fungsi akan memanggil fungsi yang ditentukan. Jika perintah tidak dikenali, maka perintah tidak akan dieksekusi

# 4. Fungsi ls()
```python
def ls(client_socket):
    path = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//server"
    dirList = os.listdir(path)
    print(dirList)
    client_socket.sendall(str(dirList).encode())
```
Fungsi ls() digunakan untuk mendapatkan daftar file dan direktori dalam suatu direktori pada server. Fungsi ini mengambil path dan direktori yang ingin di-list, kemudian menggunakan fungsi os.listdir() untuk mendapatkan daftar file dan direktori dalam path tersebut. Setelah itu, daftar tersebut dikirim kembali ke klien sebagai respon menggunakan soket klien dengan metode sendall(), setelah diubah menjadi string dan diencode terlebih dahulu.

# 5. Fungsi Download()
```python
def download(client_socket, file):
    server_dir = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//server"
    client_dir = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//client"

    server_file_path = os.path.join(server_dir, file)

    client_file_path = os.path.join(client_dir, file)

    if os.path.exists(server_file_path):
        with open(server_file_path, 'rb') as server_file:
            file_content = server_file.read()
        
            with open(client_file_path, 'wb') as client_file:
                client_file.write(file_content)
        pesan = 'file berhasil didownload'
        client_socket.sendall(pesan.encode())
```
Fungsi download() digunakan untuk mengunduh file dari server ke client. Pertama, fungsi ini mengambil path lengkap dari file yang ingin diunduh di server dan path lengkap tempat penyimpanan di client. Kemudian, fungsi mengecek apakah file tersebut ada di server menggunakan os.path.exists().

# 6. Fungsi Upload
```python
def upload(client_socket ,file):
    server_dir = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//server"
    client_dir = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//client"

    server_file_path = os.path.join(server_dir, file)
    client_file_path = os.path.join(client_dir, file)

    if os.path.exists(client_file_path):
        with open(client_file_path, 'rb') as client_file:
            file_content = client_file.read()

            with open(server_file_path, 'wb') as server_file:
                server_file.write(file_content)
            pesan = 'file berhasil diupload'
            client_socket.sendall(pesan.encode())
```
Fungsi upload merupakan kebalikan dari fungsi download(). Fungsi ini digunakan untuk mengunggah file dari client ke server. Pertama, fungsi ini mengambil path lengkap dari file yang ingin diunggah di client dan path lengkap tempat penyimpanan di server.

# 7. Fungsi size()
```python
def size(client_socket, file):
    server_path = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//server"
    serverFile = os.path.join(server_path, file)

    if os.path.exists(serverFile):
        file_size_bytes = os.path.getsize(serverFile)
        file_size_kb = file_size_bytes / 1024
        size_message = f"Ukuran file {file}: {file_size_kb:.2f} kB"
        client_socket.sendall(size_message.encode())
    else:
        not_found_message = 'File tidak ditemukan'
        client_socket.sendall(not_found_message.encode())
```
Fungsisize() digunakan untuk mengirimkan ukuran file dari server ke klien. fungsi ini mengambil path lengkap dari file yang akan dicek ukurannya di server. Kemudian, menggunakan os.path.exists(), fungsi memeriksa apakah file tersebut ada di server.

# 8. Fungsi rm()
```python
def rm(client_socket, file):
    server_path = "G://Riwayat Kuliah//Semester 4//Pr. Pemrograman Jaringan//Week 6//server"
    serverFile = os.path.join(server_path, file)

    if os.path.exists(serverFile):
        os.remove(serverFile)
        pesan = 'file berhasil dihapus'
        client_socket.sendall(pesan.encode())
    else:
        pesan = 'file tidak ditemukan'
        client_socket.sendall(pesan.encode())
```
Fungsi rm() digunakan untuk menghapus file dari server. Pertama, fungsi ini membentuk path lengkap dari file yang akan dihapus di server. Kemudian, menggunakan os.path.exists(), fungsi memeriksa apakah file tersebut ada di server.

## PENJELASAN KODE CLIENT
```python
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

```
# 1. Fungsi Main()
```python
def main():
message = input('masukkan pesan: ')
while message == 'connme':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (alamat)
    client_socket.connect(server_address)
    loopMessage(client_socket)
```



