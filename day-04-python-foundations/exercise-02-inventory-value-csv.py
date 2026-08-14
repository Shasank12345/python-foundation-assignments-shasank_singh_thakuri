#Inventory Value from Csv
import csv 
def total_inventory_value(path)->float:
    total=0
    with open(path,'r',newline='') as f:
        reader=csv.DictReader(f)
        for row in reader:
            price=float(row["price"])
            quantity=float(row['quantity'])
            total+=price*quantity

    return round(total,2)
        



with open("day-04-python-foundations/products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "price", "quantity"])
    writer.writerow(["Notebook", "2.50", 20])
    writer.writerow(["Pen", "1.00", 50])
    writer.writerow(["Backpack", "35.00", 3])
print("products.csv created.")


print(f"The total inventory value is {total_inventory_value("day-04-python-foundations/products.csv")}")
