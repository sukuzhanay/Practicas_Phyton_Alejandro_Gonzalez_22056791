{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d5c2be78-4fa1-4604-b347-6bd224514536",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyrebase as py\n",
    "import threading\n",
    "import sys\n",
    "import socket\n",
    "import pickle\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cbd2b098-39e8-4568-a85f-734775f1c947",
   "metadata": {},
   "outputs": [],
   "source": [
    "firebaseConfig = {\n",
    "  \"apiKey\": \"AIzaSyAfMJEIxKfVX_eKTrIoVdXg09QY9USMlzc\",\n",
    "  \"authDomain\": \"functions-real-case-pbi.firebaseapp.com\",\n",
    "  \"databaseURL\": \"https://functions-real-case-pbi-default-rtdb.firebaseio.com\",\n",
    "  \"projectId\": \"functions-real-case-pbi\",\n",
    "  \"storageBucket\": \"functions-real-case-pbi.appspot.com\",\n",
    "  \"messagingSenderId\": \"212033978800\",\n",
    "  \"appId\": \"1:212033978800:web:e1d63004db5d6c6fe89675\",\n",
    "  \"measurementId\": \"G-N23MB60FQV\"\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e334da43-ea51-4fd5-a62d-d20f2147526f",
   "metadata": {},
   "outputs": [],
   "source": [
    "firebase = py.initialize_app(firebaseConfig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a6f347da-e628-458f-b343-5b50a67ddc0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "sign_up_in=firebase.auth()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "43b655de-2282-4cdd-a768-c4009d31402a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Dame mail 22056791@gmail.com\n"
     ]
    }
   ],
   "source": [
    "mail = input(\"Dame mail\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "23d031ec-cc6d-41f6-bdbf-393b1ddf4ccb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Dame contraseña 315rf1eqh89h3\n"
     ]
    }
   ],
   "source": [
    "passw = input(\"Dame contraseña\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "97761f7c-019c-4c80-8dbf-f906af2b9961",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Su mail es: 22056791@gmail.com y su contraseña es : 315rf1eqh89h3\n"
     ]
    }
   ],
   "source": [
    "print(f'Su mail es: {mail} y su contraseña es : {passw}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "128d6c9d-367c-4753-b0ae-104a012fab96",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "user=sign_up_in.create_user_with_email_and_password(mail,passw)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "4c627e02-86a1-45ed-acc9-6e102bc250a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'kind': 'identitytoolkit#GetOobConfirmationCodeResponse',\n",
       " 'email': '22056791@gmail.com'}"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sign_up_in.send_email_verification(user['idToken'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "2a0ecd31-d1c4-48fa-afcd-357cccd3b7bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "ddbb = firebase.database()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0862627a-f67d-4bc0-ac33-9456ebad1cfc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'email': '22056791@gmail.com',\n",
       " 'expiresIn': '3600',\n",
       " 'idToken': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjJlMzZhMWNiZDBiMjE2NjYxOTViZGIxZGZhMDFiNGNkYjAwNzg3OWQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vZnVuY3Rpb25zLXJlYWwtY2FzZS1wYmkiLCJhdWQiOiJmdW5jdGlvbnMtcmVhbC1jYXNlLXBiaSIsImF1dGhfdGltZSI6MTYzNzk0MjQwOSwidXNlcl9pZCI6InVHUU02SmJKV21kVk9XejE5RnJjUm8xUEVvSDMiLCJzdWIiOiJ1R1FNNkpiSldtZFZPV3oxOUZyY1JvMVBFb0gzIiwiaWF0IjoxNjM3OTQyNDA5LCJleHAiOjE2Mzc5NDYwMDksImVtYWlsIjoiMjIwNTY3OTFAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIjIyMDU2NzkxQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.Kk-LCq16wfjYHmbSmPXlz1Vf2Vfbic08JLsu93CtZ-dPLn9MlDdZbMGY-jq_aBXcvcjx7kzTjQI4g_iouomm9-m0BrUGh4Hf0EU-uvgxQ4lvK_a3O9s-aGiGcVIS2ifJLGtIf3xbGbRPwQPvQcU10YMCTXZMW4pv5m3KEjDl3C61rTc_spFTbaQM_ujFUViTyNmkBs2xJQwtq_Yo5LlblBOUcs5iaGWjKfHtqtpeifnfXW4e6huUhsnckG-LQljDDUJ0wuQdzVJFHjGTd0FGDIC3b5vpq90mDmDBg1Q5HP7XLwz8TPHeZHMdP-sdmxT0Rtj9BVBDT9fi4v1lUfy1Mg',\n",
       " 'kind': 'identitytoolkit#SignupNewUserResponse',\n",
       " 'localId': 'uGQM6JbJWmdVOWz19FrcRo1PEoH3',\n",
       " 'refreshToken': 'AFxQ4_qHNnQ68Fop2X-YFRgvUZcBrGr0npYIs5zkkCzFiqeByVQ-PzMNK_1bx7o3trRp5fJmEq5h1SHBSsi1BUHPNJMxfjSnFx8WVhy0YKI4WNvEQY3L05AWr7mMNW1h277bXspvW5ucoGeYM7DlbA6bSnUd0pRoZH9a_RG9jJGSJRbDt46vdMNYUwTZB5gNKGD9tBW5Ali7HePBuuSDZa58XRqK6MlHilt6XKSlQ0KDhaG2MW_abSQ'}"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ddbb.child('pcd/credenciales/22056791/user').set(user)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "23b16668-2c8f-48d2-be29-8aeaa0abe50b",
   "metadata": {},
   "outputs": [],
   "source": [
    "storage=firebase.storage()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "39e58fa6-fd18-41a6-a88d-c52a96157f95",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'name': 'classparticipation/22056791/22056791.ipynb',\n",
       " 'bucket': 'functions-real-case-pbi.appspot.com',\n",
       " 'generation': '1637942419558679',\n",
       " 'metageneration': '1',\n",
       " 'timeCreated': '2021-11-26T16:00:19.670Z',\n",
       " 'updated': '2021-11-26T16:00:19.670Z',\n",
       " 'storageClass': 'STANDARD',\n",
       " 'size': '20898',\n",
       " 'md5Hash': 'lcnO+mBPLpx2f78LhhftdA==',\n",
       " 'contentEncoding': 'identity',\n",
       " 'contentDisposition': \"inline; filename*=utf-8''22056791.ipynb\",\n",
       " 'crc32c': '7lWYSg==',\n",
       " 'etag': 'CJei0oCztvQCEAE=',\n",
       " 'downloadTokens': '438d234f-f078-4735-93aa-8ad12a875f77'}"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "storage.child('classparticipation/22056791/22056791.ipynb').put('22056791.ipynb')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a8f3730-5f6a-48cd-afc1-c072fa1f02a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hilo: MainThread\n",
      "Proceso PID: 26332\n",
      "Daemon: False\n",
      "\n",
      "Hilos totales: 6\n",
      "Hilo: Thread-6\n",
      "Proceso PID: 26332\n",
      "Daemon: True\n",
      "\n",
      "Hilos totales: 6\n",
      "Hilo: Thread-7\n",
      "Proceso PID: 26332\n",
      "Daemon: True\n",
      "\n",
      "Hilos totales: 6\n",
      "Hilo: Thread-5\n",
      "Proceso PID: 26332\n",
      "Daemon: True\n",
      "\n",
      "Hilos totales: 6\n",
      "Hilo: IPythonHistorySavingThread\n",
      "Proceso PID: 26332\n",
      "Daemon: True\n",
      "\n",
      "Hilos totales: 6\n",
      "Hilo: Thread-4\n",
      "Proceso PID: 26332\n",
      "Daemon: True\n",
      "\n",
      "Hilos totales: 6\n",
      "Hilo: Thread-8\n",
      "Proceso PID: 26332\n",
      "Daemon: True\n",
      "\n",
      "Hilos totales: 6\n",
      "Ha aparecido 22056791 en la sala de chat\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      ">>\n",
      " Holaa\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "22056791@gmail.com: Holaa\n",
      "22056791: EDDDD\n"
     ]
    }
   ],
   "source": [
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
    "\t\tself.enviar(\"Ha aparecido 22056791 en la sala de chat\")\n",
    "\t\twhile True:\n",
    "\t\t\t# msg = input('\\nEscriba texto ? ** Enviar = ENTER ** Abandonar Chat = Q \\n')\n",
    "\t\t\tmsg = username_ + \": \" + input(\"\\n>>\\n\")\n",
    "\t\t\tddbb.child(\"repasoParcial/22056791/22056790\").push(msg)\n",
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
   "id": "f7eb79cb-32ee-4038-9e60-58fda7012d2d",
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
