import pandas as pd

# Read in a data file
df1 = pd.read_csv('/Users/carlosm/Documents/refactor_me/refactor-me/data/raw/shopping_behavior_updated.csv')

# calculate summary statistics on the Purchase Amount column

# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?
purchaseamnt_stats = df1["Purchase Amount (USD)"].describe()
print("Summary statistics on Purchase Amount (USD)")
print(purchaseamnt_stats)

# calculate summary statistics on the Age column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?
age_stats = df1["Age"].describe()
print("Summary statistics on Age")
print(age_stats)

# summary statistics
# TODO: is there another function we can use to calculate metrics on groups?
seasons_stats = df1.groupby("Season")["Purchase Amount (USD)"].describe()
print("The Purchase Amount Stats by season are:")
print(seasons_stats)

# keep all columns except for "Customer ID", & "Discount Applied"
# TODO: is there a more efficient way to exclude columns in your dataset?
df1_new = df1.drop(['Customer ID', 'Discount Applied'], axis=1)

# figure out most popular payment method in NY
# TODO: is there anyway we could modularize this behavior to apply to all
# TODO: possible states? (OR possibly use a pandas function that does this
# TODO: for us already?)

#new attempt
def find_pop_payment(state):
    payment_methods = df1['Payment Method'].unique()
    us_state = df1[df1.Location == state]

    most_frequent_method = {}

    for method in payment_methods:
        most_frequent_method[method] = len(us_state[us_state['Payment Method'] == method])

    print(most_frequent_method)

find_pop_payment("California")

# Write this updated data out to csv file
df1.to_csv('data/processed/cleaned_data.csv', index=False)
