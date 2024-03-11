from typing import Union, Optional, Annotated
import uvicorn
from fastapi import FastAPI, Query, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import json
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from pathlib import Path

from datetime import datetime, timedelta
from Controller import Controller
from Reader import Reader, Writer
from Book import Book
from Chapter import Chapter
from Payment import PaymentMethod, OnlineBanking, TrueMoneyWallet
from CoinTransaction import CoinTransaction
from Promotion import BookPromotion, CoinPromotion, Promotion
from Coin import GoldenCoin, SilverCoin

app = FastAPI()

templates = Jinja2Templates(directory="Templates")
app.mount("/Templates", StaticFiles(directory="Templates"), name="templates")

write_a_read = Controller()

if __name__ == "__main__":
     uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

now = datetime.now()

#uvicorn main:app --reload

#----------------------------------create users----------------------------------
#WriteARead.add_reader(Reader("username", "password", "dd/mm/yyyy"))
     
Mo = Writer("Mozaza", "12345678", "12/05/2000")
write_a_read.add_reader(Mo)
write_a_read.add_reader(Reader("Pinttttt", "sawasdee", "01/01/2005"))
write_a_read.add_reader(Reader("Pangrum", "ehehe", "02/01/2005"))
write_a_read.add_reader(Reader("Jueeen", "whippedcream", "12/11/2004"))

write_a_read.add_writer(Mo)

#----------------------------------create books----------------------------------
# Book("name", writer, [tag_list], "publishing/hiding", age_restricted, "prologue", "dd/mm/yyyy"):

shin_chan_prologue = "Shin Chan is a 50-year-old boy"

book1 = Book("Shin_chan", "Mola", Mo, ["kids", "comedy","crime"], "publishing", 7, shin_chan_prologue)
Mo.add_writing_list(book1)

book2 = Book("Shinosuke", "Mola", Mo, ["kids", "comedy","crime"], "publishing", 7, shin_chan_prologue)
Mo.add_writing_list(book2)


#----------------------------------create chapters----------------------------------
#Chapter("number", "name", "context", "dd/mm/yyyy", price)

book1.add_chapter_list(Chapter("Shin_chan", "1", "first_ch", "this is the first chapter of shincha", 184))

#----------------------------------create promotions----------------------------------
#BookPromotion("dd/mm/yyyy", discount, [book_list])
#CoinPromotion("dd/mm/yyyy", discount, "code")


book_sale = BookPromotion("01/01/2021",50, [])
write_a_read.add_promotion(book_sale)

free_coin = CoinPromotion("01/01/2021",40, "chakeawaroi")
write_a_read.add_promotion(free_coin)

#----------------------------------create transactions----------------------------------

Mo.add_coin_transaction_list(CoinTransaction(OnlineBanking("012-3-45678-9"), 100, 100, 10, now))
Mo.add_coin_transaction_list(CoinTransaction(TrueMoneyWallet("0123456789"), 200, 200, 20, now))

#----------------------------------add coin----------------------------------
Mo.add_silver_coin(20)
Mo.add_silver_coin(10)
Mo.add_silver_coin(50)
Mo.add_silver_coin(3)
Mo.add_silver_coin(100)
Mo.add_golden_coin(888)

#----------------------------------add to bookshelf----------------------------------
Mo.add_book_shelf_list(book1)
Mo.add_book_shelf_list(book2)
# ____________________________________FastAPI___________________________________
# _________________________________________________ GET _________________________________________________

# @app.get("/")
# def FirstPage(req: Request):
#      return template.TemplateResponse(name="index.html", context={"request":req})

@app.get("/bookname", tags=['search bar'])
def searchBook(book_name:str):
     return {"Book": write_a_read.search_book_by_name(book_name)}

@app.get("/username", tags=['search bar'])
def SearchUser(username:str):
     return {"user": write_a_read.search_user(username)}

@app.get("/coin", tags=['coin'])
def MyCoin(username:str):
     return write_a_read.show_coin(username)

@app.get("/silver_coin", tags=['coin'])
def ShowSilverCoins(username:str):
     user = write_a_read.get_user_by_username(username)
     return {"Silver_Coin" :user.show_silver_coin_list()}

@app.get("/my_page", tags=['My Page'])
def ShowMyPage(username:str):
     return {"My Page" : write_a_read.show_my_page(username)}

