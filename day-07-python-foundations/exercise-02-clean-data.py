import pandas as pd


checkout_df=pd.read_csv('day-07-python-foundations/checkouts.csv')
checkouts_clean=checkout_df.copy()

checkouts_clean['is_returned'] = checkout_df['return_date'].apply(lambda x: False if pd.isnull(x) else True)
checkouts_clean['late_fee'] = checkouts_clean['late_fee'].apply(lambda x: 0 if pd.isnull(x) else x)


print(checkouts_clean.head()) 