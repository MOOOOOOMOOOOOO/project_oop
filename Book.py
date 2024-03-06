#Book.py
import Controller
import datetime
import Chapter
import Report
import Comment

class Book:
    viewer_count = 0
    add_to_shelf_count = 0

    def __init__(self,name,writer,tag_list,status,age_restricted,prologue,date_time):
        self.__name = name
        self.__writer = writer
        self.__tag = tag_list
        self.__status = status
        self.__age_restricted = age_restricted
        self.__prologue = prologue
        self.__chapter_list = []
        self.__comment_list = []
        self.__report_list = []
        self.__date_time = date_time
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def writer(self):
        return self.__writer

    @property
    def tag(self):
        return self.__tag
    @tag.setter
    def tag(self,tag):
        self.__tag = tag
    
    @property
    def age_restricted(self):
        return self.__age_restricted
    @age_restricted.setter
    def age_restricted(self,age_restricted):
        self.__age_restricted = age_restricted

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self,status):
        self.__status = status

    @property
    def prologue(self):
        return self.__prologue
    @prologue.setter
    def prologue(self,prologue):
        self.__prologue = prologue

    @property
    def date_time(self):
        return self.__date_time
    @date_time.setter
    def date_time(self,date_time):
        self.__date_time = date_time

    def get_chapter_list(self):
        return self.__chapter_list
    def add_chapter_list(self,chapter):
        if isinstance(chapter,Chapter):
            self.__chapter_list.append(chapter)

    def get_report_list(self):
        return self.__report_list
    def add_report_list(self,report):
        if isinstance(report,Report):
            self.__report_list.append(report)

    def get_comment_list(self):
        return self.__comment_list
    def add_comment_list(self,comment):
        if isinstance(comment,Comment):
            self.__comment_list.append(comment)

    def add_report_list(self, report):
        self.report_list.append(report)
        self.counting_date_time = datetime.now()

    def counting_report_from_type(self):
        report_count=0
        for report in self.__report_list:
            for report_type in Controller.WriteARead.report_type_list:
                if report_count == 10:
                    break
                if report.report_type == report_type:
                    report_count+=1

    def delete_report(self, report):
      if report in self.report_list:
          self.report_list.remove(report)