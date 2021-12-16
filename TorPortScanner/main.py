import threading
import queue
import socket

MAX_NUMBER_PORTS = 65535
ip = input("ip : ")
my_queue = queue.Queue()

for i in range(1, MAX_NUMBER_PORTS):
    my_queue.put(i)

def scan():
    while not my_queue.empty():
        port = my_queue.get();
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socks:
            try:
                socks.connect((ip, port))
                print(f'port {port} is open!')
            except:
                print(f"Deu ruim {port}")

        my_queue.task_done()

for i in range(30):
    my_threads = threading.Thread(target=scan, daemon=True)
    my_threads.start()

my_queue.join()
print('Finished!')