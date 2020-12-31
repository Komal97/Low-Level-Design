class ParkingTicket:
    
    def __init__(self):
        self.ticket_id = None
        self.space_id = None
        self.level_id = None
        self.vehicle_entry_datetime = None
        self.vehicle_exit_datetime = None
        self.parking_space_type = None
        self.total_cost = 0
        self.parking_ticket_status = None
        
    
    def update_total_cost(self):
        pass
    
    def update_vehicle_exit_time(self, vehicle_exit_datetime):
        pass