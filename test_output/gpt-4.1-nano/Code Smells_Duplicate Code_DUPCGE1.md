**Code Review: DUPCGE1.java**

- **Code smell no.** - 1
- **Code smell name** - Duplicate Code
- **Code smell description** - The deposit, withdraw, and transfer methods all contain similar code for updating the balance and printing account details, leading to duplication.
- **Found in line no.** - 13, 18, 23, 28, 29, 30, 31, 32
- **Possible treatments** - Extract Method, Extract Method & then Move Method, Consolidate Duplicate Conditional Fragments
- **Possible solution** - Refactor the code to extract the common parts in account operations into dedicated methods like `updateBalanceAndPrint`, reducing duplication and improving maintainability.