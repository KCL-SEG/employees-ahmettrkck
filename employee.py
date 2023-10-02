"""Employee pay calculator."""

class Employee:
    def __init__(self, name, salary_rate=None, hourly_rate=None, hours=None, bonus_commision=None, contract_commision=None, contract_commision_rate=None):
        self.name = name
        self.salary_rate = salary_rate
        self.hourly_rate = hourly_rate
        self.hours = hours
        self.bonus_commision = bonus_commision
        self.contract_commision = contract_commision
        self.contract_commision_rate = contract_commision_rate

    def get_pay(self):
        total_pay = 0
        if self.salary_rate:
            total_pay+= self.salary_rate
        if self.hourly_rate and self.hours:
            total_pay += self.hourly_rate * self.hours
        if self.contract_commision and self.contract_commision_rate:
            total_pay += self.contract_commision * self.contract_commision_rate
        if self.bonus_commision:
            total_pay+= self.bonus_commision
        return total_pay

    def get_components(self):
        components = []

        if self.salary_rate:
            components.append(f'a monthly salary of {self.salary_rate}')
        if self.hourly_rate:
            components.append(f'a contract of {self.hours} hours at {self.hourly_rate}/hour')
        if self.contract_commision and self.contract_commision_rate:
            components.append(f'receives a commission for {self.contract_commision} contract(s) at {self.contract_commision_rate}/contract')
        if self.bonus_commision:
            components.append(f'receives a bonus commission of {self.bonus_commision}')

        return components

    def __str__(self):
        components = self.get_components()
        components_str = ' and '.join(components) if components else ''
        total_pay = self.get_pay()
        return f'{self.name} works on {components_str}. Their total pay is {total_pay}.'

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary_rate=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hourly_rate=25, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary_rate=3000, contract_commision_rate=200, contract_commision=4)


# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.
jan = Employee('Jan', hours=150, hourly_rate=25, contract_commision=3, contract_commision_rate=220)


# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary_rate=2000, bonus_commision=1500)


# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, hourly_rate=30, bonus_commision=600)
