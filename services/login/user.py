from provider.userprovider import userProvider


class user:

    def login(self, user_provider: userProvider, body: dict):

        # Accessing user by email. Email can't be null since it is required on swagger yaml
        user = user_provider.get_user(body['email'])
        print(user)

        # User not found, Return an error
        if user is None:
            return {'code': 'INVALID_CREDENTIALS', 'description': 'Invalid email or password'}, 400

        # Password mismatched
        if user['password'] != body.get('password') :
            return {'code': 'INVALID_CREDENTIALS', 'description': 'Invalid email or password!'}, 400

        # Password matched, Valid Login request
        print("Login success!!!")
        return {'token': user}, 200

class_instance = user()
