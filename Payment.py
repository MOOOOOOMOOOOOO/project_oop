import Controller as Controller

class Payment:
    def __init__(self):
        self.__coin_promotion = []
    #=================================
    @property
    def coin_promotion(self):
        return self.__coin_promotion
    #=================================method   
    def buy_coin(self, price):
        pass
    

class OnlineBanking(Payment):
    def __init__(self, account_id):
        self.__name = 'OnlineBanking'
        self.__account_id = account_id
    #==================================
    @property
    def name(self):
        return self.__name
    @property
    def account_id(self):
        return self.__account_id
    #==================================method
    def buy_coin(self, price):
        print("The system is implemented Please wait for the confirmation of the service")
        print(f"The system is sending a bill to account number {self.__account_id} total {price} baht")
        print("Purchase successful, THANK YOU")
        
    
    
class DebitCard(Payment):
    def __init__(self, card_id, exp_date, cvv):
        self.__name = 'Debit Card'
        self.__card_id = card_id
        self.__exp_date = exp_date
        self.__cvv = cvv
    #==================================
    @property
    def name(self):
        return self.__name
    @property
    def card_id(self):
        return self.__card_id
    @property
    def card_id(self):
        return self.__card_id
    @property
    def card_id(self):
        return self.__card_id
    #==================================method
    def buy_coin(self, price):
        print("The system is implemented Please wait for the confirmation of the service")
        print(f"The system will deduct money from the card number {self.__card_id} total {price} baht")
        print("Purchase successful, THANK YOU")
    

class TrueMoneyWallet(Payment):
    def __init__(self, phone_number, otp_number):
        self.__name = 'TrueMoney Wallet'
        self.__phone_number = phone_number
        self.__otp_number = otp_number
    #==================================
    @property
    def name(self):
        return self.__name
    @property
    def phone_number(self):
        return self.__phone_number
    @property
    def otp_number(self):
        return self.__otp_number
    #==================================method
    def buy_coin(self, price):
        print("The system is implemented Please wait for the confirmation of the service")
        print(f"Total {price}")
        print(f"An otp number will be sent to phone number {self.__phone_number} in a moment")
        print(f"Your otp number : {self.__otp_number}")
        print("Purchase successful, THANK YOU")