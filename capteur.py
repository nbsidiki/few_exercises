import paho.mqtt.client as mqtt
from win10toast import ToastNotifier
 
toaster = ToastNotifier()
 
def on_connect(client, userdata, flags, rc):
    print("connected")
    print("écoute du sujet enigma")
    client.subscribe("/temp")
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if float(msg.payload.decode("utf-8")) < 0 :
        client.publish("/beep", "Alerte température négative")
        toaster.show_toast("Ruche", "TEMPERATURE NEGATIVE BG !", duration = 5)
 
# Def du client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
# Paramétrage
client.connect("broker.hivemq.com", 1883, 60)
 
# Loop
client.loop_forever()


