# MQTT
client = MQTTClient(client_id, mqtt_server, user='my_username', password='my_password')

def checkwifi():
    while not sta_if.isconnected():
        time.sleep_ms(500)
        print(".")
        sta_if.connect()

def publish():
    while True:
        checkwifi()
        if not client.is_conn_issue():

            # Get values from BME280
            v = bme.read_compensated_data()

            # Create message to be published
            # Unix timestamp (ns precision) added automatically to end of string by telegraf
            msg = 'weather,latitude=my_lat,longitude=my_long temperature=%f,pressure=%f,humidity=%f' % (v[0], v[1]*0.01, v[2])

            # Publish message to chosen topic
            client.publish('home/weather', msg)
            print(msg)
            time.sleep(5)
        else:
            # print('Reconnecting...')
            time.sleep_ms(500)
            client.reconnect()

client.reconnect()
publish()