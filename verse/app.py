from flask import Flask, render_template
import requests

app = Flask(__name__)
@app.route("/")
def grab_verse():
    url = "http://www.randomnumberapi.com/api/v1.0/random"
    params = {
        'min': 100,
        'max': 1000,
        'count': 1
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        random_number = data[0]
    except Exception as e:
        random_number = "Error fetching number"
        print(e)

    return render_template('index.html', number=random_number)

if __name__ == '__main__':
    app.run(debug=True)