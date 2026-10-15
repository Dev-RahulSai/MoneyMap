import matplotlib.pyplot as plt


def pie_chart(totals, filename="spending_pie.png"):
    plt.figure(figsize=(6, 6))
    plt.pie(totals, labels=totals.index, autopct="%1.1f%%", startangle=90)
    plt.title("Where Your Money Went")
    plt.savefig(filename, bbox_inches="tight")
    plt.show()
    plt.close()


def trend_chart(summary, filename="monthly_trend.png"):
    plt.figure(figsize=(8, 5))
    plt.plot(summary.index.astype(str), summary["spent"], marker="o", label="Spent")
    plt.plot(summary.index.astype(str), summary["saved"], marker="o", label="Saved")
    plt.title("Monthly Spending vs Savings")
    plt.xlabel("Month")
    plt.ylabel("Amount (Rs)")
    plt.legend()
    plt.grid(True)
    plt.savefig(filename, bbox_inches="tight")
    plt.show()
    plt.close()