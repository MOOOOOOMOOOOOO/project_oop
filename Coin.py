from datetime import datetime, date, timedelta

class GoldenCoin:
    def __init__(self,balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,new_balance):
        self.__balance = new_balance

    def deduct_golden_coin(self,amount):
        self.__balance -= amount
        return amount

    def add_golden_coin(self,amount):
        self.balance += amount

class SilverCoin(GoldenCoin):
    def __init__(self, balance):
        super().__init__(balance)
        self.__exp_date_time = (datetime.today() + timedelta(days=10))

    @property
    def exp_date_time(self):
        return self.__exp_date_time
    
    @property
    def exp_date_time_str(self):
        return self.__exp_date_time.strftime("%x")

    def deduct_silver_coin(self, amount):
        silver_coin_amount = self.balance
        if amount >= silver_coin_amount:
            amount -= silver_coin_amount
            self.balance = 0
            return silver_coin_amount
        else:
            self.balance -= amount
            return amount