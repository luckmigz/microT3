from flask import Flask, jsonify
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# Configurações do GPIO
LDR_PIN = 14  # Pino GPIO que está conectado ao LDR
GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR_PIN, GPIO.IN)

@app.route('/sensor', methods=['GET'])
def read_light_sensor():
    light_value = GPIO.input(LDR_PIN)
    return jsonify({'light': light_value})

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()
