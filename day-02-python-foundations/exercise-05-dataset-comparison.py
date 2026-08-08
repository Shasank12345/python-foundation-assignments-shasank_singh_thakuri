#Dateset Comparism 


#Given Data}
dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}
dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

unique_dataset=dataset_a.symmetric_difference(dataset_b)
common_dataset=dataset_a.intersection(dataset_b)
only_a=dataset_a.difference(dataset_b)
only_b=dataset_b.difference(dataset_a)


print(f'''
dataset_a :{dataset_a}
dataset_b :{dataset_b}
All unique dataset : {unique_dataset}
Datasets found in both groups : {common_dataset}
Datasets only found in dataset_a : {only_a}
Dataset only found in dataset_b : {only_b}
''')