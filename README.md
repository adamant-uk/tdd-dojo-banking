# Banking Kata (TDD dojo green)

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
