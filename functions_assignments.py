# Task 1
def apply_discount(price,discount_percent=5):
    if discount_percent>60:
        discount_percent=60
    discount_amount=price*discount_percent/100
    final_price=price-discount_amount
    return final_price

print(apply_discount(1000,10))
print(apply_discount(500))

# Task 2
def factorial(n):
    if n<0:
        print("error: Factorial is not defined for negative numbers ")
        return None
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
    
print(factorial(5))
print(factorial(0))
print(factorial(-3))

# Task 3
gst=lambda price:price+(0.18*price)
final_price=lambda price,discount:(price-(price*discount/100),(0.18*(price-(price*discount/100))))
print(final_price(100,10))

# Task 4
prices=[100,250,400,1200,50]
gst=lambda price:price+(0.18*price)
prices_with_gst=list(map(gst,prices))

print("original prices",prices)
print("prices after GST",prices_with_gst)

# Task 5
prices=[100,250,400,1200,50,2000,850]
print(list(filter(lambda prices:prices>500,prices)))
print(list(filter(lambda prices:prices<=500,prices)))

# Task 6
def process_prices(prices):
    discount_prices=list(map(lambda prices:prices*0.1,prices))
    filter_prices=list(filter(lambda prices:prices>300,prices))
    return discount_prices,filter_prices

prices=[100,500,900,50,750]
discounted, filtered = process_prices(prices)
print("discounted prices",discounted)
print("filtered prices",filtered)

# Task 7
def add_price(prices_list,price):
    prices_list.append(price)
def get_average_price(prices_list):
    if prices_list==0:
        return 0
    return sum(prices_list)/len(prices_list)
def get_max_price(prices_list):
    if len(prices_list)==0:
        return None
    return max(prices_list)

# creating menu
prices=[]
while True:
    print("\nMenu")
    print("1- Add price")
    print("2- show average price")
    print("3- show highest price")
    print("q- quit")

    choice=input("enter your choice: ")

    if choice=="1":
        price=float(input("enter prices:"))
        add_price(prices,price)
    if choice=="2":
        print("average price of prices: ",get_average_price(prices))
    if choice=="3":
        print("maximum value: ",get_max_price(prices))
    if choice=="q":
        break
    else:
        print("enter invalid string")
