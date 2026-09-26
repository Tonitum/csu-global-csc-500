## Pseudocode

- Start
- Define global variable for tip amount (18%). This is to allow the code to be modified in the future to allow a user to select their tip amount.
- Define global variable for sales tax amount (7%). This is to easily adapt the code to different areas with different sales tax rates.
- Prompt user for base cost of meal.
- If the user cancels the input request, exit gracefully.
- Ensure user entered proper value for a float. If not, log an error and exit.
- Ensure user entered a positive, non-zero value. If not, log an error and exit.
- Calculate tip amount by multiplying global tip variable by base cost.
- Calculate sales tax amount by multiplying global sales tax variable by base cost.
- Calculate total by adding base cost, tip and sales tax amounts.
- Print the base cost
- Print the tip amount
- Print the sales tax amount
- Print the total amount
- End

## Screenshots

### Nominal Run

![](./modules/module3/images/run-1.png)

### Input is 0

![](./modules/module3/images/run-2.png)

### Input is negative

![](./modules/module3/images/run-3.png)

### Input is not numeric

![](./modules/module3/images/run-4.png)

## Source code

[GitHub](https://github.com/Tonitum/csu-global-csc-500/tree/master/modules/module3)

