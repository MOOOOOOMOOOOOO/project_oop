from datetime import datetime, timedelta

class Webmaster:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password
    
    @username.setter
    def username(self, username):
        self._username = username
    
    @password.setter
    def password(self, password):
        self._password = password

    def check_edits(self, book):
        if book.edited and (datetime.now() - book.counting_date_time).days <= 7:
            return True
        return False
