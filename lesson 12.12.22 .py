#C:\Users\mahal\AppData\Roaming\JetBrains\PyCharmCE2022.2\scratches\Map_filters.py

my_car = {
    'manufacturer': 'Mazda',
    'model': '3',
    'color': 'white',
    'license_plate': '1234567',
    'year': 2015,
    'fuel': 50,
    'km': 102000,
    'fuel_consumption': 20
}

def add_fuel(car: dict, liters):
    car['fuel'] += liters

def drive(car, km):
    car['km'] += km
   # update fuel


car = {}
car['manufacturer'] = 'Mazda'


class Car:
    def __init__(self, man: str, mod: str, col, year,
                 fuel_consumption, tank_capacity):
        self.manufacturer = man
        self.model = mod
        self.color = col
        self.year = year
        # liters per 100 km
        self.fuel_consumption = fuel_consumption
        self.tank_capacity = tank_capacity

        self.km = 0
        self.fuel = 0

    def __str__(self):
        return f"{self.manufacturer} {self.model} {self.color}"

    def fill_tank(self, liters) -> bool:
        if 0 < liters <= self.tank_capacity - self.fuel:
            self.fuel += liters
            return True
        return False

    def drive(self, km) -> bool:
        if km > 0 and (self.fuel * (100/self.fuel_consumption)) >= km:
            self.km += km
            self.fuel -= (self.fuel_consumption/100) * km
            return True
        return False

if __name__ == '__main__':
    car_mazda = Car('Mazda', '3', 'white', 2015, 20, 50)
    ret_val = car_mazda.drive(100)
    print(ret_val)
    car_mazda.fill_tank(10)
    ret_val = car_mazda.drive(15)
    print(ret_val)


car_mazda = Car('Mazda', '3', 'white', 2015, 20, 50)

#car_mazda = Car.__init__(None, 'Mazda', '3')
car_toyota = Car('Toyota', 'Yaris', 'red', 2022, 10, 35)
car_mazda.drive()

ret_val = car_mazda.fill_tank(30)
print(f"retval is: {ret_val}, new fuel is mazda: {car_mazda.fuel}")
print(f"new fuel is toyota: {car_toyota.fuel}")
ret_val = car_mazda.fill_tank(40)
print(f"retval is: {ret_val}, new fuel is mazda: {car_mazda.fuel}")

print(isinstance(car_mazda, Car))
print(car_mazda)

ret_val = car_mazda.__str__()
print(ret_val)

print(car_mazda)

Car.fill_tank(car_mazda, 10)

#fill tank
car_mazda.fuel += 50

l1 = list([3,4,5])
print(l1)
print(isinstance(l1, Car))
l2 = list([5,6,78])

print("type of l1:", type(l1))
print("type of mazda_car: ", type(car_mazda))

car_mazda.color = 'yellow'
print(car_mazda.color)


car = {}

car1 = Car()
car1 = Car("Mazda", "3", "white")
print(type(car1))
s1 = set([2,3,4,4])
l1 = list()
str1 = str()

#############################################

# from lesson10.car import Car


def test_negative_values():
    car = Car("Lamborgini", "Diablo", "yellow", 2020, 20, 45)
    km_before = car.km
    ret_val = car.drive(-90)
    assert not ret_val, "Can't insert negative km"
    assert km_before == car.km, "km was changed when received negative km"

def test_correct_fuel_calculation():
    car = Car("Lamborgini", "Diablo", "yellow", 2020, 20, 45)
    assert car.fill_tank(30)
    assert car.fuel == 30
    assert car.drive(100)
    assert car.fuel == 10

if __name__ == '__main__':
    test_negative_values()
    test_correct_fuel_calculation()

##############################___bank_account___############################

