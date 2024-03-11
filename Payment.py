import Controller as Controller

class PaymentMethod:
    def __init__(self):
        self.__name = "hi"
    #=================================
    @property
    def name(self):
        return self.__name
    #=================================method   
    def buy_coin(self, price):
        pass
    
    # def add_coin_promotion(self, new_coin_promotion):
    #     self.__coin_promotion.append(new_coin_promotion)

class OnlineBanking(PaymentMethod):
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
        # print("Purchase successful, THANK YOU")
    
class DebitCard(PaymentMethod):
    def __init__(self, card_id):
        self.__name = 'Debit Card'
        self.__card_id = card_id
    #==================================
    @property
    def name(self):
        return self.__name
    @property
    def card_id(self):
        return self.__card_id
    #==================================method
    def buy_coin(self, price):
        print("The system is implemented Please wait for the confirmation of the service")
        print(f"The system will deduct money from the card number {self.__card_id} total {price} baht")
        # print("Purchase successful, THANK YOU")
    

class TrueMoneyWallet(PaymentMethod):
    def __init__(self, phone_number):
        self.__name = 'TrueMoney Wallet'
        self.__phone_number = phone_number
    #==================================
    @property
    def name(self):
        return self.__name
    @property
    def phone_number(self):
        return self.__phone_number
    #==================================method
    def buy_coin(self, price):
        print("The system is implemented Please wait for the confirmation of the service")
        print(f"Total {price} baht")
        print(f"An bill will be sent to phone number {self.__phone_number} in a moment")
        # print("Purchase successful, THANK YOU")