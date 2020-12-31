from enum import Enum

class PaymentType(Enum):
    CASH = 1
    CREDIT_CARD = 2
    DEBIT_CARD = 3
    UPI = 4