class Person(object):
    def __init__(self, name, blood_type) -> None:
        self.name = name
        self.blood_type = blood_type

class Donor(Person):
    def __init__(self, name, blood_type, last_donation_date) -> None:
        super().__init__(name, blood_type)
        self.last_donation_date = last_donation_date

    def getLastDonationDate(self):
        return self.last_donation_date

class Recipient(Person):
    def __init__(self, name, blood_type, priority_level) -> None:
        super().__init__(name, blood_type)
        self.priority_level = priority_level

    def updatePriorityLevel(self, new_priority):
        self.priority_level = new_priority

d1 = Donor("Tom", "A+", "12-December-2012")
print(f"Donor {d1.name} (Blood Type: {d1.blood_type}) last donated on {d1.getLastDonationDate()}.")

r1 = Recipient("Harry", "O-", "High")
r1.updatePriorityLevel("Low")
print(f"Recipient {r1.name} (Blood Type: {d1.blood_type}) is {r1.priority_level} priority.")
