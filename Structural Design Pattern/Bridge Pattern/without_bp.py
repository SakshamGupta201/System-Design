class Payment:
    def process_payment(self):
        pass


class CreditCardPayment(Payment):
    def process_payment(self):
        print("Payment through credit Card")


class PaypalPayment(Payment):
    def process_payment(self):
        print("Payment through paypal")


class Ride:
    def book_ride(self):
        pass

    def process_payment(self):
        pass


class UberGoRideCreditPayment(Ride):
    def book_ride(self):
        print("Uber Go Ride")

    def process_payment(self):
        return CreditCardPayment.process_payment()


class UberGoRidePaypalPayment(Ride):
    def book_ride(self):
        print("Uber Go Ride")

    def process_payment(self):
        return PaypalPayment.process_payment()