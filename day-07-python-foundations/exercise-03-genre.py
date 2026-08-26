import pandas as pd
import numpy as np

checkouts_df=pd.read_csv('day-07-python-foundations/checkouts.csv')


checkouts_clean=checkouts_df.copy()
checkouts_clean['is_returned']=checkouts_clean['return_date'].apply(lambda x:False if pd.isnull(x) else True)
checkouts_clean['late_fee']=checkouts_clean['late_fee'].apply(lambda x:0 if pd.isnull(x) else x)

checkouts=checkouts_clean.to_dict(orient='records')
#GENERATOR FOR LAZY EVALUATION AND MEMORY EFFICENCY
def return_data(checkouts):
    for row in checkouts:
        if row['is_returned']==True:
            yield row
def average_calculate(checkouts):
    total={}
    count={}
    for  data in return_data(checkouts):
        genre=data['genre']
        fee=data['late_fee']
        total[genre]=total.get(genre,0)+fee
        count[genre]=count.get(genre,0)+1
      

    averages = {genre: total[genre] / count[genre] for genre in total}
    sorted_averages = dict(sorted(averages.items(), key=lambda x: x[1], reverse=True))
    print(f'''The total late fee in respective genre is 
    {total}
The number of occurence of genre is 
    {count}''')
    return sorted_averages


average=average_calculate(checkouts)

print(f'''The average late fee by genere is listed below 
    {average}''')

''''
THIS CAN BE ALSO DONE USING THE GROUBBY AND MEAN FUNCTION INTO THE DATAFRAME DIRECTILY

'''
#METHOD 2
returned_checkouts=checkouts_clean[checkouts_clean['is_returned']==True]
average_checkout=returned_checkouts.groupby('genre')['late_fee'].mean()
sorted_average=average_checkout.sort_values(ascending=False)
print(sorted_average)

assert len(sorted_average) == checkouts_clean["genre"].nunique()
assert sorted_average.is_monotonic_decreasing
print("Looks good -- worst genre for late fees:", sorted_average.idxmax())