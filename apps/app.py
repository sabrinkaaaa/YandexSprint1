from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/temperature')
def get_temperature():
    location = request.args.get('location', '')
    sensor_id = request.args.get('sensorID', '')

    if not location:
        location = {
            "1": "Living Room",
            "2": "Bedroom",
            "3": "Kitchen"
        }.get(sensor_id, "Unknown")

    if not sensor_id:
        sensor_id = {
            "Living Room": "1",
            "Bedroom": "2",
            "Kitchen": "3"
        }.get(location, "0")

    return jsonify({
        "location": location,
        "sensor_id": sensor_id,
        "temperature": round(random.uniform(15, 30), 2)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
