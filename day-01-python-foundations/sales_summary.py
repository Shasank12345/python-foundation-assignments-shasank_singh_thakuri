''' Program to Create variables for a product name, unit price, quantity sold, and discount percentage,
    Calculate the gross sales, discount amount, and final sales amount.
    & Display the output using an f-string.'''

#Input
product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10

#Calculation
Gross_Sales=unit_price*quantity_sold
discount_amount=Gross_Sales*discount_percentage
final_sales=Gross_Sales-discount_amount


#Output
print(f"Product: {product_name} \n Gross sales:NPR {Gross_Sales:.2f} \n Discount: NPR {discount_amount:.2f} \n Final sales: NPR {final_sales:.2f}")
#note: Escape Sequence Character \n is used for printing data in new line but decreases readability of the code 