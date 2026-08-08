#sales list analysis


monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]
sorted_sales=sorted(monthly_sales,reverse=True)
high_sales=[amount for amount in monthly_sales if amount>100000]
sales_withtax=[round(amount*1.13,3) for amount in monthly_sales ]
total_sales=sum(monthly_sales)
average_sales=total_sales/len(monthly_sales)


print(f'''
An original list : {monthly_sales}
A sorted list : {sorted_sales}
A list with values above 100k : {high_sales}
A list where each amount has 13% tax added : {sales_withtax}
The total sales amount : {total_sales}
The average sales amount : {average_sales}
''')
