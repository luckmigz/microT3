from flask import Flask, jsonify
import RPi.GPIO as GPIO
import time
import threading

app = Flask(__name__)

# Configuração do GPIO
SENSOR_PIN = 18 # Pino GPIO onde o sensor LM393 está conectado
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

# Variável global para armazenar o estado do sensor
sensor_state = 0

# Função para monitorar o estado do sensor de luz continuamente
def monitor_sensor():
    global sensor_state
    while True:
        # Lê o estado atual do sensor
        sensor_state = GPIO.input(SENSOR_PIN)
        time.sleep(0.5)  # Intervalo de atualização de 0,5 segundos

# Rota HTTP para fornecer o estado do sensor
@app.route('/sensor', methods=['GET'])
def get_sensor_state():
    # Retorna o estado do sensor em formato JSON
    return jsonify({'light_on': bool(sensor_state)})

# Iniciar a função de monitoramento em uma thread separada
if __name__ == '__main__':
    try:
        sensor_thread = threading.Thread(target=monitor_sensor)
        sensor_thread.start()
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()
