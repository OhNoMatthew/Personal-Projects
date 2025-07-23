class Microwave:
    """Class representing Microwaves with branding and power"""
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    # Methods
    def turn_on(self) -> None:
        """Method for turning on microwave"""
        if self.turned_on:
            print(f'Microwave ({self.brand}) is already turned on.')
        else:
            self.turned_on = True
            print(f'Microwave ({self.brand}) is now turned on.')

    def turn_off(self) -> None:
        """Method for turning off microwave"""
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave ({self.brand}) is already turned off.')
        else:
            self.turned_on = False
            print(f'Microwave ({self.brand}) is now turned off.')

    def run(self, seconds: int) -> None:
        """Method for using microwave"""
        if self.turned_on:
            print(f'Running ({self.brand}) for {seconds} seconds')
        else:
            print(f'A mystical force whispers: "Turn on microwave first..."')

    # Dunder Methods
    # def __add__(self, other):
    #     return f'{self.brand} + {other.brand}'
    
    # def __mul__(self, other):
    #     return f'{self.brand} * {other.brand}'

    # Useful String Dunder Method which is user freindly and easy to read
    def __str__(self) -> str:
        return f'{self.brand} (Rating: {self.power_rating})'
    
    # Useful Representation Dunder method which is developer friendly to identify the use of a class
    def __repr__(self) -> str:
        return f'Microwave(brand="{self.brand}", power_rating="{self.power_rating}")'

smeg: Microwave = Microwave('smeg', 'B')

# smeg.turn_on()
# smeg.run(30)
# smeg.turn_off()
# smeg.run(10)

# print(smeg)
# print(smeg.brand)
# print(smeg.power_rating)

bosch: Microwave = Microwave('bosch', 'C')

# bosch.turn_on()
# bosch.run(10)
# bosch.turn_off()
# print(bosch)
# print(bosch.brand)
# print(bosch.power_rating)

# print(smeg + bosch)
# print(smeg * bosch)

print(repr(smeg))
print(bosch)
