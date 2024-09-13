from models.restaurant import Restaurant

restaurant_square = Restaurant('Golden Spoon', 'Gourmet')
restaurant_square.receive_rating('Gui', 5)
restaurant_square.receive_rating('Lais', 4)
restaurant_square.receive_rating('Emy', 2)

def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()
