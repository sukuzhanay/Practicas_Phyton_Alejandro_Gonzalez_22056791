{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "057072cc-83df-4f2e-8a14-152a6cc56686",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'firebaseConfig' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\ALEJX_~2\\AppData\\Local\\Temp/ipykernel_28844/3050507243.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mos\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpyrebase\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpy\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m \u001b[0mfirebase\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minitialize_app\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfirebaseConfig\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m \u001b[0msign_up_in\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mfirebase\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mauth\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[0mmail\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Dame mail\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'firebaseConfig' is not defined"
     ]
    }
   ],
   "source": [
    "import threading\n",
    "import sys\n",
    "import socket\n",
    "import pickle\n",
    "import os\n",
    "import pyrebase as py\n",
    "firebase = py.initialize_app(firebaseConfig)\n",
    "sign_up_in=firebase.auth()\n",
    "mail = input(\"Dame mail\")\n",
    "passw = input(\"Dame contraseña\")\n",
    "firebaseConfig = {\n",
    "  \"apiKey\": \"AIzaSyAfMJEIxKfVX_eKTrIoVdXg09QY9USMlzc\",\n",
    "  \"authDomain\": \"functions-real-case-pbi.firebaseapp.com\",\n",
    "  \"databaseURL\": \"https://functions-real-case-pbi-default-rtdb.firebaseio.com\",\n",
    "  \"projectId\": \"functions-real-case-pbi\",\n",
    "  \"storageBucket\": \"functions-real-case-pbi.appspot.com\",\n",
    "  \"messagingSenderId\": \"212033978800\",\n",
    "  \"appId\": \"1:212033978800:web:e1d63004db5d6c6fe89675\",\n",
    "  \"measurementId\": \"G-N23MB60FQV\"\n",
    "}\n",
    "print(f'Su mail es: {mail} y su contraseña es : {passw}')\n",
    "user=sign_up_in.create_user_with_email_and_password(mail,passw)\n",
    "sign_up_in.send_email_verification(user['idToken'])\n",
    "ddbb = firebase.database()\n",
    "ddbb.child('pcd/credenciales/22056791/user').set(user)\n",
    "storage=firebase.storage()\n",
    "storage.child('repasoParcial/22056791.ipynb').put('22056791.ipynb')\n",
    "\n",
    "\n",
    "class Cliente():\n",
    "\n",
    "\tdef __init__(self, host=socket.gethostname(), port=59989):\n",
    "\t\tself.sock = socket.socket()\n",
    "\t\tusername_ = mail\n",
    "\t\tself.sock.connect((str(host), int(port)))\n",
    "\t\thilo_recv_mensaje = threading.Thread(target=self.recibir)\n",
    "\t\thilo_recv_mensaje.daemon = True\n",
    "\t\thilo_recv_mensaje.start()\n",
    "\t\t\n",
    "\t\tfor thread in threading.enumerate():\n",
    "\t\t\tprint(\"Hilo: \" + thread.name + \"\\n\" + \"Proceso PID: \"+ str(os.getpid()) + \"\\n\" + \"Daemon: \" + str(thread.daemon) +  \"\\n\")\n",
    "\t\t\tprint(\"Hilos totales: \" + str(threading.activeCount()-1))\n",
    "\n",
    "\t\tself.enviar(\"Ha aparecido \" + username_ + \" en la sala de chat\")\n",
    "\t\twhile True:\n",
    "\t\t\t# msg = input('\\nEscriba texto ? ** Enviar = ENTER ** Abandonar Chat = Q \\n')\n",
    "\t\t\tmsg = username_ + \": \" + input(\"\\n>>\\n\")\n",
    "\t\t\tif msg != 'Q' :\n",
    "\t\t\t\tself.enviar(msg)\n",
    "\t\t\telse:\n",
    "\t\t\t\tprint(\" **** Ha abandonado el chat ****\" + username_)\n",
    "\t\t\t\tself.sock.close()\n",
    "\t\t\t\tsys.exit()\n",
    "\n",
    "\tdef recibir(self):\n",
    "\t\twhile True:\n",
    "\t\t\ttry:\n",
    "\t\t\t\tdata = self.sock.recv(1024)\n",
    "\t\t\t\tif data:\n",
    "\t\t\t\t\tprint(pickle.loads(data))\n",
    "\t\t\texcept:\n",
    "\t\t\t\tpass\n",
    "\n",
    "\tdef enviar(self, msg):\n",
    "\t\tself.sock.send(pickle.dumps(msg))\n",
    "\t\tdata = pickle.dumps(msg)\n",
    "\t\tif data: \n",
    "\t\t\tprint(pickle.loads(data))\n",
    "\n",
    "c = Cliente()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10023526-3ac4-4237-867e-a1e13640a1c7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
