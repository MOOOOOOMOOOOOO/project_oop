from typing import Union
import uvicorn
from fastapi import FastAPI
import json
from datetime import datetime, timedelta

from Controller import Controller
from Reader import Reader, Writer
from Book import Book
from Chapter import Chapter
from Payment import Payment, OnlineBanking, TrueMoneyWallet
from CoinTransaction import CoinTransaction
from Promotion import BookPromotion, CoinPromotion, Promotion

app = FastAPI()

WriteARead = Controller()


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

now = datetime.now()

# uvicorn main:app --reload

# ----------------------------------create users----------------------------------
# WriteARead.add_reader(Reader("username", "password", "dd/mm/yyyy"))

Mo = Writer("Mozaza", "namchakeawpun", "12/05/2000")
WriteARead.add_reader(Mo)
WriteARead.add_reader(Reader("Pinttttt", "sawasdee", "01/01/2005"))
WriteARead.add_reader(Reader("Pangrum", "ehehe", "02/01/2005"))
WriteARead.add_reader(Reader("Jueeen", "whippedcream", "12/11/2004"))

WriteARead.add_writer(Mo)

# ----------------------------------create books----------------------------------
# Book("name", writer, [tag_list], "publishing/hiding", age_restricted, "prologue", "dd/mm/yyyy"):

shin_chan_prologue = "Shin Chan is a 50-year-old boy"

Book1 = Book("Shin_chan", Mo, ["kids", "comedy", "crime"], "publishing", 7, shin_chan_prologue, "01/01/2020")
Mo.add_writing_book_list(Book1)

Book2 = Book("Shinosuke", Mo, ["kids", "comedy", "crime"], "publishing", 7, shin_chan_prologue, "01/01/2020")
Mo.add_writing_book_list(Book2)


# ----------------------------------create chapters----------------------------------
# Chapter("number", "name", "context", "dd/mm/yyyy", price)

Chapter1_1 = Chapter("1", "first chapter of shinchan", "this is the first chapter of shinchan", "01/01/2020", 5)


# ----------------------------------create promotions----------------------------------
# BookPromotion("dd/mm/yyyy", discount, [book_list])
# CoinPromotion("dd/mm/yyyy", discount, "code")


book_sale = BookPromotion("01/01/2021", 50, [])
WriteARead.add_promotion(book_sale)

free_coin = CoinPromotion("01/01/2021", 40, "chakeawaroi")
WriteARead.add_promotion(free_coin)

# ----------------------------------create transactions----------------------------------

Mo.add_coin_transaction_list(
    CoinTransaction(OnlineBanking("012-3-45678-9"), 100, [100, 10], now.strftime("%d/%m/%Y, %H:%M:%S")))
Mo.add_coin_transaction_list(
    CoinTransaction(TrueMoneyWallet("0123456789", "5174"), 200, [200, 20], now.strftime("%d/%m/%Y, %H:%M:%S")))

# ----------------------------------fastapi----------------------------------

@app.get("/")
def FirstPage():
    return "Welcome to WriteARead"


@app.get("/bookname", tags=['search bar'])
def SearchBook(book_name: str):
    return {"Book": WriteARead.search_book_by_name(book_name)}


@app.get("/username", tags=['search bar'])
def SearchUser(username: str):
    return {"user": WriteARead.search_user(username)}


@app.get("/coin", tags=['coin'])
def ShowCoins(username: str):
    return WriteARead.show_coin(username)


@app.post("/signup", tags=['sign up/sign in'])
def SignUp(username: str, password: str, birth_date: str):
    return WriteARead.sign_up(username, password, birth_date)


@app.get("/My Page", tags=['user'])
def ShowMyPage(username: str):
    return f"My Page : {WriteARead.show_my_page(username)}"


@app.get("/My Profile", tags=['user'])
def ShowMyProfile(username: str):
    return f"My Profile : {WriteARead.show_my_profile(username)}"

@app.get("/Writing Name List", tags=['user'])
def ShowWritingNameList(username: str):
    user = WriteARead.get_user_by_username(username)
    if isinstance(user, Writer):
        return {"Writing Name List": user.show_writing_name_list()}
    else:
        return {"error": "No books found."}
    
# from fastapi import HTTPException

# @app.post("/upgrade_to_writer", tags=['user'])
# def upgrade_to_writer(username: str):
#     user = WriteARead.get_user_by_username(username)
#     if isinstance(user, Writer):
#         return {"message": "User is already a writer."}
#     else:
#         WriteARead.add_writer(user)
#         return {"message": "User upgraded to writer successfully."}


@app.get("/get_coin_transacttion", tags=['Coin Transaction'])
def get_coin_transaction(username: str):
    user = WriteARead.get_user_by_username(username)
    return {"Coin Transaction": user.show_coin_transaction()}


# ----------------------------------test----------------------------------

# @app.get("/My Writing", tags=['user'])
# def ShowMyWriting(username: str):
#     return {"My Writing": WriteARead.show_my_writing(username)}

