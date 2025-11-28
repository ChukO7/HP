from flask import Flask
#Create a Flask application instance    
app = Flask(__name__)

#Define a route and view function
@app.route('/')
def hello():
    return "Hello, World!"

# To run the app, if this file is executed
if __name__ == '__main__':
    app.run(debug=True)