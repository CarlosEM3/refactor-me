import pandas as pd

# Read in a data file
df1 = pd.read_csv('/Users/carlosm/Documents/refactor_me/refactor-me/data/raw/shopping_behavior_updated.csv')

# calculate summary statistics on the Purchase Amount column
purchaseamnt_stats = df1["Purchase Amount (USD)"].describe()
print("Summary statistics on Purchase Amount (USD)")
print(purchaseamnt_stats)


# calculate summary statistics on the Age column
age_stats = df1["Age"].describe()
print("Summary statistics on Age")
print(age_stats)

# summary statistics
# TODO: is there another function we can use to calculate metrics on groups?
seasons_stats = df1.groupby()