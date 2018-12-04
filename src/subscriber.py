import paho.mqtt.client as mqtt
import time

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

# Cria nova instância
client = mqtt.Client("NOME_SENSOR")

# Callbacks
client.on_connect = on_connect
client.on_disconnect = on_disconnect
#client.on_log = on_log
client.on_message = on_message

# Conecta ao broker
print("Conectando ao broker: ", broker)
client.connect(broker)
client.loop_start()

# Subscribe
client.subscribe("house/sensor1")

# Publish
client.publish("house/sensor1", "mensagem de teste")

# Timer
#print("Timer... ")
time.sleep(4)
client.loop_stop()

# Desconecta do broker
client.disconnect()
