# https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/mqtt

import network

def conncb(task):
    print("[{}] Connected".format(task))


def disconncb(task):
    print("[{}] Disconnected".format(task))


def subscb(task):
    print("[{}] Subscribed".format(task))


def pubcb(pub):
    print("[{}] Published: {}".format(pub[0], pub[1]))


def datacb(msg):
    print("[{}] Data arrived from topic: {}, Message:\n".format(
        msg[0], msg[1]), msg[2])

# mqtt = network.mqtt(name, server [, user, password, port, autoreconnect, clientid, cleansession, keepalive, qos, retain, secure, connected_cb, disconnected_cb, subscribed_cb, unsubscribed_cb, published_cb, data_cb])
mqtt = network.mqtt("loboris", "mqtt.m5stack.com", connected_cb=conncb, disconnected_cb=disconncb, subscribed_cb=subscb, published_cb=pubcb, data_cb=datacb)

# secure connection requires more memory and may not work
# mqtts = network.mqtt("eclipse", "iot.eclipse.org", secure=True, cleansession=True, connected_cb=conncb, disconnected_cb=disconncb, subscribed_cb=subscb, published_cb=pubcb, data_cb=datacb)


'''

# Wait until status is: (1, 'Connected')

mqtt.subscribe('test')
mqtt.publish('test', 'Hi from Micropython')

'''
