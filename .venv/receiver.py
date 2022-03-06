import paho.mqtt.client as mqtt

# fonction appelée lors de la connection
def on_connect(client, userdata, flags, rc):
    print("connected")   
    print("j'ecoute les events d'enigma 2021")
    client.publish("/tmp")
    


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

client.loop_forever()