class userProvider(object):
    User = {
        "learningcurve@gmail.com":{
            "user_id":"001",
            "email": "learningcurve@gmail.com",
            "first_name": "d0001",
            "last_name" : "1",
            "password" : "1234"
        }
    }

    def get_user(self,email) -> dict:
        return self.User.get(email,None)