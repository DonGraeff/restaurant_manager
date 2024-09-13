from models.rating import Rating

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._ratings = []
        Restaurant.restaurants.append(self)
    
    def __str__(self):
        return f'{self._name} | {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        print(f"{'Restaurant Name'.ljust(25)} | {'Category'.ljust(25)} | {'Rating'.ljust(25)} |{'Status'}")
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.average_rating).ljust(25)} |{restaurant.active}')

    @property
    def active(self):
        return '⌧' if self._active else '☐'
    
    def toggle_status(self):
        self._active = not self._active

    def receive_rating(self, customer, rating):
        if 0 < rating <= 5:
            new_rating = Rating(customer, rating)
            self._ratings.append(new_rating)

    @property
    def average_rating(self):
        if not self._ratings:
            return '-'
        total_ratings = sum(rating._rating for rating in self._ratings)
        number_of_ratings = len(self._ratings)
        average = round(total_ratings / number_of_ratings, 1)
        return average
