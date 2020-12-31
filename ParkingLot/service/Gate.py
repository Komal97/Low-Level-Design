from abc import ABC, abstractmethod

class Gate:
    
    def __init__(self, gate_id, attendent):
        self.gate_id = gate_id
        self.attendent = attendent
        
class EntranceGate(Gate):
    
    def __init__(self, gate_id, attendent):
        super().__init__(gate_id, attendent)
        
    def process_ticket(self, vehicle):
        pass

class ExitGate(Gate):
    
    def __init__(self, gate_id, attendent):
        super().__init__(gate_id, attendent)
        
    def process_payment(self, ticket, payment_type):
        pass
    