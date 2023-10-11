class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def reviews(self):
        pass

    def restaurants(self):
        pass

    def num_negative_reviews(self):
        pass

    def has_reviewed_restaurant(self, restaurant):
        pass
    
class Restaurant:
    def __init__(self, name):
        self.name = name

    def reviews(self):
        pass

    def customers(self):
        pass

    def average_star_rating(self):
        pass

    @classmethod
    def top_two_restaurants(cls):
        pass
    
class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
