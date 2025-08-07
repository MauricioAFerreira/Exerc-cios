class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
            else:
                print(f"Warning: {purchased_item} not found in menu.")
                
        return bill

brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu("brunch", brunch_items, 11, 16)

early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("early bird", early_bird_items, 15, 18)

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu("dinner", dinner_items, 17, 23)

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("kids", kids_items, 11, 21)

menus = [brunch, early_bird, dinner, kids]

#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))  

#crirando a franquia

class Franchise():
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available = []
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        available.append(menu)
    return available
        
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

franchises = [flagship_store, new_installment]
#criando business

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

take_a_arepa = Menu("take a arepa", arepas_items, 10, 20)  # 10 até 20 (8 não faz sentido para hora final)

arepas_place = Franchise("189 Fitzgerald Avenue", [take_a_arepa])

# Task 24: criar o business de arepas
arepa_business = Business("Take a' Arepa", [arepas_place])
