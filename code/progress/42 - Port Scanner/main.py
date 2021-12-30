import socket
import time
import sys


ip = input("Enter target ip address: ")


def scan(address, port_range=None):
    common_port = [
        20,
        21,
        22,
        23,
        25,
        26,
        50,
        51,
        53,
        67,
        68,
        69,
        80,
        110,
        119,
        123,
        135,
        136,
        137,
        138,
        139,
        143,
        161,
        162,
        389,
        443,
        587,
        989,
        990,
        993,
        995,
        2077,
        2078,
        2082,
        2083,
        2086,
        2087,
        2095,
        2096,
        3306,
        3389,
    ]
    hostname = socket.gethostbyname(address)

    scan_port = common_port
    for port in scan_port:
        print(port)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:

            result = server.connect_ex((hostname, port))
            if result == 0:
                print(f"Open Port | {port} ")
        except socket.gaierror:
            print("Host could not resolve")
        except KeyboardInterrupt:
            sys.exit()
        server.close()


start_time = time.time()
print("-" * 30)
print("Scanning remote host...")
print("-" * 30)
scan(ip)
