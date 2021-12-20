import threading
import queue
import socket
#import socks

MAX_NUMBER_PORTS = 1000 # 65535
NUMBER_THREADS = 30

LOOPBACK_INTERFACE_IP = '127.0.0.1'
TOR_PORT = 9050


ip = input("ip : ")
my_queue = queue.Queue()
#socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, LOOPBACK_INTERFACE_IP, TOR_PORT)
#socket.socket = socks.socksocket

for i in range(1, MAX_NUMBER_PORTS):
    my_queue.put(i)

def scan():
    while not my_queue.empty():
        port = my_queue.get();
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sockets:
            try:
                sockets.connect((ip, port))
                print(f'port {port} is open!')
            except:
                # print(f"deu ruim {port}")
                pass

        my_queue.task_done()

for i in range(NUMBER_THREADS):
    my_threads = threading.Thread(target=scan, daemon=True)
    my_threads.start()

my_queue.join()
print('Finished!')