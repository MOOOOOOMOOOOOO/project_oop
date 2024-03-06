#Reader.py
from datetime import datetime, date, timedelta
# from dateutil import relativedelta
from Book import Book
from Chapter import Chapter
from Coin import GoldenCoin
from Coin import SilverCoin
from ChapterTransaction import ChapterTransaction
from CoinTransaction import CoinTransaction
import Controller

class Reader:
    def __init__(self, username, password, birth_date):
        self.__username = username
        self.__password = password
        self.__birth_date = birth_date #check age_restricted
        self.__golden_coin = GoldenCoin(0)
        self.__silver_coin_list = []
        self.__book_shelf_list = []
        self.__recent_read_chapter_list = []
        self.__chapter_transaction_list = []
        self.__coin_transaction_list = []
    
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,username):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @username.setter
    def password(self,password):
        self.__password = password

    @property
    def birth_date(self):
        return self.__birth_date
    
    @property
    def golden_coin(self):
        return self.__golden_coin
    
    def add_golden_coin(self,amount):
        self.golden_coin.balance += amount
    def deduct_golden_coin(self,amount):
        self.golden_coin.balance -= amount
    
    @property
    def silver_coin_list(self):
        return self.__silver_coin_list
    def add_silver_coin(self,amount):
        self.__silver_coin.append(SilverCoin(amount))

    def delete_exp_silver_coin(self):
        for silver_coin in self.__silver_coin_list:
            if silver_coin.exp_date_time - datetime.now():
                self.__silver_coin_list.remove(silver_coin)

    def deduct_silver_coin(self,amount):
        self.delete_exp_silver_coin()
        for silver_coin in self.__silver_coin_list:
            if amount > silver_coin.balance :
                self.__silver_coin_list.remove(silver_coin)
                amount -= silver_coin.balance
            elif amount < silver_coin.balance :
                silver_coin.balance -= amount
                break
            else :
                self.__silver_coin_list.remove(silver_coin)
                break
    
    @property
    def book_shelf_list(self):
        return self.__book_shelf_list
    def add_book_shelf_list(self, book):
        if isinstance(book,Book):
            self.__book_shelf_list.append(book)

    @property
    def recent_read_chapter_list(self):
        return self.__recent_read_chapter_list
    def add_recent_read_chapter_list(self, chapter):
        if isinstance(chapter,Chapter):
            self.__recent_read_chapter_list.append(chapter)

    @property
    def chapter_transaction_list(self):
        return self.__chapter_transaction_list
    def add_chapter_transaction_list(self,chapter_transaction):
        if isinstance(chapter_transaction, ChapterTransaction):
            self.__chapter_transaction_list.append(chapter_transaction)
    
    @property
    def coin_transaction_list(self):
        return self.__coin_transaction_list
    def add_coin_transaction_list(self,coin_transaction):
        if isinstance(coin_transaction,CoinTransaction):
            self.__coin_transaction_list.append(coin_transaction)

    # def check_age_restricted(self):
    #     day, month, year = map(int, self.__birth_date.split('/'))
    #     birth = datetime(year, month, day)
    #     date_diff = relativedelta.relativedelta(datetime.now(),birth)
    #     if date_diff.years>=18 :
    #         return "over 18"
    #     else: 
    #         return "under 18"

class Writer(Reader):
    money_balance = 0
    def __init__(self,username,password,birth_date):
        super().__init__(username,password,birth_date)
        self.__writing_book_list = []
    
    @property
    def writing_list(self):
        return self.__writing_book_list
    
    def show_writing_name_list(self):
        show_writing_name_list = []
        for book in self.__writing_book_list:
            show_writing_name_list.append(book.name)
        return show_writing_name_list
    
    def add_writing_book_list(self,book):
        if isinstance(book,Book):
            self.__writing_book_list.append(book)

    @property
    def pseudonym_list(self):
        return self.__pseudonym
    
    def add_pseudonym(self, pseudonym):
        self.__pseudonym.append(pseudonym)

    @property
    def viewer_count(self):
        count = 0
        for book in self.__writing_book_list:
            for chapter in book.get_chapter_list():
                count += chapter.viewer_count
        return count
    
    @property
    def comment_list(self):
        comment_list = []
        for book in self.__writing_book_list:
            comment_list.append(book.get_comment_list())
        return comment_list
    
    @property
    def json_comment_list(self):
        comment_list = []
        for book in self.__writing_book_list:
            for comment in book.get_comment_list():
                comment_dict = {}
                comment_dict["user"] = comment.commentator.name
                comment_dict["context"] = comment.context
                comment_dict["chapter"] = f"#{comment.chapter.chapter_number} : {comment.chapter.name}"
                comment_dict["date_time"] = comment.publish_date_time
                comment_list.append(comment_dict)
        return comment_list
    

            


