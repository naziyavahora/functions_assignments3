Task 1: Price After Discount

* Created a function `apply_discount(price, discount_percent)`
* Returns the price after applying a discount.
* Uses a **default discount of 5%** if no discount is provided.
* Ensures the discount does not exceed **60%**.

---

 Task 2: Recursive Factorial Function

* Implemented a recursive function `factorial(n)`.
* Handles edge cases:

  * `n = 0`
  * `n = 1`
* Displays an error message for negative numbers.

---

Task 3: Lambda Function – GST Calculator

* Created a lambda function to calculate price after adding **18% GST**.
* Also implemented a lambda to calculate **final price after discount and GST**.

---

 Task 4: Using map()

* Applied GST to a list of product prices using the `map()` function.
* Generated a new list containing prices after GST.

Example list:

```
[100, 250, 400, 1200, 50]
```

---

 Task 5: Using filter()

* Used the `filter()` function to separate product prices:

  * Prices **greater than 500**
  * Prices **less than or equal to 500**

---

 Task 6: Combined Utility Function

* Created `process_prices(prices)` function that:

  * Applies **10% discount** using `map()`  
  * Filters discounted prices **above 300** using `filter()`
* Returns:

  * `discounted_prices`
  * `filtered_prices`

---

 Task 7: Menu-Based Program

Implemented a simple menu-driven system with functions:

Functions used:

* `add_price()` – Adds a price to the list
* `get_average_price()` – Calculates average price
* `get_max_price()` – Finds the highest price

Menu options:

```
1 - Add price
2 - Show average price
3 - Show highest price
q - Quit
```