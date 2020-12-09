import socket

try:
  fSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  fSocket.connect(('data.pr4e.org', 80))
  cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
  fSocket.send(cmd)

  while True:
    data = fSocket.recv(512)
    if len(data) < 1:
      break

    print(data.decode(), end='')
  fSocket.close()
except:
  print('Error')