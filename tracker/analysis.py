def get_expenses(df):
    expenses = df[df["amount"] < 0].copy()
    expenses["amount"] = expenses["amount"].abs()
    return expenses


def category_totals(df):
    expenses = get_expenses(df)
    return expenses.groupby("category")["amount"].sum().sort_values(ascending=False)


def monthly_summary(df):
    df = df.copy()
    df["month"] = df["date"].dt.to_period("M")
    income = df[df["amount"] > 0].groupby("month")["amount"].sum()
    spent = df[df["amount"] < 0].groupby("month")["amount"].sum().abs()
    summary = income.to_frame("income").join(spent.to_frame("spent"), how="outer").fillna(0)
    summary["saved"] = summary["income"] - summary["spent"]
    return summary