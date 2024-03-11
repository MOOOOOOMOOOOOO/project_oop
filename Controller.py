from Book import Book 
from Chapter import Chapter 
from Comment import Comment 
from Reader import Reader, Writer 
from CoinTransaction import CoinTransaction 
from ChapterTransaction import ChapterTransaction 
from Promotion import CoinPromotion, BookPromotion
from Payment import OnlineBanking, TrueMoneyWallet, DebitCard
from datetime import datetime

class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__writer_list = []
        self.__payment_list = ["OnlineBanking", "Debit Card", "TrueMoney Wallet"]
        self.__promotion_list = []
        self.__report_type_list = ["violence", "harrasment"]
    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Sub Methods <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # ____________________________________Getters___________________________________
    
    @property
    def reader_list(self):
        return self.__reader_list
    
    @property
    def writer_list(self):
        return self.__writer_list
    
    @property
    def payment_list(self):
        return self.__payment_list

    @property
    def report_type_list(self):
        return self.__report_type_list
    
    @property
    def all_book_list(self):
        book_list=[]
        for writer in self.__writer_list:
            for book in writer.writing_list:
                book_list.append(book)
        return book_list
    
    @property
    def all_pseudonym_list(self):
        pseudonym_list = []
        for user in self.__writer_list:
            for pseudonym in user.pseudonym_list:
                pseudonym_list.append(pseudonym)
        return pseudonym_list
    
    def get_book_by_name(self, book_name):
        for book in self.all_book_list:
            if book.name == book_name:
                return book
        return "Book Not Found"
                
    def get_user_by_username(self, username):
        for reader in self.__reader_list:
            if reader.username == username:
                return reader
        
        for writer in self.__writer_list:
            if writer.username == username:
                return writer
            
        return "User Not Found"
    
    def get_chapter_by_chapter_id(self, chapter_id):
        for book in self.all_book_list:
            for chapter in book.chapter_list:
                if chapter.chapter_id == chapter_id:
                    return chapter
        return "Chapter Not Found"
    
    def get_book_by_chapter_id(self, chapter_id):
        for book in self.all_book_list:
            for chapter in book.chapter_list:
                if chapter.chapter_id == chapter_id:
                    return book
        return "Book Not Found"
    
    # ____________________________________Add to list___________________________________

    def add_reader(self, reader):
        self.__reader_list.append(reader)
        
    def add_writer(self, writer):
        self.__writer_list.append(writer)
        
    def add_payment(self, payment):
        self.__payment_list.append(payment)

    def add_promotion(self, promotion):
        self.__promotion_list.append(promotion)
        
    # ____________________________________Check___________________________________
    
    def check_repeated_pseudonym(self, new_pseudonym):
        for pseudonym in self.all_pseudonym_list:
            if pseudonym.lower() == new_pseudonym.lower():
                return True
        return False
    
    def if_user_not_found(self, user):
        if not (isinstance(user, Reader) or isinstance(user, Writer)):
            return True
        return False
    
    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> UI <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # ____________________________________Search___________________________________
        
    def search_all_list(self, search_str):
        search_book_list = self.search_book_by_name(search_str)
        search_reader_list = self.search_user(search_str).get("Reader")
        search_writer_list = self.search_user(search_str).get("Writer")

        search_dict = {"Book": search_book_list,"Reader": search_reader_list, "Writer": search_writer_list}

        if search_book_list == [] and search_reader_list == [] and search_writer_list == []:
            return "Nothing matches your search"
        return search_dict

    def search_book_by_name(self, book_name):
        search_list=[]
        for book in self.all_book_list:
            if book_name.lower() in book.name.lower():
                search_list.append(book.name)
                
        if search_list==[]:
            return "Not found"
        return search_list

    def search_user(self, username):
        search_reader_list = []
        search_writer_list = []
        for reader in self.__reader_list:
            if username.lower() in reader.username.lower():
                search_reader_list.append(reader.username)
        
        for writer in self.__writer_list:
            if username.lower() in writer.username.lower():
                search_writer_list.append(writer.username)

        if search_reader_list == [] : search_reader_list = "Not Found"
        if search_writer_list == [] : search_writer_list = "Not Found"
        
        return {"Reader" : search_reader_list, "Writer" : search_writer_list} 
        
    def search_coin_promotion(self, code):
        if(code != None):
            for promotion in self.__promotion_list:
                if isinstance(promotion, CoinPromotion) and promotion.code == code:
                    return promotion  
        else: return None
        
    # ____________________________________Financials___________________________________
        
    def buy_coin(self, username, payment, code, golden_amount):
        price = golden_amount
        silver_amount = int(golden_amount * 10 / 100)
        
        user = self.get_user_by_username(username)
        
        coin_promotion = self.search_coin_promotion(code) #redeem code?
        
        if(code != None and coin_promotion != None):
            print("Applying code")
            price = (100 - coin_promotion.discount) / 100 * price #ลดราคา
            
        elif(coin_promotion != None):
                return "Your code is expired or not exist"
        else:
            print("Not applying any code")
            
        self.add_coin_to_user(user, payment, golden_amount, silver_amount, price)

    def add_coin_to_user(self, user, payment, golden_amount, silver_amount, price):
        payment.buy_coin(price)
        date_time = datetime.now()
        user.add_golden_coin(golden_amount)
        user.add_silver_coin(silver_amount)
        user.add_coin_transaction_list(CoinTransaction(payment.name, price, f"+{golden_amount}", f"+{silver_amount}", datetime.today()))
    
    def buy_chapter(self, username, chapter_id):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user

        chapter = self.get_chapter_by_chapter_id(chapter_id)
        if not isinstance(chapter, Chapter): return chapter
        
        if user.check_repeated_purchase(chapter): return "You have already purchased this chapter."
        
        cost = chapter.cost

        coin_balance = user.user_coin_balance

        if coin_balance >= cost:
            user.deduct_coin(cost)
            user.add_chapter_transaction_list(ChapterTransaction(chapter, cost))
            return "Your purchase was successful"
        else:
            return "Not enough coin"
    
    # ____________________________________Create / Add___________________________________

    def sign_up(self,username:str, password:str, birth_date: str, role:str):
        user = self.get_user_by_username(username)
        if not (role.lower() == "reader" or role.lower() == "writer"):
            return "please select Reader or Writer and try again"
        
        if not self.if_user_not_found(user): return "username is already taken"
        
        if role.lower() == "reader":
            self.add_reader(Reader(username, password, birth_date))
            
        elif role.lower() == "writer":
            self.add_writer(Writer(username, password, birth_date))
        
        return "Sign Up Successful"
    
    def create_book(self, name:str, pseudonym:str, writer_name:str, tag_list: str, status: str, age_restricted: bool, prologue: str):
        writer = self.get_user_by_username(writer_name)
        book = self.get_book_by_name(name)
        if isinstance(writer,Writer) and not isinstance(book,Book):
            new_book = Book(name, pseudonym, writer, tag_list, status,age_restricted, prologue)
            writer.add_writing_list(new_book)
            return {"create book successfully" : new_book.show_book_info()}
            #pint returns new_book
        return "please try again"
    
    #return reasons in detail, ไม่ควรสร้าง chapter ที่ n ได้ถ้ายังไม่มี n-1
    def create_chapter(self,book_name,chapter_number, name, context, cost):
        book = self.get_book_by_name(book_name)
        if isinstance(book,Book) and book.is_chapter_valid(chapter_number):
            chapter = Chapter(book_name, chapter_number, name, context, cost)
            book.add_chapter_list(chapter)
            return {"create Chapter successfully" : chapter.show_chapter_info()}
        else : 
            return "please try again"
        
    def create_comment(self, chapter_id, username, context):
        chapter = self.get_chapter_by_chapter_id(chapter_id)
        user = self.get_user_by_username(username)
        if not isinstance(chapter, Chapter): return {"Comment": "please try again"}
        new_comment = Comment(chapter, user, context)
        book = self.get_book_by_chapter_id(chapter_id)
        book.add_comment_list(new_comment)
        chapter.add_comment(new_comment)
        return {"Comment": "create comment success"}
        
    # อันนี้ไว้ทำไรอะ
    # รับ username มาด้วยดีมั้ย แล้วเพิ่มpaymentmethodไว้ในuserแต่ละคน  
    def create_payment_method(self, payment_method_name, payment_info):
        if payment_method_name == self.__payment_list[0]:
            return OnlineBanking(payment_info)
        elif payment_method_name == self.__payment_list[1]:
            return DebitCard(payment_info)
        elif payment_method_name == self.__payment_list[2]:
            return TrueMoneyWallet(payment_info)
        
    def add_pseudonym(self, username, pseudonym):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        if self.check_repeated_pseudonym(pseudonym):
            return "pseudonym already exists"
        user.add_pseudonym(pseudonym)
        return "pseudonym added"
        
    # ____________________________________Edit / Change___________________________________
            
    def edit_book_info(self, old_name, new_name, pseudonym, add_tag_list, delete_tag_list, status, age_restricted, prologue):
        book = self.get_book_by_name(old_name)
        #เขียนดักไม่ให้ช้ำ
        if new_name:
            book.name = new_name
        #เขียนดักให้เพิ่ม pseudonym ก่อนถึงจะใช้ได้ หรือ เพิ่ม pseudonym เข้าลิสต์หลังใช้ new_pseudonym
        if pseudonym:
            book.pseudonym = pseudonym
        if add_tag_list:
            book.add_tag(add_tag_list)
        if delete_tag_list:
            book.delete_tag(delete_tag_list)
        if status:
            book.status = status
        if age_restricted != book.age_restricted:
            book.age_restricted = age_restricted
        if prologue:
            book.prologue = prologue
        # book.date_time(0) #last edit
        return {"Book updated" : book.show_book_info()}
            
    def edit_chapter_info(self,chapter_id, name, context, cost):
        chapter = self.get_chapter_by_chapter_id(chapter_id)
        if not isinstance(chapter, Chapter): return chapter
        if name:
            chapter.update_name(name)
        if context:
            chapter.update_context(context)
        if cost:
            chapter.update_cost(cost)
        # chapter.publish_date_time(0) #last edit
        return {"Chapter updated" : chapter.show_chapter_info()}
    
    def change_password(self, username, old_password, new_password):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        if user.password == old_password and len(new_password) >= 8:
            user.password = new_password
            return "Password has been changed"
        elif user.password != old_password:
            return "Wrong password"
        elif len(new_password) < 8:
            return "Password must be at least 8 letters"
        else:
            return "Please try again"
        
    def change_display_name(self, username, new_display_name):
        user = self.get_user_by_username(username)
        user.display_name = new_display_name
        return "display name has been changed"
    
    # ____________________________________Show / View____________________________________
    
    def show_coin(self, username):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        return {"Golden Coin" : user.golden_coin.balance, "Silver Coin" : user.silver_coin_balance}
    
    def show_my_page(self, username):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        
        writing_count = "0"
        reads = "0"
        writing_list = [] # "Create your first writing"
        pseudonym_list = [] # "Pseudonym Not Found"
        comment_list = [] # "Add comment"
            
        if isinstance(user, Writer):
            writing_count = len(user.writing_list)
            reads = user.viewer_count
            writing_list = user.show_writing_name_list()
            pseudonym_list = user.pseudonym_list
            comment_list = user.show_comment_list()
        
        return {"display_name" : user.display_name,
                "username" : user.username,
                "introduction" : user.introduction,
                "writing_count" : writing_count,
                "book_on_shelf_count" : len(user.book_shelf_list),
                "followers" : len(user.follower_list),
                "read_count" : len(user.recent_read_chapter_list),
                "viewer_count" : reads,
                "writings" : writing_list,
                "pseudonyms" : pseudonym_list,
                "comments" : comment_list}
    
    def show_my_profile(self, username):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        return {"display_name" : user.display_name,
                "username" : user.username,
                "password" : "******",
                "menu" : ["change password",
                            "go to page",
                            "upgrade to writer",
                            "pseudonym",
                            "verify age"]}
        
    def show_my_reading(self, username):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return user
        reading_list = []
        for book in user.book_shelf_list:
            reading_list.append(book.show_book_info())
        return reading_list
    
    def view_chapter(self, chapter_id):
        chapter = self.get_chapter_by_chapter_id(chapter_id)
        return chapter.show_chapter_info()
    
    def view_book(self, book_name):
        book = self.get_book_by_name(book_name)
        return book.show_book_info()
    
    def create_report(reporter_username: str, content: str, content_id: int, report_type: str, additional_info: str = ""):
        content = Reader.get_content_by_id(content_id)

        if content:
            report = {
                "report_type": report_type,
                "content": content,
                "content_id": content_id,
                "reporter_username": reporter_username,
                "additional_info": additional_info
            }
            Reader.add_report(report)

            return {"User": "Report created successfully."}
        else:
            return {"User": "Content not found."}

    
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
    
    # ____________________________________others___________________________________    
    
    def sign_in(self, username, password):
        user = self.get_user_by_username(username)
        if self.if_user_not_found(user): return "username doesn't exist"
        if user.password == password:
            return "log in successfully"
        return "wrong password"
    
    # ____________________________________Error____________________________________
    
    # def counting_report(self, book):
    #     for report_type in self.__report_type_list:
    #         if book.counting_report_from_type(report_type) in self.__report_type_list:
    #             #send to web master
    #             book.status = "hiding"
    #             return f"your book has been reported 10 times in {report_type}"