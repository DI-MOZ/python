shopping_list= ["milk","eggs","bread","bananas"]
shopping_list.append("apples")
shopping_list.remove("bread")
def show_list(shop_list):
    for element in show_list:
        print(element)

def show_list_v2(shopping_list):
    print (shopping_list)
    
def total_items(shopping_list):
    return len(shopping_list)

print("your shopping list")
show_list_v2(shopping_list)
print("total items ",total_items(shopping_list))
                