from flask import Flask, render_template, jsonify
import random
# import serial

# ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
# ser.flush()

    
app = Flask(__name__)

@app.route('/')
def Index():
    return render_template("index.html")

@app.route('/info')
def Info():
    
    # line = ser.readline().decode('utf-8').rstrip()
    line = random.randrange(10)
    res = {
        'A': line,
    }
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True,port=9900)