class BankAccount:

    def __init__(self, bank_name: str, branch: str, account_num: int, account_holder: dict,
                 usd_allowed: bool = False, credit_limit: float=0):

        self.bank_name: str = bank_name
        self.branch: str = branch
        self.account_num: int = account_num
        self.holders: dict = account_holder
        # self.__bank_name: str = bank_name
        # self.__branch: str = branch
        # self.__account_num: int = account_num
        # self.__holder: dict = account_holder

        self.nis_balance: float = 0
        self.usd_balance: float = 0
        # self.__nis_balance: float = 0
        # self.__usd_balance: float = 0

        self.usd_allowed: bool = usd_allowed
        self.nis_credit_limit: float = credit_limit
        # self.__usd_allowed: bool = usd_allowed
        # self.__nis_credit_limit: float = credit_limit

        self.transactions: dict[str, list] = {}

    def get_bank_name(self):
        return self.bank_name

    def get_branch(self):
        return self.__branch

    def set_branch(self, name):
        self.__branch = name

    def get_balance(self):
        return {'nis': self.nis_balance,
                'usd': self.usd_balance}

    def get_account_num(self):
        return self.account_num

    def get_holder(self):
        return self.holder

    def set_holder_address(self, address):
        self.holder['address'] = address

        self.transactions: dict[str, list] = {}

    def __str__(self):
        return f"Account {self.account_num}"

    @staticmethod
    def _valid_params(amnt, currency):
        return amnt > 0 and currency in ('nis', 'usd')

    def _add_transaction(self, transaction_date: str, transaction_type: str):

        # add new dictionary key if needed
        if transaction_date not in self.transactions:
            self.transactions[transaction_date] = []

        # if we are here, we are sure that the key already exists
        self.transactions[transaction_date].append(transaction_type)

    def withdraw(self, date: str, amount: float, currency: str = 'nis') -> bool:

        if not self._valid_params(amount, currency):
            return False

        if currency == 'nis':
            if self.nis_balance - amount >= (self.nis_credit_limit * -1):
                self.nis_balance -= amount
            else:
                return False
        else:
            if self.usd_allowed and self.usd_balance >= amount:
                self.usd_balance -= amount
            else:
                return False
        self._add_transaction(date, 'withdraw')
        return True

    def deposit(self, date, amount: float, currency: str = 'nis'):
        if not self._valid_params(amount, currency):
            return False

        if currency == 'nis':
            self.nis_balance += amount
            self._add_transaction(date, 'deposit')
            return True
        else:
            if not self.usd_allowed:
                return False
            else:
                self._add_transaction(date, 'deposit')
                self.usd_balance += amount
                return True

    def convert_to_usd(self, date, nis_amnt, nis2usd_exchange_rate):
        if nis_amnt < 0:
            return False
        if not self.usd_allowed or self.nis_balance - nis_amnt < (self.nis_credit_limit * -1):
            return False
        self.nis_balance -= nis_amnt
        self.usd_balance += nis_amnt * nis2usd_exchange_rate
        self._add_transaction(date, 'convert_to_usd')
        return True

    def convert_to_nis(self, date, usd_amnt, usd2nis_exchange_rate):
        if usd_amnt < 0:
            return False
        if not self.usd_allowed or self.usd_balance < usd_amnt:
            return False
        self.nis_balance += usd_amnt * usd2nis_exchange_rate
        self.usd_balance -= usd_amnt
        self._add_transaction(date, 'convert_to_nis')
        return True

    def get_current_balance(self) -> tuple[float, float]:
        return self.nis_balance, self.usd_balance

    def get_transactions_per_date(self, date: str) -> list[str]:
        return self.transactions.get(date, [])

if __name__ == '__main__':
    # create bank account
    account1 = BankAccount('Discount', 'Kiryat Hasharon', 12345,
                           {"id": "123345",
                            "name": "Valeria",
                            "address": "Netanya"},
                           usd_allowed=True, credit_limit=10_000)
    print(f"Current balance for {account1}: {account1.get_current_balance()}")

    print("Trying to withdraw 10500 shekels passing the limit - should fail!")
    result = account1.withdraw("11-12-2022", 10500)
    print(f"Result: {result}")

    print("Trying to withdraw 9500 shekels in the range of limit - should succeed!")
    result = account1.withdraw("11-22-2022", 9500)
    print(f"Result: {result}")

    print(f"Current balance: {account1.get_current_balance()}")

    print("Trying to convert 1000 shekels to USD - outside the limit, should fail")
    result = account1.convert_to_usd("12-22-2022", 1000, 3.5)
    print(f"Result: {result}")

    print("Deposit 20_000 to account - should succeed")
    result = account1.deposit("12-22-2022", 20000)
    print(f"Result: {result}")

    print("Deposit $5_000 to account - should succeed")
    result = account1.deposit("12-22-2022", 5000, currency='usd')
    print(f"Result: {result}")

    print(f"New balance: {account1.get_current_balance()}")
    print(f"Transactions on 11-22-2022: {account1.get_transactions_per_date('11-22-2022')}")
    print(f"Transactions on 12-22-2022: {account1.get_transactions_per_date('12-22-2022')}")