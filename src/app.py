from flask import Flask, request 
from twilio.twiml.messaging_response import MessagingResponse
from src.userinfo import UserInfo # a class contains info about the user 
from datetime import datetime # to get retrieve current time of the user 
import src.messages as m # import all the constants 
import os # use to manipulate folders and path 
import json # use to handle json files between various applications
import src.API as API # all the API are here 
from dotenv import load_dotenv, find_dotenv # set up environmental variables in .env


# initalize the flask application
app = Flask(__name__)

# search from .env file and looks for keys
load_dotenv(find_dotenv())


# make sure that you fix the typos and put the header 'methods'
@app.route('/sms', methods=['POST'])
def chatbot():
	# receive user's paramater
	args = request.values
	print(args)
	current_time = datetime.now().strftime("%H:%M:%S %m/%d/%Y")
	# initalize the user info
	user_info = UserInfo(args.get('Body').lower(),
						 args.get('ProfileName'),
						 args.get('From').split(":")[1],
						 args.get('Longitude'),
						 args.get('Latitude'),
						 current_time)
	

	# making the response and message object to respond back 
	messaging_response = MessagingResponse()
	message = messaging_response.message()


	# check if user exists in the system
	# this program is being run on Macbook, so we use / to direct path
	if os.path.exists(f"uploads/{user_info.phone_number}"):
		'''exists in the system'''
		if user_info.has_location(): 
			with open(f"uploads/{user_info.phone_number}/location.json", "w") as file:
				json.dump(user_info.JSON_data(), file, indent=4, sort_keys=True)
			message.body(m.location_received)
			# After receiving the location, start showing options
			message.body(m.options)
			return str(messaging_response)
	else:
		'''does not exist'''
		if user_info.body == 'y':
			'''want to use our bot, so then create a folder for user'''
			message.body(m.share_location)
			try:
				os.mkdir(f"uploads/{user_info.phone_number}")
				print("a folder has been created for the user")
			except:
				print("unsuccessful folder creation")
			return str(messaging_response)

		elif user_info.body == 'n': 
			'''does not want to use our bot'''
			message.body(m.goodbye)
			return str(messaging_response)

		elif user_info.body == 'hi' or user_info.body == 'hello':
			message.body(m.introduction)
			return str(messaging_response)

		else:  # random message at the beginning 
			message.body(m.start_conversation)
			return str(messaging_response)

	# start getting the JSON data from user's folder 
	try:
		with open(f"uploads/{user_info.phone_number}/location.json", "r") as file:
			# json.load() accepts file object, parses the JSON data, populates a Python dictionary with the data and returns it back to you
			data = json.load(file)
			latitude = data.get('latitude')
			longtitude = data.get('longtitude')
			time_rec = data.get('time received')
	except FileNotFound:
		message.body(m.location_json_not_exist)
		return str(messaging_response)


	# check if the user types an actual integer like 1,2,3,4 for options
	if len(user_info.body) == 1:
		try:
			data['option'] = int(user_info.body)
		except ValueError:
			pass
		else:
			with open(f"uploads/{user_info.phone_number}/location.json", "w") as file:
				json.dump(data, file, indent=4, sort_keys=True)
	option = data.get('option')  # option got updated so it must be placed here
	print(option)

	# chat bot logic
	if option == 1: # OPENWEATHER
		weather_APIKEY = os.getenv("OPENWEATHERAPI_KEY")
		weather = API.get_weather_info(latitude, longtitude, weather_APIKEY)
		message.body(weather)
		return str(messaging_response) 
	elif option == 2: 
		if data.get('destination') == None and data.get('mode') == None: # the system has no destination and the mode of transportation 
			if len(user_info.body) == 1:
				message.body("Where would you like to go?")
			else: # The destination session (reading user's input)
				data['destination'] = user_info.body
				try:
					with open(f"uploads/{user_info.phone_number}/location.json", "w") as file:
						json.dump(data, file, indent=4, sort_keys=True)
				except FileNotFound:
						message.body(m.location_json_not_exist)
				else:
					message.body('How would you like to get there\t\t\t\t1.   Car\n2.   Walk\n3.   Train\n4.   Bicycle')
			return str(messaging_response) 
		elif data.get('destination') != None and data.get('mode') == None: 
			# accepting a single letter (a,b,c,d)
			if len(user_info.body) == 1 and user_info.body.isalpha():
				mode = user_info.body
				if mode == 'a':
					tranportation = "Car"
				elif mode == 'b':
					tranportation = "Walk"
				elif mode == 'c':
					tranportation = "Train"
				elif mode == 'e':
					tranportation = "Bicycle"
				else:
					tranportation = None
					message.body("not an option")
				data['tranportation'] = tranportation
				with open(f"uploads/{user_info.phone_number}/location.json", "w") as file:
						json.dump(data, file, indent=4, sort_keys=True)
			else:
				message.body("Not valid letter (must be a,b,c,d)")
			return str(messaging_response)
		elif data.get('destination') != None and data.get('mode') != None: 


		# return str(messaging_response) 

	# elif user_info.body == '3':

	# elif user_info.body == '4':

	# else:
	


	# string representation of the response
	return str(messaging_response)



# run the application here and activate debugger 
if __name__=='__main__':
    app.run(debug=True)