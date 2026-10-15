# MoneyMap

See where your money goes. A Python tool that reads a bank statement CSV,
sorts each payment into categories, and draws spending charts.

## Setup
pip install -r requirements.txt

## Run
python main.py --file sample_statement.csv
python main.py --file sample_statement.csv --month 2026-09

## CSV format
Columns: Date, Description, Amount (spending is negative).