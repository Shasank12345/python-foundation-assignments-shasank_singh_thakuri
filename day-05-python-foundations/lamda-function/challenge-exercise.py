
'''
DATA PROCESSING PIPELINE
'''

import functools as f
import json
from random import choice
sales = [
    {"product": "pen",    "qty": 10, "price": 1.5},
    {"product": "laptop", "qty": 2,  "price": 800.0},
    {"product": "pencil", "qty": 50, "price": 0.5},
    {"product": "monitor", "qty": 3,  "price": 150.0},
    {"product": "eraser", "qty": 25, "price": 0.2},
]

sales_with_total = list(
    map(lambda r: {**r, "total": r['qty']*r["price"]}, sales))
sales_with_total_morethan50 = list(
    filter(lambda r: r["total"] >= 50, sales_with_total))
grand_total_revenue = f.reduce(lambda x, y: x+y['total'], sales_with_total, 0)
sorted_sales = sorted(sales_with_total_morethan50,
                      key=lambda r: r['total'], reverse=True)


def surviving_products(sales_with_total_morethan50):
    for records in sales_with_total_morethan50:
        yield records


for records in surviving_products(sales_with_total_morethan50):
    for key, value in records.items():
        print(f'{key}:{value}')
    print(f"Grand Total : {grand_total_revenue}\n")
print('Record Processing Finished')


'''
LIST COMPREHENSION METHOD

'''
sales_with_total_2 = [{**r, "total": r['qty']*r['price']}for r in sales]


    

   

'''Map with lambda are less readable than the list comprehension'''

def print_records(records: list,grand_total_revenue,formatter={},style=" "):
    if style==" " and formatter=={}:
         for record in records:
                for key, value in record.items():
                    print(f'{key}:{value}')
                print(f"Grand Total : {grand_total_revenue}\n")
    else:
        for record in records:
            print(formatter[style](record))
        print(f"Grand Total : {grand_total_revenue}\n")

#Formatter records
formatter = {
    "short": lambda r: f"{r['qty']}*{r['price']}: {r['total']}",
    "verbose": lambda r: (
        f"Product : {r['product']}\n"
        f"Quantity: {r['qty']}\n"
        f"Price   : {r['price']}\n"
        f"Total   : {r['total']}"
    ),
    "json": lambda r: json.dumps(r),
    "csv": lambda r: f"{r['product']},{r['qty']},{r['price']},{r['total']}",
}
def menu():
    return f'''What do you want to print ?Choose for option:
    1. record of sales with total
    2. sales with total greater than 50
    3. sorted list of sales with total greater than 50 (higher to lower)
    
    '''
def style_menu():
    return f'''CHOOSE A STYLE :
    -short
    -csv
    -json
    -verbose
    
    '''



choice=" "
disp_menu='yes'
while(choice!="no"):
    if disp_menu=="yes":
        data=int(input(menu()))
    print("Do you want to choose a style? say yes or no")
    choose_style=input().lower().strip() 
    if choose_style=='yes':
        style=input(style_menu()).lower().strip()
        match data:
            case 1:
                print_records(sales_with_total,grand_total_revenue,formatter,style)
            case 2:
                print_records(sales_with_total,grand_total_revenue,formatter,style)
            case 3:
                print_records(sorted_sales,grand_total_revenue,formatter,style)
            case _:
                print("Nothing to print ")
    else:
        match data:
             case 1:
                    
                    print_records(sales_with_total,grand_total_revenue)
             case 2:
                    print_records(sales_with_total,grand_total_revenue)
             case 3:
                    print_records(sorted_sales,grand_total_revenue)
             case _:
                    print("Nothing to print ")
    choice=input("do you want to continue say yes or no").lower().strip()
    disp_menu=input("do you want to display menu again say yes or no").lower.strip()

            

        


