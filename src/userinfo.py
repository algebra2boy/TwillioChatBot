import json
class UserInfo:

	def __init__(self, body, name, phone_number, longtitude, latitude, time):
		self.body = body
		self.name = name
		self.phone_number = phone_number
		self.longtitude = longtitude
		self.latitude = latitude
		self.time = time
		self.option = 0


	def dict_format(self) -> dict:
		return {"body": self.body,
				"name": self.name,
				"phone_number": self.phone_number,
				"longtitude": self.longtitude,
				"latitude": self.latitude,
				"time received": self.time,
				"option": self.option}


	def JSON_data(self) -> dict:
		return {"longtitude": self.longtitude,
				"latitude": self.latitude,
				"time received": self.time,
				"option": self.option} 

	def has_location(self) -> bool:
		return self.latitude is not None and self.longtitude is not None 

	def store_option(self) -> None:
		try:
			self.option = int(self.body)
		except:
			raise ValueError("The option is not an integer")
		else:
			with open(f"uploads/{self.phone_number}/location.json", "w") as file:
				json.dump(self.JSON_data(), file, indent=4, sort_keys=True)



