from abc import ABC, abstractmethod
from datetime import datetime


class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self. rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f'{self.company_name} with riders: {len(self.riders)} and drive: {len(self.drivers)}'




class User(ABC):
    def __init__(self, name, email, nID) -> None:
        self.name = name
        self.email = email
        # TODO: set user id dynamically
        self.__id = 0
        self.__nID = nID
        self.wallet = 0

    def display_profile(self):
        raise NotImplementedError
    


class Rider(User):
    def __init__(self, name, email, nID, current_location, initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, nID)

    def display_profile(self):
        print(f'Rider: Name: {self.name}, Email: {self.email}')

    def load_cash(self, amount):
        if amount > 0:
            self.wallet +=amount

    def update_location(self, current_location):
        self.current_location= current_location

    def request_ride(self,ride_sharing, destination):
        if not self.current_ride:
            # TODO: set ride properly
            # TODO: set current ride via ride match
            
            rede_requeset = Ride_Request(self, destination)
            ride_matcher = Ride_Matching(ride_sharing.drivers)
            ride = ride_matcher.find_driver(rede_requeset)
            print('got the ride, allhamdulilla')
            self.current_ride = ride

    def show_current_ride(self):
        print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, nID, current_location) -> None:
        self.current_location = current_location
        self.wallet = 0
        super().__init__(name, email, nID)

    def display_profile(self):
        print(f"Driver Name: {self.name}, Driver email: {self.email}")

    def accept_ride(self, ride):
        ride.set_driver(self)


class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None
        
        

    def set_driver(self, driver):
        self.driver =driver

    def start_ride(self):
        self.start_time = datetime.now()

    
    def end_ride(self, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self) -> str:
        return f'Ride details. Started: {self.start_location} to {self.end_location}'


class Ride_Request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location
        


class Ride_Matching:
    def __init__(self, driver) -> None:
        self.available_drivers = driver

    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            #TODO find the colosest driver of the rider
            print('looking for a driver')
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride
        
class Vehicle(ABC):
    speed = {
        'car' : 60,
        'bike' : 70,
        'cng' : 15
    }
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'available'
        

    @abstractmethod
    def start_drive(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)


    def start_drive(self):
        self.status = 'unavailable'


class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = 'unavailable'


# check the class integration: 

niya__jau = Ride_Sharing('Niya Jao')

alamin = Rider('Md Al Amin', 'alamin@nsu.edu', 1234, 'Bashundhara', 1200)
niya__jau.add_rider(alamin)

kala_phaki = Driver('Kala Phaki', 'kala@phaki.com', 5643, 'Gulshan-2')
niya__jau.add_driver(kala_phaki)

print(niya__jau)
alamin.request_ride( niya__jau, 'Uttara Gramer Bari')
alamin.show_current_ride()