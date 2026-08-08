#order summary


orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}
def display_result(result:dict):
       for order_id,cust_info in result.items():
        print(f'''Order id : {order_id}\nCustomer Details :''')
        for key,value in cust_info.items():
            print(f"\t{key} : {value}")
        print("")
      


print(f"\nThe original order's are listed below :\n")
display_result(orders)

print(f"\nThe completed order's are listed below :\n")
for order_id,cust_info in orders.items():
        if cust_info['status'].lower()=="completed":
             display_result(orders)
                

total_amount=sum(cust_info['amount'] for cust_info in orders.values() if cust_info['status'].lower()=='completed')
pending_order=sum(1 for cust_info in orders.values() if cust_info['status'].lower()=='pending')

print(f'''
The Total amount of completed orders is {total_amount}
The Total number of pending orders is {pending_order}
''')


print(f"Do you want to add details of customer, Enter Yes or NO\n  ")
choice=input("choice :")
while(choice.lower()!="no"):
      order_id = input("Order ID (e.g., ORD-004): ")
      customer_name = input("Customer name: ")
      amount = int(input("Amount: "))
      status = input("Status (Completed/Pending): ")
      orders[order_id] ={
            "customer": customer_name,
            "amount": amount,
            "status": status
      }
      choice=input("Enter 'NO' if you want to stop\n")


print("\n Details After Adding new details are listed below\n")
display_result(orders)



    
        
    