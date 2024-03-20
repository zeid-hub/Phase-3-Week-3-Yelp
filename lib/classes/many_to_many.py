class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._reviews = []

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._first_name = value
        else:
            raise ValueError("First name must be a string with length between 1 and 25.")
        
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._last_name = value
        else:
            raise ValueError("Last name must be a string with length between 1 and 25.")

    def reviews(self):
        return self._reviews

    def restaurants(self):
        return list({review.restaurant for review in self._reviews})

    def num_negative_reviews(self):
        return sum(1 for review in self._reviews if review.rating in [1, 2])

    def has_reviewed_restaurant(self, restaurant):
        return any(review.restaurant == restaurant for review in self._reviews)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self._reviews = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str)and  len(value) >= 1:
            self._name = value
        else:
            raise ValueError('Name must be a string and more than 1 characters')

    def reviews(self):
        return self._reviews

    def customers(self):
        return list({review.customer for review in self._reviews})

    def average_star_rating(self):
        total_ratings = sum(review.rating for review in self._reviews)
        num_ratings = len(self._reviews)
        if num_ratings == 0:
            return 0.0
        return round(total_ratings / num_ratings, 1)

    @classmethod
    def top_two_restaurants(cls):
        pass


class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        customer._reviews.append(self)
        restaurant._reviews.append(self)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if isinstance(value, int) and range(1,6):
            self._rating = value
        else:
            raise ValueError("Rating must be an integer between 1 and 5")
        