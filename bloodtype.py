# creates the blood type object with specific attributes and methods
# for keeping track of donor's and recipient's blood types
class BloodType:

    # the blood type's constructor
    def __init__(self, type_name, rh_factor) -> None:
        self.type_name = type_name
        self.rh_factor = rh_factor

    # a method to determine the compatibility of blood types
    def get_compatible_types(self):

        # the method first determines the blood type, then whether it is positive or negative
        # to determine compatibility
        if self.type_name == "O":
            if self.rh_factor == "+":
                return ["O+", "O-"]
            else:
                return ["O-"]
        elif self.type_name == "A":
            if self.rh_factor == "+":
                return ["A+", "A-", "O+", "O-"]
            else:
                return ["A-", "O-"]
        elif self.type_name == "B":
            if self.rh_factor == "+":
                return ["B+", "B-", "O+", "O-"]
            else:
                return ["B-", "O-"]
        elif self.blood_type_name == "AB":
            if self.rh_factor == "+":
                return ["AB+", "A+", "B+", "O+", "AB-", "A-", "B-", "O-"]
            else:
                return ["AB-", "A-", "B-", "O-"]
            
    def check_compatibility(self, other_type):
        if self.rh_factor == "-" and other_type.rh_factor == "+":
            return f"{self.type_name} and {other_type.type_name} are not compatible."
        
        if self.type_name == "O":
            return other_type.type_name in ["O", "A", "B", "AB"]
        elif self.type_name == "A":
            return other_type.type_name in ["A", "O"]
        elif self.type_name == "B":
            return other_type.type_name in ["B", "O"]
        elif self.type_name == "AB":
            return other_type.type_name == "AB"
        
b1 = BloodType("A","-")
b2 = BloodType("B", "+")
b3 = BloodType ("O", "-")

print("Person 1 has blood type: " + str(b1.type_name) + ". They're list of compatible blood types are: ")
print(b1.get_compatible_types())
print("Person 2 has blood type: " + str(b2.type_name) + ". They're list of compatible blood types are: ")
print(b2.get_compatible_types())
print("Person 3 has blood type: " + str(b3.type_name) + ". They're list of compatible blood types are: ")
print(b3.get_compatible_types())

print(b1.check_compatibility(b2))
print(b2.check_compatibility(b3))
print(b3.check_compatibility(b1))

