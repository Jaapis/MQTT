# MQTT
Trabalho de Redes de Computadores 2018 2º semestre.

Implementar uma aplicação usando protcolo MQTT.

Basicamente deve-se ler 3 sensores de tópicos diferentes e exibir os respectivos dados para os seus subscribes correspondentes.

## Definições

### MQTT 

MQTT é um protocolo de comunicação chamado de Message Queuing Telemetry Transport. É utilizado para fazer a comunicação entre máquinas. É um protocolo antigo, mas que ganhou força e está sendo bastante utilizado em soluções para IoT.

O protocolo MQTT utiliza um padrão de Publish and Subscribe, no qual haverão três conceitos fundamentais:
* Publisher
* Broker
* Subscriber

Publisher é aquele que publica algum dado, que transmite uma informação. O Broker retransmite esses dados e os retransmite para seus respectivos Subscribers. Subscribers são aqueles que possuem a assinatura de que querem receber determinado dado.


### Instalações necessárias

#### Paho

Esta é uma biblioteca em Python do protocolo MQTT.

Comando para instalá-lo:

<b>pip install paho-mqtt</b>

#### Mosquitto

Este é o programa utilizado para ser o Broker da comunicação dos nosso protocolo. Os comandos para instalá-lo no Linux são descritos abaixo:

<b>sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa</b>

<b>sudo apt-get update</b>

<b>sudo apt-get install mosquitto</b>

<b>sudo apt-get install mosquitto-clients</b>

