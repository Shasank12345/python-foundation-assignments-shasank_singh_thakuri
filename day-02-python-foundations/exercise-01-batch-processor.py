''' Implementation of range() and for loop to print batch number from 1 to 10 
&& display checkpoint on every third batch'''



#Implementation
for Batch_Number in range(1,11):
    print(f"Processing batch {Batch_Number}")
    if (Batch_Number%3==0):
        print("Checkpoint Reached") #checkpoint for every third batch
        print("")  #Printing newline after everycheckpoint increasing readability of the code 
    