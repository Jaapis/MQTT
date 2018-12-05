import paho.mqtt.client as mqtt
import time

from random import randrange

def on_log(client, userdata, level, buf):
    print("  log: "+buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Conectado com sucesso")
    else:
        print("Não conectado. Código: ", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print("Desconectado. Código:"+str(rc))

def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    print("Mensagem recebida:\n", m_decode)

# Define broker
broker = "127.0.0.1"

publisher = input("Nome do publisher: ")


# Cria nova instância
client = mqtt.Client(publisher)

# Callbacks
client.on_connect = on_connect
client.on_disconnect = on_disconnect
#client.on_log = on_log
client.on_message = on_message

# Conecta ao broker
print("Conectando ao broker: ", broker)
client.connect(broker)

# Subscribe (publisher não precisa subscrever nada)
#client.subscribe("house/sensor1")

# Publish
while(1):
    client.loop_start()

    msg = str(randrange(0,9))
    topic = "house/" + publisher
    print("Publicando em: ", topic, " msg: ", msg )
    client.publish(topic, msg)

    # Timer
    #print("Timer... ")
    time.sleep(4)
    client.loop_stop()



# Desconecta do broker
client.disconnect()
