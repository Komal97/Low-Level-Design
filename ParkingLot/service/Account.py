class Account:
    
    def __init__(self):
        self.name = None
        self.email = None
        self.phone = None
        self.emp_id = None
        self.address = None
        
class Admin(Account):
    
    def add_parking_floor(parking_lot, floor):
        pass
    
    def add_parking_space(parking_floor, parking_space):
        pass
    
    def add_parking_display_board(parking_floor, display_board):
        pass

class ParkingAttendent(Account):
    
    def __init__(self):
        self.payment_service = None
        
    def process_vehicle_entry(self, vehicle):
        pass
    
    def process_payment(self, parking_ticket, payment_type):
        pass