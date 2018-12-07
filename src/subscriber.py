import paho.mqtt.client as mqtt
import time, sys
import logging

logging.basicConfig(level=logging.INFO)

def on_log(client, userdata, level, buf):
    print("  log: "+buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True
        print("Conectado com sucesso")
    else:
        print("Não conectado. Código: ", rc)

def on_disconnect(client, userdata, flags, rc=0):
    client.connected_flag=False
    print("Desconectado. Código:"+str(rc))

def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    print("Mensagem recebida: \t", topic, "\tmsg: \t",  m_decode)

# Define broker
#broker = "127.0.0.1"
broker = input("Endereço do broker: ")
client_name = input("Nome do subscriber: ")

topics = []
end = "sim"

while not (end == "n" or end == "no"):
    topico = input("Nome do topico: ")
    publisher = input("Nome do publisher: ")
    topics = topics + [(topico+"/"+publisher,0)]
    end = input("Adicionar mais subscribes? (s/n): ")
    print(end)


# Cria nova instância
client = mqtt.Client(client_name)
client.connected_flag=False

# Callbacks
client.on_connect = on_connect
client.on_disconnect = on_disconnect
#client.on_log = on_log
client.on_message = on_message

# Topics (são representados por tuplas)
#topics = [("house/sensor1", 0), ("house/sensor2", 0)]
topic_ack=[]

# Rotina de conexão
print("Conectando ao broker: ", broker)
try:
    client.connect(broker)
except:
    print("Problema na conexão")    
    sys.exit(1)

# Inicia loop
client.loop_start()

# Subscribe
print("Subscribe: " + str(topics) + "\n")
for t in topics:
    try:
        r = client.subscribe(t)
        if r[0] == 0:
            logging.info("Subscribed: " + str(t[0]) + " Código: " + str(r))
            topic_ack.append([t[0], r[1], 0])
        else:
            logging.info("Erro: " + str(r))
            client.loop_stop()
            sys.exit(1)
    except Exception as e:
        logging.info("Erro" + str(e))
        client.loop_stop()
        sys.exit(1)

while(1):
    while not client.connected_flag:
        print ("Aguardando loop")
        time.sleep(1)

    
    # Timer
    #print("Timer... ")
    time.sleep(4)

# Encerra loop
client.loop_stop()

# Desconecta do broker
client.disconnect()