@app.get("/my_profile", tags=['My Profile'])
def ShowMyProfile(username:str):
     return {"My Profile" : write_a_read.show_my_profile(username)}

@app.get("/get_coin_transaction", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
     user = write_a_read.get_user_by_username(username)
     return {"Coin Transaction" : user.show_coin_transaction()}

@app.get("/show_chapter_transaction", tags=['Chapter Transaction'])
def ShowChapterTransaction(username:str):
     user = write_a_read.get_user_by_username(username)
     if write_a_read.if_user_not_found(user): return user
     return {"Chapter Transaction" : user.show_chapter_transaction()}

@app.get("/my_reading", tags=['My Reading'])
def ShowMyReading(username:str):
     return {"My Reading" : write_a_read.show_my_reading(username)}

@app.get("/test", tags=['test'])
def Test(book_name:str):
     return {write_a_read.get_book_by_name(book_name)}

@app.get("/sign_in", tags=['sign up/sign in'])
def SignIN(username:str, password:str):
     return write_a_read.sign_in(username, password)

@app.get("/search_all/{search_str}", tags=['search bar'])
def searchBar(search_str:str):
     return {"Search": write_a_read.search_all_list(search_str)}

@app.get('/', response_class=HTMLResponse)
def main(request: Request):
     return templates.TemplateResponse('index.html', {'request': request})

# _________________________________________________ POST _________________________________________________

class dto_sign_up(BaseModel):
     username:str
     password:str
     birth_date: str
     role: str

@app.post("/sign_up", tags=['sign up/sign in'])
def SignUp(dto : dto_sign_up):
     return write_a_read.sign_up(dto.username, dto.password, dto.birth_date, dto.role)

#..........................................................................................................

class dto_add_pseudonym(BaseModel):
     username : str
     new_pseudonym : str


@app.post("/my_profile/psedonym", tags=["My Profile"])
def AddPseudonym(dto : dto_add_pseudonym):
     return {"Add Pseudonym" : write_a_read.add_pseudonym(dto.username, dto.new_pseudonym)}

#..........................................................................................................

class dto_buy_chapter(BaseModel):
     username : str
     chapter_id : str

@app.post("/buy_chapter", tags=['chapter'])
def BuyChapter(dto : dto_buy_chapter):
     return {"Buy Chapter" : write_a_read.buy_chapter(dto.username, dto.chapter_id)}

#..........................................................................................................

class dto_create_book(BaseModel):
     name:str
     writer_name:str
     tag_list: str
     prologue: str
     age_restricted: bool
     status: str 
     
@app.post("/book", tags=['Book'])
def CreateBook(dto : dto_create_book):
     return write_a_read.create_book(dto.name, dto.writer_name, dto.tag_list, dto.status, dto.age_restricted, dto.prologue)

#..........................................................................................................

class dto_create_chapter(BaseModel):
     book_name:str
     chapter_number:int
     name:str
     context: str
     cost : int
     
@app.post("/chapter", tags=['Chapter'])
def CreateChapter(dto : dto_create_chapter):
     return write_a_read.create_chapter(dto.book_name, dto.chapter_number, dto.name, dto.context, dto.cost)

#..........................................................................................................

class dto_create_comment(BaseModel):
     chapter_id : str
     username : str
     context : str
     
@app.post("/comment", tags=['Comment'])
def CreateComment(dto: dto_create_comment):
     return write_a_read.create_comment(dto.chapter_id, dto.username, dto.context)

#..........................................................................................................

class dto_buy_coin(BaseModel):
     username:str
     golden_coin_amount:int
     payment_info: str
     payment_method:str 
     code: Optional[str]
     
@app.post("/buy_coin", tags=['Coin'])
def buy_coin(dto : dto_buy_coin):
     payment = write_a_read.create_payment_method(dto.payment_method, dto.payment_info)
     write_a_read.buy_coin(dto.username, payment, dto.code, dto.golden_coin_amount)  
     return "Purchase successful, THANK YOU"

# _________________________________________________ PUT _________________________________________________

class dto_edit_introduction(BaseModel):
     username : str
     text : str

@app.put("/my_page/edit_introduction", tags=["My Page"])
def EditIntroduction(dto : dto_edit_introduction):
     user = write_a_read.get_user_by_username(dto.username)
     return {"Edit Introduction" : user.edit_introduction(dto.text)}

# #..........................................................................................................

class dto_change_password(BaseModel):
     username : str
     old_password :str
     new_password : str

@app.put("/my_profile/change_password", tags=['My Profile'])
def ChangePassword(dto : dto_change_password):
     return {"Change Password" : write_a_read.change_password(dto.username, dto.old_password, dto.new_password)}

#..........................................................................................................

class dto_change_display_name(BaseModel):
     username : str
     new_display_name : str


@app.put("/my_page/change_display_name", tags=['My Page'])
def ChangeDisplayName(dto : dto_change_display_name):
     return {"Change Display Name" : write_a_read.change_display_name(dto.username, dto.new_display_name)}

#..........................................................................................................

class dto_edit_book(BaseModel):
     old_name : str = None
     new_name : str = None
     add_tag_list: list = None
     delete_tag_list: list = None
     prologue: str = None
     age_restricted: bool = None
     status: str = None
     
@app.put("/edit_book", tags=['Book'])
def EditBookInfo(dto : dto_edit_book):
     book =  write_a_read.edit_book_info(dto.old_name,dto.new_name,dto.add_tag_list,dto.delete_tag_list,dto.status,dto.age_restricted,dto.prologue)
     if isinstance(book,Book):
          return book
     else:
          return {"error": "Book not found"}
     
#..........................................................................................................

class dto_edit_chapter(BaseModel):
     chapter_id : str = None
     name : str = None
     context : str = None
     cost : int = None
     
@app.put("/edit_chapter", tags=['Chapter'])
def EditChapterInfo(dto : dto_edit_chapter):
     chapter =  write_a_read.edit_chapter_info(dto.chapter_id, dto.name, dto.context, dto.cost)
     if isinstance(chapter,Chapter):
          return chapter
     else:
          return {"error": "Book not found"}
     
# _________________________________________________ TEST _________________________________________________
# mo_username = "Mozaza"
# mo_password = "namchakeawpun"

# print("________________________________________________sign in_______________________________________________")
# print(write_a_read.sign_in("Mozaza", "12345678"))

# print("_______________________________________________sign up_______________________________________________")
# print(write_a_read.sign_up("reader1", "12345678", "01/01/2000", "reader"))
# print(write_a_read.sign_up("writer1", "12345678", "01/01/2000", "reader"))

print("_______________________________________________search all_______________________________________________")
print(write_a_read.search_all_list("mo"))

# print("_______________________________________________My Page_______________________________________________")
# print(write_a_read.show_my_page("Mozaza"))

# print("_______________________________________________My Page____________________________________")
# print(write_a_read.show_my_profile("Mozaza"))

# print("_______________________________________________My Reading_______________________________________________")
# print(write_a_read.show_my_reading("Mozaza"))

# print("_______________________________________________Create Book_______________________________________________")
# print(write_a_read.create_book("SAO", "Mola", "Mozaza", ["romance", "anime"], "publishing", True, "Kirito<3Asuna"))

# print("_______________________________________________Edit Book_______________________________________________")
# print("----------Edit everything-----------")
# print(write_a_read.edit_book_info("SAO", "Shinnosuke", "lala", ["kids", "comedy"], [], "hiding", False, "edited"))
# print("----------Edit tags-----------")
# print(write_a_read.edit_book_info("Shinnosuke", "Shinnosuke", "lala", ["family"], ["romance"], "hiding", False, "edited"))

# print("_______________________________________________Creat Chapter_______________________________________________")
# print(write_a_read.create_chapter("Shin_chan", "10", "second", "hihi", 50))

# print("_______________________________________________Edit Chapter_______________________________________________")
# print(write_a_read.edit_chapter_info("Shin_chan/10", "edited_name", "this is edited version", 99))


# print("_______________________________________________Add Comment_______________________________________________")
# print(write_a_read.create_comment("Shin_chan/1", "Mozaza", "this is amazing"))

# print("_______________________________________________View Chapter_______________________________________________\n")
# print(write_a_read.view_chapter("Shin_chan/1"))

# print("_______________________________________________View Book_______________________________________________\n")
# print(write_a_read.view_book("Shin_chan"))

# print("_______________________________________________Creat Chapter_______________________________________________")
# print(MyCoin("Mozaza"))

#________________________________________Error________________________________________
# print("_______________________________________________Buy Coin_______________________________________________")
# print(write_a_read.buy_coin("Mozaza", OnlineBanking, "chakeawaroi", 100))


