# MQTT
Trabalho de Redes de Computadores 2018 2º semestre.

Equipe:  
Rodrigo Toshiaki Horie 26620 
Tiago Coli Resende 2016000103 
Tercio Naoki Sato  30697

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

### Como MQTT funciona [1]

É dividida em quatro estágios: conexão, autenticação, comunicação e término. Um cliente começa pela criação de uma conexão em TCP/IP para o Broker por meio do uso de uma porta padrão ou uma porta personalizada definida pelos operadores do Broker. Quando a conexão é estabelecida, tem a possibilidade do servidor continuar uma seção antiga se é fornecido o reúso da identidade do cliente.

A porta padrão para comunicação não encriptadas é 1883. Para comunicação encriptada (Secure Sockets Layer (SSL)/Transport Layer Security (TLS)), é 8883. Durante o "handshake" do SSL/TTL, o cliente valida o certificado do servidor para auntenticar o servidor. O cliente pode também pode fornecer um certificado do cliente para o Broker durante o "handshake", o qual o Broker pode usar para autenticar o cliente. Enquanto não é especificamente parte dos requerimentos do MQTT, tem se tornado comum para o Broker utilizar autenticação de cliente com certificados SSL/TLS da parte do cliente.

Como o protocolo MQTT visa ser um protocolo para recursos limitados e dispotivos IOT, SSL/TLS nem sempre pode ser uma opção e, em alguns casos, possivelmente não é desejado. Em tais casos, autenticação é realizada por meio do envio de usuário e senha pelo cliente ao servidor como parte da sequência do pacote CONNECT/CONNACK. Alguns brokers, especialmente publicações de brokers abertos na internet, vão aceitar clientes anônimos. Neste caso, usuário e senha são deixados em branco.

MQTT é chamado de protocolo leve (lightweight) porque todas as suas mensagens têm uma estrutura pequena de código. Cada mensagem consiste de um cabeçalho fixo de 2 bytes, um cabeçalho variável e opcional, uma mensagem payload que é limitado à 256 MB de informação e um nível de qualidade de serviço (QoS - Quality of Service).

Os três níveis de qualidade de serviço determinam como o conteúdo é gerenciado pelo protocolo MQTT. Apesar de níveis elevados de QoS serem mais confiáveis, eles apresentam mais requisitos de latência e largura de banda, logo subscrever clientes pode especificar o nível mais alto de QoS que eles gostariam de receber.

O nível mais simples de QoS é um serviço "unacknowledged". Esse nível de QoS usa uma sequência de pacote PUBLISH. O Publisher envia uma mensagem ao Broker uma única vez e o Broker passa a mensagem ao Subscriber apena uma vez. Não há mecanismo em funcionamento que indique se a mensagem foi recebida corretamente, e note que o Broker não salva a mensagem. Este nível QoS pode também ser referido como "no máximo uma vez" (at most once), QoS0, ou atire e esqueça (fire and forget).

Fonte:
[1] https://internetofthingsagenda.techtarget.com/definition/MQTT-MQ-Telemetry-Transport (para mais informações).


## Instalações necessárias

### Python 

Linguagem utilizada no trabalho (versão 3.6.5).

Comando para instalá-lo:

`sudo apt-get install python3.6`

### Paho

Esta é uma biblioteca em Python do protocolo MQTT.

Comando para instalá-lo:

`pip install paho-mqtt`

### Mosquitto

Este é o programa utilizado para ser o Broker da comunicação dos nosso protocolo. Os comandos para instalá-lo no Linux são descritos abaixo:

`sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa`

`sudo apt-get update`

`sudo apt-get install mosquitto`

`sudo apt-get install mosquitto-clients`

Para rodar o Mosquitto:

`sudo mosquitto -v`

## Como funciona

Primeiro instala-se o Mosquitto. Em seguida pode-se abrir tanto Publisher quanto Subscriber. Ao rodar o código serão pedidas informações para endereço do broker e respectivamente pedir nome do Subscriber e nomes dos tópicos e Publishers. A partir das configurações prontas o broker se encarrega de gerenciar Publishers e Subscribers.
