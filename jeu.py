import socket
import sys
import json
from random import randint
import random

playlength = 800 #nombre de mouvements maximum dans une partie (moyenne playlength/2)
maxscore = 1000 #score maximal atteignable
movesamount=12	#nombre de mouvements possibles

def generate_moves():
	score=random.randint(0,maxscore)

	random.seed(score) #le reste de la partie dépends du score

	length = random.randint(0,playlength)*score

	moves = []
	for i in range(length):
		moves.append(randint(0,movesamount))

	playsession = score, moves

	return playsession

def send_moves(score, moves):
	socket = connect_to_server()
	send_to_server(score,moves,socket)

def send_to_server(score,moves,sock):

	try:

		message = json.dumps([score]+moves).encode("utf-8")
		#print('sending: "%s"' % message)
		sizestring = str(len(message)).zfill(10).encode("utf-8")
		print("Sending size",sizestring,"lenth",len(sizestring))
		sock.sendall(sizestring)
		sock.sendall(message)
		print("Sent message")
		sock.sendall(("0"*2000).encode("utf-8"))
		print("Sent extra")
		"""amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			data = sock.recv(16)
			amount_received += len(data)
			print('received "%s"' % data)"""
		answer=sock.recv(64).decode("utf-8")
		#answer = json.loads(data)
		print(answer)

	finally:
		sock.close()

def connect_to_server():# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect the socket to the port on the server given by the caller
	server_address = (sys.argv[1], 10000)
	print('connecting to %s port %s' % server_address)
	sock.connect(server_address)
	return sock

def main():
	playsession = generate_moves()
	send_moves(*playsession)

if __name__ == "__main__":
	main()
