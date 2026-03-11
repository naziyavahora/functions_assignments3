# Task 1 – Apply Discount
A function that applies a discount to a price.  
If the discount is greater than 60%, it automatically limits it to 60%.

Example:
- apply_discount(1000,10)
- apply_discount(500)

# Task 2 – Factorial using Recursion
This function calculates the factorial of a number using recursion.

Features:
- Handles negative numbers
- Returns factorial for positive numbers

Example:
- factorial(5)
- factorial(0)
- factorial(-3)

# Task 3 – GST Calculation using Lambda
Uses lambda functions to calculate:
- GST on a price
- Final price after applying discount and GST

GST rate used: **18%**

## Task 4 – Apply GST using map()
A list of prices is processed using the **map() function** to apply GST to each price.

Example price list:
```
[100, 250, 400, 1200, 50]
```
## Task 5 – Filter Prices using filter()
Uses **filter()** with lambda to separate prices:

- Prices greater than 500
- Prices less than or equal to 500

## Task 6 – Process Prices
This function performs two operations:

1. Calculates **10% discount** on prices
2. Filters prices **greater than 300**

Returns:
- Discounted prices list
- Filtered prices list

## Task 7 – Menu Driven Price Manager
A simple menu-based system that allows users to:

1. Add a price
2. Show average price
3. Show highest price
4. Quit the program

Functions used:
- `add_price()` – Adds price to list
- `get_average_price()` – Calculates average
- `get_max_price()` – Finds maximum price

# Example Menu

```
Menu
1 - Add price
2 - Show average price
3 - Show highest price
q - Quit
```
