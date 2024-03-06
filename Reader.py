#Reader.py
from datetime import datetime, date, timedelta
from dateutil import relativedelta
import Book
import Chapter
import Coin
import ChapterTransaction
from CoinTransaction import CoinTransaction

class Reader:
    def __init__(self,username,password,birth_date):
        self.__username = username
        self.__display_name = username
        self.__password = password
        self.__birth_date = birth_date #check age_restricted
        self.__golden_coin = Coin.GoldenCoin(0)
        self.__silver_coin_list = []
        self.__book_shelf_list = []
        self.__recent_read_chapter_list = []
        self.__chapter_transaction_list = []
        self.__coin_transaction_list = []
        self.__follower_list = []
        self.__introduction = ''
    
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,username):
        self.__username = username

    @property
    def display_name(self):
        return self.__display_name
    @display_name.setter
    def display_name(self, display_name):
        self.__display_name = display_name

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
    def follower_list(self):
        return self.__follower_list
    
    def get_user_coin_balance(self):
      return self.__golden_coin.balance + self.get_silver_coin_balance()
    
    def get_silver_coin_balance(self):
      silver_coin_balance = 0
      for silver_coin in self.__silver_coin_list:
        silver_coin_balance += silver_coin.balance
      return silver_coin_balance
    
    @property
    def golden_coin(self):
        return self.__golden_coin
    
    @property
    def introduction(self):
        return self.__introduction
    @introduction.setter
    def introduction(self, text):
        self.__introduction = text
    
    def add_golden_coin(self,amount):
        self.golden_coin.balance += amount
    def deduct_golden_coin(self,amount):
        self.golden_coin.balance -= amount
    
    def get_silver_coin_list(self):
        return self.__silver_coin_list

    def add_silver_coin(self,amount):
        self.__silver_coin_list.append(Coin.SilverCoin(amount))

    def delete_exp_silver_coin(self):
        for silver_coin in self.__silver_coin_list:
            if silver_coin.exp_date_time - datetime.today():
                self.__silver_coin_list.pop(silver_coin)

    def deduct_silver_coin(self,amount):
        self.delete_exp_silver_coin()
        for silver_coin in self.__silver_coin_list:
            if amount > silver_coin.balance :
                self.__silver_coin_list.pop(silver_coin)
                amount -= silver_coin.balance
            elif amount < silver_coin.balance :
                silver_coin.balance -= amount
                break
            else :
                self.__silver_coin_list.pop(silver_coin)
                break
    
    def get_book_shelf_list(self):
        return self.__book_shelf_list
    def add_book_shelf_list(self,book):
        if isinstance(book,Book.Book):
            self.__book_shelf_list.append(book)
        
    def get_follower_list(self):
        return self.__follower_list

    def get_recent_read_chapter_list(self):
        return self.__recent_read_chapter_list
    def add_recent_read_chapter_list(self,chapter):
        if isinstance(chapter,Chapter.Chapter):
            self.__recent_read_chapter_list.append(chapter)

    def get_chapter_transaction_list(self):
        return self.__chapter_transaction_list
    def add_chapter_transaction_list(self,chapter_transaction):
        if isinstance(chapter_transaction,ChapterTransaction):
            self.__chapter_transaction_list.append(chapter_transaction)
    
    def get_coin_transaction_list(self):
        return self.__coin_transaction_list
    def add_coin_transaction_list(self,coin_transaction):
        if isinstance(coin_transaction,CoinTransaction):
            self.__coin_transaction_list.append(coin_transaction)

    def check_age_restricted(self):
        day, month, year = map(int, self.__birth_date.split('/'))
        birth = datetime(year, month, day)
        date_diff = relativedelta.relativedelta(datetime.now(),birth)
        if date_diff.years>=18 :
            return "over 18"
        else: 
            return "under 18"
        
    def show_coin_transaction(self):
        show_list = []
        for coin_transaction in self.__coin_transaction_list:
            payment_type = coin_transaction.payment.name
            golden_amount = coin_transaction.golden_amount
            silver_amount = coin_transaction.silver_amount
            price = coin_transaction.price
            date_time = coin_transaction.date_time
            show_list.append(f"{payment_type} +{golden_amount}_golden_coin +{silver_amount}_silver_coin -{price} baht at {date_time}")
        return show_list


class Writer(Reader):
    money_balance = 0
    def __init__(self,username,password,birth_date):
        super().__init__(username,password,birth_date)
        self.__writing_book_list = []
        self.__pseudonym = []
    
    def get_writing_list(self):
        return self.__writing_book_list
    
    def show_writing_list(self):
        show_writing_list = []
        for book in self.__writing_book_list:
            show_writing_list.append(book.name)
        return show_writing_list
    
    def add_writing_book_list(self,book):
        if isinstance(book,Book.Book):
            self.__writing_book_list.append(book)

    def get_pseudonym_list(self):
        return self.__pseudonym
    
    def add_pseudonym(self, pseudonym):
        self.__pseudonym.append(pseudonym)

    def get_viewer_count(self):
        count = 0
        for book in self.__writing_book_list:
            for chapter in book.get_chapter_list():
                count += chapter.viewer_count
        return count
    
    def get_comment_list(self):
        comment_list = []
        for book in self.__writing_book_list:
            comment_list.append(book.get_comment_list())
        return comment_list
    
    def get_json_comment_list(self):
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
