## Pseudocode

1. Define ItemToPurchase class with members item_name, item_price, item_quantity and method print_item_cost
2. Start program
3. Prompt user for name
4. Validate input (string value). If invalid, exit
5. Initialize an empty list of ItemToPurchase objects (cart_items)
6. Begin a while loop. 
7. Ask for item name
8. Validate input (string value). If invalid, log a warning and return to step 6.
9. If input is a sentinel value (quit or q), break the loop and go to step 16.
10. Ask how much the item costs
11. Validate input (float value, positive). If invalid, log a warning and return to step 6.
12. Ask for the number of these items in the cart
13. Validate input (int value, positive). If invalid, log a warning and return to step 6.
14. Create an ItemToPurchase object and assign the name, cost and quantity
15. Add the ItemToPurchase object to the list (cart_items)
16. Loop back to step 6
17. Initialize a total_cost variable to 0
18. Start another loop over the number of ItemToPurchase objects in cart_items
19. Use the ItemToPurchase.print_item_cost() method to log the item name, quantity, per item cost and total cost
20. Calculate the item cost by multiplying item.item_price x item.item_quantity and add to running total (total_cost)
21. End loop
22. Print the total cost
23. End program

## Screen Shots

![](./modules/module4/images/run-1.png)

## Source Code

[GitHub](https://github.com/Tonitum/csu-global-csc-500/tree/master/modules/module4)
