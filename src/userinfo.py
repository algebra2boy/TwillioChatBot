import json
class UserInfo:

    def __init__(self, body, name, phone_number, longitude, latitude, time):
        self.body = body
        self.name = name
        self.phone_number = phone_number
        self.longitude = longitude
        self.latitude = latitude
        self.time = time
        self.option = 0

    def dict_format(self) -> dict:
        return {"body": self.body,
                "name": self.name,
                "phone_number": self.phone_number,
                "longitude": self.longitude,
                "latitude": self.latitude,
                "time received": self.time,
                "option": self.option}

    def JSON_data(self) -> dict:
        return {"longitude": self.longitude,
                "latitude": self.latitude,
                "time received": self.time,
                "option": self.option}

    def has_location(self) -> bool:
        return self.latitude is not None and self.longitude is not None
       
