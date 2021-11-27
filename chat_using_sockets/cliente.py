import threading
import sys
import socket
import pickle
import os

firebaseConfig = {
  "apiKey": "AIzaSyAfMJEIxKfVX_eKTrIoVdXg09QY9USMlzc",
  "authDomain": "functions-real-case-pbi.firebaseapp.com",
  "databaseURL": "https://functions-real-case-pbi-default-rtdb.firebaseio.com",
  "projectId": "functions-real-case-pbi",
  "storageBucket": "functions-real-case-pbi.appspot.com",
  "messagingSenderId": "212033978800",
  "appId": "1:212033978800:web:e1d63004db5d6c6fe89675",
  "measurementId": "G-N23MB60FQV"
}
firebase = py.initialize_app(firebaseConfig)
ddbb = firebase.database()
sign_up_in=firebase.auth()
sign_up_in.send_email_verification(user['idToken'])

class Cliente():

	def __init__(self, host=socket.gethostname(), port=59989):
		self.sock = socket.socket()
		username_ = "22056791"
		self.sock.connect((str(host), int(port)))
		hilo_recv_mensaje = threading.Thread(target=self.recibir)
		hilo_recv_mensaje.daemon = True
		hilo_recv_mensaje.start()
		
		for thread in threading.enumerate():
			print("Hilo: " + thread.name + "\n" + "Proceso PID: "+ str(os.getpid()) + "\n" + "Daemon: " + str(thread.daemon) +  "\n")
			print("Hilos totales: " + str(threading.activeCount()-1))

		self.enviar("Ha aparecido 22056791 en la sala de chat")
		while True:
			# msg = input('\nEscriba texto ? ** Enviar = ENTER ** Abandonar Chat = Q \n')
			msg = username_ + ": " + input("\n>>\n")
			ddbb.child("repasoParcial/22056791/22056790").push(msg)
			if msg != 'Q' :
				self.enviar(msg)
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

