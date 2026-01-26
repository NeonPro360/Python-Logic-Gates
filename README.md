# Optimizations
For XOR and XNOR logic, I originally had a conditional to first check that at least one statement is true, and then a second conditional to check if only one conditional is true. This was replaced with only one return statement that performs the same checks in less lines of code and less time.

OR, AND, NOR, and NAND logic currently uses a for loop to accomodate more than two conditionals. I am currently looking into a way to check each boolean in a more timely way.

The inclusion of OR, AND, NOR, NAND, and NOT logic gates are currently in the module for my own sense of completion.
