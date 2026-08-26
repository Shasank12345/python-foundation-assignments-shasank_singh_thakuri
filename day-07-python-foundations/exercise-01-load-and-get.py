import pandas as pd



checkout_df=pd.read_csv('day-07-python-foundations/checkouts.csv')

number_of_checkouts=checkout_df['checkout_date'].count()
n_still_checked_out=checkout_df['return_date'].isnull().sum()


print(f'''
Total number of checkouts is {number_of_checkouts}
TOtal number of book which havent been returned is {n_still_checked_out}
''')

assert number_of_checkouts==len(checkout_df)
assert n_still_checked_out==checkout_df['return_date'].isna().sum()
assert n_still_checked_out<number_of_checkouts
print('''LOOKS GOOD''')

'''
ASSERT IS A DEBUGGING TOOL WHICH CHECKS CONDITION , IF FAILS EXECUTION IS TERMINATED
HERE THE LOOKS GOOD STATEMENT IS PROOF OF OUR SUCESSFUL EXECUTION

'''