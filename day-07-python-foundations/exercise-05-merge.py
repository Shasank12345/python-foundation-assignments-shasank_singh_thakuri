# solved by both generator and group_by approach
import pandas as pd
BACKUP_BOOK_FACTS = {
    "Pride and Prejudice": {"author": "Jane Austen", "first_publish_year": 1813},
    "To Kill a Mockingbird": {"author": "Harper Lee", "first_publish_year": 1960},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "first_publish_year": 1925},
    "The Catcher in the Rye": {"author": "J. D. Salinger", "first_publish_year": 1951},
    "1984": {"author": "George Orwell", "first_publish_year": 1949},
    "Brave New World": {"author": "Aldous Huxley", "first_publish_year": 1932},
    "Frankenstein": {"author": "Mary Shelley", "first_publish_year": 1818},
    "Jane Eyre": {"author": "Charlotte Bronte", "first_publish_year": 1847},
    "Moby Dick": {"author": "Herman Melville", "first_publish_year": 1851},
    "The Hobbit": {"author": "J. R. R. Tolkien", "first_publish_year": 1937},
    "War and Peace": {"author": "Leo Tolstoy", "first_publish_year": 1869},
    "Crime and Punishment": {"author": "Fyodor Dostoevsky", "first_publish_year": 1866},
}
checkouts_df=pd.read_csv('day-07-python-foundations/checkouts.csv')
checkouts_clean=checkouts_df.copy()
checkouts_clean['is_returned']=checkouts_clean['return_date'].apply(lambda x:False if pd.isnull(x) else True)
checkouts_clean['late_fee']=checkouts_clean['late_fee'].apply(lambda x:0 if pd.isnull(x) else x)

book_facts_df=pd.DataFrame.from_dict(BACKUP_BOOK_FACTS,orient='index')
book_facts_df=book_facts_df.reset_index().rename(columns={'index':'book_title'})
merged_df=pd.merge(checkouts_clean,book_facts_df,on='book_title',how='left').drop(columns=['book_title'])

merged_df['author']=merged_df['author'].apply(lambda x:None if pd.isnull(x) else x)
merged_df['first_publish_year']=merged_df['first_publish_year'].apply(lambda x:None if pd.isnull(x) else x)

merged_dict=merged_df.to_dict(orient='records')\

#Generator approach
def return_record_with_author(merged_dict):
    for records in merged_dict:
        if records['author'] is not None :
            yield records

def calulate_total(merged_dict):
    total={}
    for record in return_record_with_author(merged_dict):
        author=record['author']
        late_fee=record['late_fee']
        total[author]=total.get(author,0)+late_fee

    sorted_total=dict(sorted(total.items(),key=lambda x:x[1] ,reverse=True))
    return sorted_total


final=calulate_total(merged_dict)
print("LATE FEE BY AUTHOR :")
print('''
USING GENERATOR APPROACH
''')

print(final)

print('''
USING GROUP BY APPROACH
''')
#group_by approach

with_author=merged_df[merged_df['author']!=None]
late_fee=with_author.groupby('author')['late_fee'].sum()
descending=late_fee.sort_values(ascending=False)

print(descending)