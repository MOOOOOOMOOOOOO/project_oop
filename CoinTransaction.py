class CoinTransaction:
    def __init__(self, payment, price, golden_coin_amount, silver_coin_amount, date_time):
        self.__payment = payment
        self.__price = price
        self.__golden_amount = golden_coin_amount
        self.__silver_amount = silver_coin_amount
        self.__date_time = date_time
        
    #=======================================
    
    @property
    def payment(self):
        return self.__payment
    
    @property
    def price(self):
        return self.__price
    
    @property
    def golden_amount(self):
        return self.__golden_amount
    
    @property
    def silver_amount(self):
        return self.__silver_amount
    
    @property
    def date_time(self):
        return self.__date_time
    
    @property
    def date_time_str(self):
        return self.__date_time.strftime("%x %X")