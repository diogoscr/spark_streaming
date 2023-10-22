import socket
import time

HOST = 'localhost'
PORT = 3000

s = socket.socket()
s.bind((HOST, PORT))
print(f'Aguardando conexão na porta: {PORT}')

s.listen(5)
conn, address = s.accept()

print(f'Recebendo solicitação de {address}')

messages = [
    'message a',
    'message b',
    'message c',
    'message d',
    'message e',
    'message f',
    'estou animado com o curso'
]

for message in messages:
    message = bytes(message, 'utf-8')
    conn.send(message)
    time.sleep(4)

conn.close()