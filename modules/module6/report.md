# Module 6

## Pseudocode

1. Define ItemToPurchase class with members item_name, item_price, item_quantity and item_description. Initialize the name and description to "none", price to 0.0 and quantity to 0.
2. Define print_item_cost method to display the item name, quantity, price and subtotal (price x quantity).
3. Define ShoppingCart class with customer_name (default "none"), current_date (default "January 1, 2020") and an empty list of ItemToPurchase objects (cart_items).
4. Define find_item method to search cart_items by item name. Return the first matching item, or no item if not found.
5. Define add_item method to add an ItemToPurchase object to cart_items.
6. Define remove_item method to find an item by name and remove it. If not found, print "Item not found in cart. Nothing removed".
7. Define modify_item method to accept an ItemToPurchase object, find the existing item by name and update its quantity if found.
8. Define get_num_items_in_cart method to add the quantities of all items and return the total.
9. Define get_cost_of_cart method to add each item's price x quantity and return the total cost.
10. Define print_total method to print "SHOPPING CART IS EMPTY" if there are no items. Otherwise, print each item's cost details and the combined total cost.
11. Define print_descriptions method to print the name and description of each item in cart_items.
12. Start program and prompt user for name.
13. Create a ShoppingCart object using the user's name and today's date.
14. Begin a while loop and display the customer name, date and menu options (a, r, c, i, o and q).
15. Prompt user to select a menu option.
16. If the option is a (add item):
    - Ask for the item name, price, quantity and description.
    - Validate the price (float value, positive) and quantity (int value, positive). If invalid, display a warning or error and return to the menu.
    - If an item with the same name already exists, display an error and return to the menu.
    - Create an ItemToPurchase object, assign the entered values and use add_item to add it to the cart.
17. If the option is r (remove item), ask for the item name and use remove_item to remove it or display the not-found message.
18. If the option is c (change quantity):
    - Ask for the item name and find the existing item.
    - If not found, display an error and return to the menu.
    - Ask for the new quantity and validate it (int value, positive). If invalid, display a warning or error and return to the menu.
    - Create an ItemToPurchase object with the existing name and price and the new quantity. Use modify_item to update the cart.
19. If the option is i (output descriptions), use print_descriptions to display the item names and descriptions.
20. If the option is o (output shopping cart), use print_total to display the cart's item cost details and total, or the empty-cart message.
21. If the option is q (quit), break the menu loop.
22. If the option is invalid, display an error and return to the menu.
23. Repeat the menu loop after each completed action until q is selected.
24. Print "Goodbye" and end program.

## Screen Shots

### Item addition
![](./modules/module6/images/add.png)

### Item output
![](./modules/module6/images/desc-and-output.png)

### Item update
![](./modules/module6/images/update.png)

### Item removal
![](./modules/module6/images/remove.png)

## Source Code

[GitHub](https://github.com/Tonitum/csu-global-csc-500/tree/master/modules/module6)
