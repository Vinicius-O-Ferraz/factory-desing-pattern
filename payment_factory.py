from inspect import getmembers, isclass, isabstract
import payment_methods

class PaymentFactory(object):
    payment_implementions = {}

    def __init__(self) -> None:
        self.load_payment_methods()

    def load_payment_methods(self):
        implementations = getmembers(payment_methods, lambda m: isclass(m) and not isabstract(m))
        for name, _type in implementations:
            if isclass(_type) and issubclass(_type, payment_methods.Payment):
                self.payment_implementions[name] = _type
    
    def create(self,payment_type: str):
        if payment_type in self.payment_implementions:
            return self.payment_implementions[payment_type]()
        else:
            raise ValueError(f"{payment_type} is not currentyly supported as a payment method.")