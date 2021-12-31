# author : gamingdy
import socket
import time
import sys


ip = input("Enter target ip address: ")


def scan(address, port_range=None):
def ask_range():
    while True:
        port_range = input("Do you want to specify port range ? y/n").lower()
        if port_range == "y":
            range_port = input("Enter your range: start-end : ").split("-")
            start_port = int(range_port[0])
            end_port = int(range_port[1])
            return range(start_port, end_port + 1)
        elif port_range == "n":
            return None


def scan(address, _range=None):
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

    scan_port = _range if _range else common_port
    for port in scan_port:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
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
range_port = ask_range()
print("-" * 30)
print("Scanning remote host...")
print("-" * 30)
scan(ip, range_port)
total_time = time.time() - start_time
print("Elapsed time: " + str(total_time))
