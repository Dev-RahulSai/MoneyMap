import argparse

from tracker.loader import load_statement
from tracker.categorizer import add_categories
from tracker.analysis import category_totals, monthly_summary
from tracker.charts import pie_chart, trend_chart


def main():
    parser = argparse.ArgumentParser(description="MoneyMap - see where your money goes")
    parser.add_argument("--file", default="sample_statement.csv", help="Path to your bank statement CSV")
    parser.add_argument("--month", help="Optional month filter, like 2026-09")
    args = parser.parse_args()

    df = load_statement(args.file)
    df = add_categories(df)

    if args.month:
        df = df[df["date"].dt.strftime("%Y-%m") == args.month]
        if df.empty:
            print("No transactions found for that month.")
            return

    totals = category_totals(df)
    summary = monthly_summary(df)

    print("\n--- Spending by Category ---")
    for category, amount in totals.items():
        print(f"{category:<15} Rs {amount:,.2f}")

    print("\n--- Monthly Summary ---")
    print(summary.round(2))

    pie_chart(totals)
    trend_chart(summary)
    print("\nCharts saved: spending_pie.png and monthly_trend.png")


if __name__ == "__main__":
    main()