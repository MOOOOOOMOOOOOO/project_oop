from datetime import datetime, timedelta
import Book

class Promotion():
    def __init__(self, start_date_time, discount):
        day, month, year = map(int, start_date_time.split('/'))
        self.__start_date_time = datetime(year, month, day)
        self.__end_date_time = self.__start_date_time + timedelta(days=10)
        self.__discount = discount

    @property
    def start_date_time(self):
        return self.__start_date_time
    @property
    def end_date_time(self):
        return self.__end_date_time
    @property
    def discount(self):
        return self.__discount

    def is_valid(self):
        current_time = datetime.now()
        return self.start_date_time <= current_time <= self.end_date_time


class CoinPromotion(Promotion):
    def __init__(self, start_date_time,discount, code):
        super().__init__(start_date_time,discount)
        self.__code = code

    @property
    def code(self):
        return self.__code

class BookPromotion(Promotion):
    def __init__(self, start_date_time,discount, promotion_book_list):
        super().__init__(start_date_time,discount)
        self.__promotion_book_list = promotion_book_list

    @property
    def promotion_book_list(self):
        return self.__promotion_book_list
    
    def add_promotion_book_list(self,book):
        if isinstance(book,Book.Book):
            self.__promotion_book_list.append(book)

    def remove_promotion_book_list(self, book):
        if book in self.__promotion_book_list:
            self.__promotion_book_list.remove(book)