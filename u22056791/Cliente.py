import threading
import sys
import socket
import pickle
import os

class Cliente():
	def __init__(self, host= input("Escriba la dirección ip: "), port= input("Escriba el puerto: ")):
		self.sock = socket.socket()
		username_ = input('Escriba el nombre de usuario que desea tener: ')
		self.sock.connect((str(host), int(port)))
		hilo_recv_mensaje = threading.Thread(target=self.recibir)
		hilo_recv_mensaje.daemon = True
		hilo_recv_mensaje.start()
		
		for thread in threading.enumerate():
			print("Hilo: " + thread.name + "\n" + "Proceso PID: "+ str(os.getpid()) + "\n" + "Daemon: " + str(thread.daemon) +  "\n")
			print("Hilos totales: " + str(threading.activeCount()-1))

		self.enviar("Ha aparecido " + username_ + "en la sala de chat")
		while True:
			# msg = input('\nEscriba texto ? ** Enviar = ENTER ** Abandonar Chat = Q \n')
			msg = input("\n>>\n")
			if msg != 'Q' :
				self.enviar(username_ + ": " + msg)
			else:
				print(" **** Ha abandonado el chat ****" + username_)
				self.sock.close()
				sys.exit()

	def recibir(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def enviar(self, msg):
		self.sock.send(pickle.dumps(msg))
		data = pickle.dumps(msg)
		if data: 
			print(pickle.loads(data))

c = Cliente()