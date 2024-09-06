# Importing necessary modules
from flask import Flask, render_template

# Initializing Flask app
app = Flask(__name__)

# Route to render the 'index.html' template
@app.route('/')
def index():
    return render_template('index.html')

# Running the Flask app
if __name__=='__main__':
    app.run(debug=True)