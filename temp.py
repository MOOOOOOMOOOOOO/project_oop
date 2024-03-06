#Reader.py
from datetime import datetime, date, timedelta
import Book
import Chapter
import Coin
import ChapterTransaction
import CoinTransaction

class Reader:
    def __init__(self,username,password,birth_date):
        self.__username = username
        self.__password = password
        self.__birth_date = birth_date #check age_restricted
        self.__golden_coin = Coin.GoldenCoin(0)
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
    
    def get_silver_coin_list(self):
        return self.__silver_coin_list
    def add_silver_coin(self,amount):
        self.__silver_coin.append(Coin.SilverCoin(amount))

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


class Writer(Reader):
    money_balance = 0
    def __init__(self,username,password,birth_date):
        super().__init__(username,password,birth_date)
        self.__writing_book_list = []
    
    @property
    def writing_book_list(self):
        return self.__writing_book_list
    def add_writing_book_list(self,book):
        if isinstance(book,Book.Book):
            self.__writing_book_list.append(book)