import pandas as pd
def load_statement(file_path):
  df = pd.read_csv(file_path)
  df.columns = df.columns.str.strip().str.lower()
  df["date"] = pd.to_datetime(df["date"], dayfirst=True)
  df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
  df["description"] = df["description"].astype(str)
  df =df.dropna(subset = ["date","amount"])
  return df
