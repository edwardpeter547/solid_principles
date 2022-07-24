
from order import Order, Item
from payment_processor import CreditPaymentProcessor, DebitPaymentProcessor, PaypalPaymentProcessor, SMSAuthorizer


def main():
    item = Item("beans", 1, 100.0)
    order = Order()
    order.add_item(item)
    
    authorizer = SMSAuthorizer()
    
    payment_processor = PaypalPaymentProcessor("edwardpeter547@gmail.com", authorizer)
    authorizer.verify_code(5469)
    payment_processor.pay(order)
    
    print(f"Total Price of Items: {order.total_price()}")
    print(f"Order Status {order.status}")
    


if __name__ == "__main__":
    main()