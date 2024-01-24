import math

class Cart:
    baseDelivery_fee = 2.00
    def __init__(self, cart_value, delivery_distance, number_of_items, rush_hour):
        self.cart_value = cart_value
        self.delivery_distance = delivery_distance
        self.number_of_items = number_of_items
        self.rush_hour = rush_hour
        self.fee = 0.00

    def calculate(self):
        surcharge = 0.00
        if self.cart_value < 10:
            surcharge = 10 - self.cart_value  

        if self.delivery_distance > 1:
            surcharge = surcharge + (math.ceil(self.delivery_distance/0.5) - 2)

        if self.number_of_items > 4:
            surcharge = surcharge + (self.number_of_items-4)*0.5
        if self.number_of_items > 12: surcharge = surcharge + 1.20

        self.fee = self.baseDelivery_fee + surcharge

        if self.rush_hour == True: self.fee = self.fee*1.2

        if self.cart_value >= 200: self.fee = 0

        if self.fee > 15: return "value error"

        return self.fee




