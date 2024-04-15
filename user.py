class User:
    def __init__(self, details):
        self.email = details[0]
        self.password = details[1]
        self.first_name = details[2]
        self.last_name = details[3]

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
