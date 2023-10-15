# Import the Flask class from the flask module
from flask import Flask, render_template

# Create an instance of the Flask class, which will be our web application
app = Flask(__name__)


@app.route('/fizzbuzz')
def fizzbuzz():
    numbers = range(1, 101)
    return render_template('template.html', numbers=numbers)


# This block of code is executed if the file is run as a script (not imported as a module)
if __name__ == '__main__':
    # Run the Flask web server with debugging mode turned on
    app.run(debug=True)
