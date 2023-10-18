class Employee:
    def __init__(self, name, commission = None):
        self.name = name
        self.commission = commission

    def get_pay(self):
        pass

    def __str__(self):
        pass

class SalaryContract(Employee):
    def __init__(self, name, salary, commission):
        super().__init__(name, commission)
        self.salary = salary

    def get_pay(self):
        return self.salary + self.commission.get_commission() if self.commission else self.salary

    def __str__(self):
        commission_info = self.commission.get_string() if self.commission else ""
        return f"{self.name} works on a monthly salary of {self.salary}{commission_info}. Their total pay is {self.get_pay()}."

class HourlyContract(Employee):
    def __init__(self, name, hours, hourly, commission):
        super().__init__(name, commission)
        self.hours = hours
        self.hourly = hourly

    def get_pay(self):
        return self.hours * self.hourly + self.commission.get_commission() if self.commission else self.hours * self.hourly

    def __str__(self):
        commission_info = self.commission.get_string() if self.commission else ""
        return f"{self.name} works on a contract of {self.hours} hours at {self.hourly}/hour{commission_info}. Their total pay is {self.get_pay()}."


class Commission:
    def get_commission(self):
        pass

    def get_string(self):
        pass

class FixedBonus(Commission):
    def __init__(self, fixed_bonus):
        self.fixed_bonus = fixed_bonus

    def get_commission(self):
        return self.fixed_bonus

    def get_string(self):
        return f' and receives a bonus commission of {self.fixed_bonus}'

class UnfixedBonus(Commission):
    def __init__(self, no_contracts, per_contract):
        self.no_contracts = no_contracts
        self.per_contract = per_contract

    def get_commission(self):
        return self.no_contracts * self.per_contract

    def get_string(self):
        return f' and receives a commission for {self.no_contracts} contract(s) at {self.per_contract}/contract'

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryContract('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyContract('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryContract('Renee', 3000, UnfixedBonus(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyContract('Jan', 150, 25, UnfixedBonus(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryContract('Robbie', 2000, FixedBonus(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyContract('Ariel', 120, 30, FixedBonus(600))

