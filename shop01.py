'''
Shopping cart example

user details
greet user -- any offers
main_menu -- categories, userprofile...
categiories -- mobile, laptops...
show_items
add cart
add wishlist
'''
'''
item = {
    name:
    price:
    category: 
    specs: {A
        modelno:
        ram:
    }
    color:
    warranty: 
}

mobiles = [item1, item2]
'''
mobiles = {
    'Samsung Galaxy S21' : 80999, 
    'iPhone 12' : 79990, 
    'Realme 7 Pro' : 35000, 
    'Oppo A12' : 29780, 
    'Moto G' : 45560,
    'realme 8' : 15000
}
laptops = {
    'Lenovo Ideapad' : 30990, 
    'HP 15s': 23990, 
    'Asus TUF Gaming' : 64990, 
    'Acer Aspire 7' :54960, 
    'Dell Inspiron':61990,
    'lenovo A10' : 45000
}
home_appliances = {
    'Pureit filter': 13000,
    'Bajaj fan': 1800,
    'Philips G7 Iron': 1125, 
    'Dyson room air purifier': 38000,
    'Eureka vaccum cleaner': 4000,
    'water purifier' :20000
}
audio = {
    'Realme buds 2': 600,
    'boAt rockerz': 1299,
    'JBL Headset': 1100,
    'Ubon Bluetooth Headset': 1500,
    'Motorola Pulse 3': 2500,
    'Air Pod series 3' : 30000
}
cameras = {
    'Canon EOS' : 25999,
    'Fujifilm XT3': 59000,
    'Sony B9': 66999,
    'Nikon D535': 44699,
    'Panasonic Lumix': 52650,
    'Sony A34' : 50000
}
categories = [mobiles, laptops, home_appliances, audio, cameras]

user_name = ''
user_cart = []
user_wishlist = []

def get_user():
    global user_name
    user_name = input("Enter your name : ")
    # you can also include other user information

def greet_user():
    global user_name
    print("\nHello, {}. \nWelcome to Flipkart... ".format(user_name))

def cart_or_wishlist(product, price):
    global categories, user_cart, user_wishlist
    print("\n*** Choose one option ***")
    print("1. Add to wishlist")
    print("2. Add to cart")
    print('0. Go to main menu')
    choice = int(input("Enter your choice : "))
    if choice == 0:
        show_menu()
    if choice == 1:
        user_wishlist.append({ 'name': product, 'price': price })
        print('\n{} is added to wishlist.'.format(product))
        show_wishlist()
    else:
        user_cart.append({ 'name': product, 'price': price })
        print('\n{} is added to cart.'.format(product))
        show_cart()

def show_categories():
    global categories
    category_names = ['Mobiles', 'Laptops', 'Home Appliances', 'Audio', 'Cameras']
    num = 1
    print("\n*** Categories ***")
    for ind in range(len(category_names)):
        print('{}. {}'.format(ind+1, category_names[ind]))
    print('0. Go to main menu')
    choice = int(input("Enter your choice : "))
    if choice == 0:
        show_menu()

    for prod_name, prod_price in categories[choice-1].items():
        print('\n{}. {}\nPrice: Rs.{}/-'.format(num, prod_name, prod_price))
        num += 1

    choice_prod = int(input("\nChoose any product : "))
    selected_prod_name = list(categories[choice-1])[choice_prod-1]
    selected_prod_price = categories[choice-1][selected_prod_name]
    cart_or_wishlist(selected_prod_name, selected_prod_price)

def show_wishlist():
    pass

def show_cart():
    global user_cart

    if len(user_cart) == 0:
        print('\nYour cart is empty!!')
    else:
        for ind, cart_item in enumerate(user_cart):
            print('{}. {} -- Rs.{}/-'.format(ind+1, cart_item['name'], cart_item['price']))

    show_menu()

def show_menu():
    options = ['Categories', 'My cart', 'My wishlist', 'Exit']
    print('\n*** Choose any option ***')
    for ind in range(len(options)):
        print('{}. {}'.format(ind+1, options[ind]))

    choice = int(input("Enter your choice : "))

    if choice == 1:
        show_categories()
    elif choice == 2:
        # my cart
        show_cart()
        
    elif choice == 3:
        # my wishlist
        pass
    elif choice == 4:
        exit(0)
        # return
    else:
        print('\nInvalid choice!!!. Please try again.')
        show_menu()

# main flow
get_user()
greet_user()
show_menu()