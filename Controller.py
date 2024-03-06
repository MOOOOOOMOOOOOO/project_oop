import Book
import Chapter
import ChapterTransaction
import CoinTransaction
from Reader import Reader, Writer


class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__report_list = []
        self.__writer_list = []
        self.__payment_list = []
        self.__promotion_list = []
        self.__report_type_list = ["violence","harrasment"]

    def add_reader(self, reader):
        self.__reader_list.append(reader)

    def add_report(self, report):
        self.__report_list.append(report)

    def search_book_by_name(self, book_name):
        search_list=[]
        for writer in self.__writer_list:
            for book in writer.writing_book_list:
                if book_name.lower() in book.name.lower():
                    search_list.append(book.name)
                    
        if search_list==[]:
            return "huhuuuu"
        else:
            return search_list
          
    def search_user(self, username):
        search_list = []
        for reader in self.__reader_list:
            if username.lower() in reader.username.lower():
                search_list.append(reader.username)
        
        for writer in self.__writer_list:
            if username.lower() in writer.username.lower() and writer.username not in search_list:
                search_list.append(writer.username)

        if search_list == []:
            return "user not found"
        else:
            return search_list
                    
    def get_book_by_name(self, book_name):
        for writer in self.__writer_list:
            for book in writer.book:
                if book.name == book_name:
                    return book
                
    def get_user_by_username(self, username):
        for reader in self.__reader_list:
            if reader.username == username:
                return reader
        
        for writer in self.__writer_list:
            if writer.username == username:
                return writer
            
        return "User Not Found"

    @property
    def report_type_list(self):
        return self.__report_type_list

    def search_coin_promotion(self, code):
        pass

    def add_writer(self, writer):
        self.__writer_list.append(writer)

    def add_payment(self, payment):
        self.__payment_list.append(payment)

    def add_promotion(self, promotion):
        self.__promotion_list.append(promotion)

    def buy_chapter(self, chapter_id, book_name, username):
        book = self.get_book_by_name(book_name)
        chapter_list = book.get_chapter_list()

        for chapter in chapter_list:
            if chapter.chapter_id == chapter_id:
                cost = chapter.cost

        user = self.get_user_by_username(username)
        coin_balance = user.get_user_coin_balance()

        if coin_balance >= cost:
            user.deduct_coin(cost)
            user.add_chapter_transaction()
        else:
            return "Not enough coin"
        
    def show_coin(self, username):
        user = self.get_user_by_username(username)
        if user:
            return f"Golden Coin : {user.golden_coin.balance} | Silver Coin : {user.get_silver_coin_balance()}"
        return "User Not Found"
    
    def sign_up(self,username:str, password:str, birth_date: str):
        new_reader = Reader(username,password,birth_date)
        if isinstance(new_reader, Reader):
            self.add_reader(new_reader)
            return {"User": "sign up success"}
        else : 
            return {"User": "please try again"}
        
    def create_report(self, username: str, report_type: str, content: str):
        content = Reader(username, report_type, content)
        if isinstance(content, Reader):
            self.add_report(content)
            return {"User": "Report created successfully."}
        else:
            return {"User": "Content not found."}
        
        
    def show_my_page(self, username):
        writing_count = 0
        reads = 0
        writing_list = None
        pseudonym_list = None
        comments = None
        user = self.get_user_by_username(username)
        if isinstance(user, Writer):
            writing_count = len(user.get_writing_list())
            reads = user.get_viewer_count()
            writing_list = user.get_writing_name_list()
            pseudonym_list = user.get_pseudonym_list()
            comment_list = user.get_json_comment_list()
        else:
            return "User Not Found"
        return {"display_name" : user.display_name,
                "introduction" : user.introduction,
                "writing_count" : writing_count,
                "book_on_shelf_count" : len(user.get_book_shelf_list()),
                "followers" : len(user.get_follower_list()),
                "read_count" : len(user.get_recent_read_chapter_list()),
                "viewer_count" : reads,
                "writings" : writing_list,
                "pseudonyms" : pseudonym_list,
                "comments" : comment_list}
    
    def show_my_profile(self, username):
        writing_count = 0
        reads = 0
        writing_list = None
        pseudonym_list = None
        comments = None
        user = self.get_user_by_username(username)
        if isinstance(user, Writer):
            writing_count = len(user.get_writing_list())
            reads = user.get_viewer_count()
            writing_list = user.get_writing_name_list()
            pseudonym_list = user.get_pseudonym_list()
            comment_list = user.get_json_comment_list()
        else:
            return "User Not Found"
        return {"display_name" : user.display_name,
                "username" : user.username,
                "password" : "*" * len(user.password),
                "book_on_shelf_count" : len(user.get_book_shelf_list()),
                "followers" : len(user.get_follower_list()),
                "read_count" : len(user.get_recent_read_chapter_list()),
                "viewer_count" : reads,
                "writings" : writing_list,
                "pseudonyms" : pseudonym_list,
                "comments" : comment_list}
    
        # def show_my_writing_list(self, writer_name=None):
    #     writing_list = []
    #     for writer in self.__writer_list:
    #         if writer_name is None or writer_name.lower() == writer.username.lower():
    #             writing_list.extend(writer.get_writing_list())

    #     if writing_list:
    #         book_names = [book.name for book in writing_list]
    #         return book_names
    #     else:
    #         return "No books found."
        
    # def upgrade_to_writer(self):
    #     WriteARead.add_writer(self)
    #     print("Congratulations! You have been upgraded to a Writer.")
    #     return

    # def show_my_writing(self, writer_name=None):
    #     writing_list = []
    #     is_writer = False
    #     for writer in self.__writer_list:
    #         if writer_name is None or writer_name.lower() == writer.username.lower():
    #             writing_list.extend(writer.get_writing_list())
    #             is_writer = True

    #     if writing_list:
    #         # สร้างรายการเป็น list ของชื่อหนังสือ
    #         book_names = [book.name for book in writing_list]
    #         return book_names
    #     elif is_writer:
    #         return "No books found."
    #     else:
    #         upgrade = input("Do you want to upgrade to writer? (yes/no): ").lower()
    #         if upgrade == "yes":
    #             self.upgrade_to_writer()
    #         else:
    #             return "You have no books in your writing list."
    

    