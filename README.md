# Council Tax Single Person Discount Checker

A small Python prototype for a local authority resident-facing service, built using Behaviour-Driven Development (BDD) with `behave`.

## User story
As a resident who lives alone, I want to check if I qualify for the single person discount, so that I know how much council tax I need to pay.

## Setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run the BDD tests
```
python -m behave
```

## Run the checker
```
python main.py
```