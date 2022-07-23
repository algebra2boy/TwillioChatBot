from flask import Flask

# initalize the flask application
app = Flask(__name__)


@app.route('/')
def hello():
	return "hello"


# run the application here and activate debugger 
if __name__=='__main__':
    app.run(debug=True)