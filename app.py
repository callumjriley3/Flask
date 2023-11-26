from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def convert_to_fahrenheit(celsius):
    """Calculate the equivalent of Celsius temperature in Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return str(fahrenheit)


@app.route('/f/<celsius>')
def f(celsius=0.0):
    return f"{celsius} degrees Celsius = {convert_to_fahrenheit(float(celsius))} degrees Fahrenheit"


if __name__ == '__main__':
    app.run()
