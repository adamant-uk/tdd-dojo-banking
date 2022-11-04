# Banking Kata (TDD dojo green)

Create a simple bank application with features of depositing, withdrawing, and printing account statements.

## Setup
```bash
pipenv install --dev
pipenv run pytest .
```

## Requirements
* Create an account
* Deposit some amount of money into the account
* Withdraw some amount of money
* Get the account balance
* Retrieve a bank statement for an account for example:

```
DATE       | AMOUNT  | BALANCE
10/04/2014 | 500.00  | 1400.00
02/04/2014 | -100.00 | 900.00
01/04/2014 | 1000.00 | 1000.00
```

## Bonus
* Person A should be able to transfer some amount of money into Person B's account
* Get an accounts balance as at a point in time

## TDD flow 🏓
To make sure both people in your pair are contributing equally, please do ping-pong style TDD. This means:
1. Person A writes a failing test
2. Person B makes it pass
3. Person B writes a failing test
4. Person A makes it pass 

