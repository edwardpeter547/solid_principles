from abc import ABC, abstractmethod, abstractproperty
from random import randint, random

class PaymentProcessor(ABC):
    
    @abstractmethod 
    def pay(self, order, security_code: int):
        pass
    
    
class Authorizer(ABC):
    
    authorized = False
    
    @abstractmethod
    def is_authorized(self) -> bool:
        pass
    

class SMSAuthorizer(Authorizer):        
    
    def verify_code(self, code):
        print(f"Verifying Code {code}")
        self.authorized = True
        
    def is_authorized(self) -> bool:
        return self.authorized
    
class EmailAuthorizer(Authorizer):
    
    def verify_code(self, code):
        print(f"Verifying Email {code}")
    
    def is_authorized(self) -> bool:
        return self.authorized
    
   

class CreditPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code):
        self.security_code = security_code
    
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying Security Code: {self.security_code + 2}")
        order.status = "paid"
        


        
class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer
        
    
    def pay(self, order):
        if not self.authorizer.is_authorized:
            raise Exception("Not Authroized")
        print("processing debit payment type")
        print(f"verifying Security Code: {self.security_code + 1}")
        order.status = "paid"



        
class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email_address: str, authorizer: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer
    
    def pay(self, order):
        if not self.authorizer.is_authorized:
            raise Exception("Payment Not Authorized")
        print("processing paypal payment type")
        print(f"verifying Email Address: {self.email_address}")
        order.status = "paid"