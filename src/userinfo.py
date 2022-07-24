class UserInfo:

	def __init__(self, body, name, phone_number, longtitude, latitude, time):
		self.body = body
		self.name = name
		self.phone_number = phone_number
		self.longtitude = longtitude
		self.latitude = latitude
		self.time = time


	def dict_format(self) -> dict:
		return {"body": self.body,
				"name": self.name,
				"phone_number": self.phone_number,
				"longtitude": self.longtitude,
				"latitude": self.latitude,
				"time received": self.time}


	def JSON_data(self) -> dict:
		return {"longtitude": self.longtitude,
				"latitude": self.latitude,
				"time received": self.time} 

	def has_location(self) -> bool:
		return self.latitude is not None or self.longtitude is not None 