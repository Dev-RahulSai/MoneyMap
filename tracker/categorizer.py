RULES = {
  "Food": ["swiggy", "zomato", "restaurant", "grocery", "bazar"],
  "Transport": ["uber", "ola", "fuel", "petrol"],
  "Shopping": ["amazon", "flipkart", "myntra"],
  "Bills": ["electricity", "recharge", "water", "gas"],
  "Entertainment": ["netflix", "spotify", "movie"],
  "Income": ["salary", "credit"],
}

def categorize(description, rules=RULES):
  description = description.lower()
  for category, keywords in rules.items():
    if any(word in description for word in keywords):
       return category
  return "Other"
 
 
def add_categories(df):
  df["category"] = df["description"].apply(categorize)
  return df
 