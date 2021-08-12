import socket
import sys
import argparse

from datetime import datetime

thisdict = {
  21: "FTP",
  22: "SSH",
  23: "TELNET",
  25: "SMTP",
  53: "DNS",
  80: "HTTP",
  110: "POP3",
  115: "SFTP",
  135: "RPC",
  139: "NetBIOS",
  143: "IMAP",
  194: "IRC",
  443: "SSL",
  445: "SMB",
  3306: "MySQL",
  3389: "Remote Desktop",
  5632: "PCAnywhere",
  5900: "VNC",
  6112: "Warcraft III"
}

parser = argparse.ArgumentParser()

parser.add_argument('-t', '--target', help='ip', dest='target', required=True)
parser.add_argument('-s', '--speed', help='speed', dest='speed', const=1, nargs='?')
parser.add_argument('-p', '--port', help='use 50,100', dest='commen')

min = 50
max = 85

# nargs 0 veya 1
# const 0 argüman olduğunda varsayılanı ayarlar
# type=int  argümanı int'e dönüştürür

args = parser.parse_args()

target = args.target
speed = args.speed
commen = args.commen

print("-" * 50)
print("Scanning target " + target)
print("Time started : " + str(datetime.now()))
print("-" * 50)

timeout = 1 if speed is None else 0.5


def speedCheck():
    if speed != 1:
        if speed is not None:
            print("[-]No value entered -s")
            sys.exit()
def portNameCheck():
    for f in range(min, max):
        for x in thisdict:
            if f == x:
                print(thisdict[f])


try:
    if commen is not None:
        spl = commen.split(",")
        min = int(spl[0])
        max = int(spl[1])

    for port in range(min, max):

        speedCheck()
        portNameCheck()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(timeout)
        result = s.connect_ex((target, port))
        print("Checking port {}".format(port))
        if result == 0:

            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname cloud not be resolve")
    sys.exit()

except socket.error:
    print("Couldn't connect to server. ")
    sys.exit()
