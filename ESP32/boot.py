# This file is executed on every boot (including wake-boot from deepsleep)

# base imports
import os
import bme280_float as bme280

# MQTT imports
from robust2 import MQTTClient
import ubinascii
import machine
import utime as time
import gc
import micropython
import network
import esp

esp.osdebug(None)

#import webrepl
#webrepl.start()

# Connect Wi-Fi
import network
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
	print('Connecting to network...')
	sta_if.active(True)
	sta_if.connect('my_network_SSID', 'my_password')
	while not sta_if.isconnected():
		pass
print('Network Config:', sta_if.ifconfig())


# BME instantiation

# i2c connection
scl = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
sda = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
i2c = machine.I2C(scl=scl, sda=sda, freq=10000)

# BME object
bme = bme280.BME280(i2c=i2c, address=0x77)

# MQTT
mqtt_server = 'mqtt_broker_ip_address'
client_id = ubinascii.hexlify(machine.unique_id())