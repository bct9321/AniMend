# Import necessary modules
from flask import Flask, render_template, request
from animend import process_directories_batch  # Import function from animend.py

# Create the Flask application
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to process the directories and display results
@app.route('/process', methods=['POST'])
def process_directories():
    process_directories_batch()  # Call the function from animend.py
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
