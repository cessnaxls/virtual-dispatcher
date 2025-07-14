from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    trip = []
    if request.method == 'POST':
        # Example: Generate random 5-day trip rig
        airlines = ['DAL', 'AAL']
        aircraft = ['B737', 'B757', 'CRJ700']
        airports = ['IND', 'ATL', 'DFW', 'ORD', 'CLT']

        for day in range(1, 6):
            leg = {
                'day': day,
                'airline': random.choice(airlines),
                'aircraft': random.choice(aircraft),
                'dep': random.choice(airports),
                'arr': random.choice([ap for ap in airports if ap != 'IND']),
                'dep_time': f"{random.randint(5, 22)}:{random.randint(0,59):02d}",
                'arr_time': f"{random.randint(5, 22)}:{random.randint(0,59):02d}"
            }
            trip.append(leg)

    return render_template('index.html', trip=trip)

if __name__ == '__main__':
    app.run(debug=True)
