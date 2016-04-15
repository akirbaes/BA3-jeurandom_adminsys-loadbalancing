import socket
import sys
from random import randint
import random
import json

movesamount=12	#nombre de mouvements possibles
playlength = 800 #nombre de mouvements maximum dans une partie (moyenne playlength/2)
maxscore = 1000 #score maximal atteignable


def verify_data(score, moves):
	random.seed(score) #le reste de la partie dépends du score
	
	locallength = random.randint(0,playlength)*score
	
	try:
		for i in range(locallength):
			if(moves[i] != randint(0,movesamount)):
				print("Mouvement ",i,"non conforme")
				return False
	except Exception as e:
		print(e)
		return False
	
	return True
	
def setup_server():

	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the address given on the command line
	if(len(sys.argv)>=2):
		server_name = sys.argv[1]
	else:
		server_name="localhost"
	server_address = (server_name, 10000)
	print('starting up on %s port %s' % server_address)
	sock.bind(server_address)
	sock.listen(1)
	return sock

def server_loop(sock):
	while True:
		print('waiting for a connection')
		connection, client_address = sock.accept()
		try:
			print('client connected:', client_address)
			message = "".encode("utf-8")
			counter=0
			size = int(connection.recv(10).decode("utf-8"))
			print("Will receive message of size ",size)
			
			while len(message)<size:
				data = connection.recv(min(4096,size-len(message))) #bizarrement ça marche avec 4096
				#if not(counter%100):
				#print('received "%s"' % data,"\b")
				counter+=1
				#print(counter)
				if data:
					"""connection.sendall(data)"""
					message+=data
				else:
					print("Break no data")
					break
			print("Received messages of length",len(message))
			message = message.decode("utf-8")
			#print(message)
			list = json.loads(message)
			#print(list)
			print("Parsed into list of length",len(list))
			print("Verifying data\b")
			answer=(verify_data(list.pop(0),list) and "Test réussit" or "Test échec").encode("utf-8")
			print(answer.decode("utf-8"))
			
			print("Sending answer\b")
			connection.sendall(answer)
		except KeyboardInterrupt:
			exit()
		except ConnectionResetError as e:
			
			print("Connection reset! Continue...")
		finally:
			connection.close()

def main():
	s=setup_server()
	server_loop(s)
			
if __name__=="__main__":
	main()