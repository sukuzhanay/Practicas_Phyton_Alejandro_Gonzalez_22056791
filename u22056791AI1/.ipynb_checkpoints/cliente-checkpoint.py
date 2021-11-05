import threading
import sys
import socket
import pickle
import os

class Cliente():
	puerto_ = input('Escriba el puerto')
    ip123_ = input('Escriba la dirección ip')
	def __init__(self, host=ip123_, port=puerto_):
		self.sock = socket.socket()
		username_ = input('Escriba el nombre de usuario que desea tener')
		self.sock.connect((str(host), int(port)))
		hilo_recv_mensaje = threading.Thread(target=self.recibir)
		hilo_recv_mensaje.daemon = True
		hilo_recv_mensaje.start()


		
		for thread in threading.enumerate():
			print("Hilo: " + thread.name + "\n" + "Proceso PID: "+ str(os.getpid()) + "\n" + "Daemon: " + str(thread.daemon) +  "\n")
		print("Hilos totales: " + str(threading.activeCount()-1))

		self.enviar("<" + username_ + "> se ha conectado")
		while True:
			# msg = input('\nEscriba texto ? ** Enviar = ENTER ** Abandonar Chat = Q \n')
			msg = input("\n>>\n")
			if msg != 'Q' :
				self.enviar(username + ": " + msg)
			else:
				print(" ****LOGOUT****")
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