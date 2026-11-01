# Module 7

## Pseudocode

1. Initialize 3 dictionaries with course information
  - Course room
  - Course instructor
  - Course time
2. Seed the 3 dictionaries with course information for CSC101, CSC102, CSC103, NET110 and COM241
3. Print welcome messages and begin a loop
4. Prompt the user to enter a course number
5. Sanitize the input by stripping off whitespace and making it uppercase
6. Check if the input is a sentinel value [Q, QUIT]. If yes, break the loop, ending the program, going to step 9.
7. Check if the input course number exists in the information dictionaries. If not, print a warning and return to step 4, restarting the loop.
8. Print the course information. Return to step 4, restarting the loop.
9. Exit

## Screen Shots

![](./modules/module7/images/run-1.png)

## Source Code

[GitHub](https://github.com/Tonitum/csu-global-csc-500/tree/master/modules/module7)

