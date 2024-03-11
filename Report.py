from datetime import datetime

class Report:
    def __init__(self, report_to, user, report_type, context):
        self.__report_to = report_to
        self.__user = user
        self.__report_type = report_type
        self.__context = context
        self.__date_time = datetime.now()

    @property
    def report_to(self):
        return self.__report_to

    @property
    def user(self):
        return self.__user

    @property
    def report_type(self):
        return self.__report_type

    @property
    def context(self):
        return self.__context

    @property
    def date_time(self):
        return f"{self.__date_time.strftime('%x')} {self.__date_time.strftime('%X')}"

    @report_to.setter
    def report_to(self, report_to):
        self.__report_to = report_to

    @user.setter
    def user(self, user):
        self.__user = user

    @report_type.setter
    def report_type(self, report_type):
        self.__report_type = report_type

    @context.setter
    def context(self, context):
        self.__context = context

    @date_time.setter
    def date_time(self, date_time):
        self.__date_time = date_time

    def delete(self):
        if self.__report_to:
            self.__report_to.delete_report(self)
