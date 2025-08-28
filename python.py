# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Derived class (inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call base constructor
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery

    def call(self, contact):
        print(f"Calling {contact} from {self.device_info()}...")

    def charge(self):
        print(f"{self.device_info()} is charging... Battery at {self.battery}%")

    def phone_info(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery}%"

# Example 
phone1 = Smartphone("Samsung", "Galaxy S22", 256, 85)
phone2 = Smartphone("Apple", "iPhone 14", 128, 65)

print(phone1.phone_info())
print(phone2.phone_info())

phone1.call("Alice")
phone2.charge()