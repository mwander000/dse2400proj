# ESP32
Python scripts housed on the ESP32 boards for interfacing with the BME280 sensor and the MQTT broker. The board acts as a client and publishes values from the BME280 obtained across I2C to the broker.
* boot.py - Imports, Wi-Fi connectivity, MQTT server IP address, and BME280 object instantiation.
* main.py - Establishes an MQTTClient object, connects to the broker, and publishes values in a loop.
* bme280_float.py - Module for interfacing with the BME280 sensor across I2C. https://github.com/robert-hh/BME280/blob/master/bme280_float.py
* umqttsimple.py - MQTT client module (simple). https://github.com/fizista/micropython-umqtt.simple2/blob/master/src/umqtt/simple2.py
* robust2.py - MQTT client module (robust). https://github.com/fizista/micropython-umqtt.robust2/blob/master/src/umqtt/robust2.py
