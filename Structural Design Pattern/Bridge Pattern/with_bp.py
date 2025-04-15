from abc import abstractmethod, ABC


class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class CreditCardPayment(Payment):
    def process_payment(self):
        print("Payment through Credit Card")


class PaypalPayment(Payment):
    def process_payment(self):
        print("Payment through PayPal")


class Ride(ABC):
    @abstractmethod
    def book_ride(self):
        pass


class UberGoRide(Ride):
    def __init__(self, payment: Payment):
        self.payment = payment

    def book_ride(self):
        print("Booking UberGo ride...")
        self.payment.process_payment()


credit_payment = CreditCardPayment()
paypal_payment = PaypalPayment()


uber_go_credit = UberGoRide(credit_payment)
uber_go_credit.book_ride()


uber_go_paypal = UberGoRide(paypal_payment)
uber_go_paypal.book_ride()
