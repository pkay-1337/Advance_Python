class Bill:
    """Object that contains data about bill. like period and amount"""
    def __init__(self, amount, period):
         self.amount = amount
         self.period = period

class Flatmate:
    """flatmate"""
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self):
        pass



