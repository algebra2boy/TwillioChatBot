from flask import Flask, request 
from twilio.twiml.messaging_response import MessagingResponse
from src.userinfo import UserInfo # a class contains info about the user 
from datetime import datetime # to get retrieve current time of the user 
import src.messages as m # import all the constants 


# initalize the flask application
app = Flask(__name__)

# make sure that you fix the typos and put the header 'methods'
@app.route('/sms', methods=['POST'])
def chatbot():
	# receive user's paramater
	args = request.values
	current_time = datetime.now().strftime("%H:%M:%S")
	user_info = UserInfo(args.get('Body'),
						 args.get('ProfileName'),
						 args.get('From').split(":")[1],
						 args.get('Longtitude'),
						 args.get('Latitude'),
						 current_time)
	



	messaging_response = MessagingResponse()
	message = messaging_response.message()
	message.body(m.introduction)

	# string representation of the response
	return str(messaging_response)



# run the application here and activate debugger 
if __name__=='__main__':
    app.run(debug=True)