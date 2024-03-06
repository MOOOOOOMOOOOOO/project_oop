from datetime import datetime, timedelta

class Chapter:
    def __init__(self, chapter_number, chapter_name, context, cost, book_name):
        self.__chapter_id = str(book_name) + "/" + str(chapter_number)
        self.__chapter_number = chapter_number
        self.__name = chapter_name
        self.__context = context
        self.__publish_date_time = datetime.now()
        self.__viewer_count = 0
        self.__comment_list = []
        self.__cost = cost

    @property
    def name(self):
        return self.__name
    
    @property
    def chapter_id(self):
        return self.__chapter_id
    
    @property
    def chapter_number(self):
        return self.__chapter_number
    
    @property
    def context(self):
        return self.__context
    
    @property
    def publish_date_time(self):
        return self.__publish_date_time
    
    @property
    def publish_date_time_str(self):
        return self.__publish_date_time.strftime("%d/%m/%Y, %H:%M:%S")
    
    @property
    def cost(self):
        return self.__cost

    @property
    def viewer_count(self):
        return self.__viewer_count

    def add_comment(self, comment):
        self.__comment_list.append(comment)

    def add_viewer_count(self):
        self.__viewer_count += 1

    def update_cost(self, new_cost):
        self.__cost = new_cost

    def update_name(self, new_name):
        self.__name = new_name

    def update_context(self, context):
        self.__context = context