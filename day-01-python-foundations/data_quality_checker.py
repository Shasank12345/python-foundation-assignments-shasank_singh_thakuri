''' Program to Calculate the total number and percentage of problematic rows.
    & Classify the dataset using these rules:
        ->At most 2%: Excellent
        ->More than 2% and at most 5%: Acceptable
        ->More than 5%: Needs Cleaning'''

#Input
total_rows = 2000
missing_rows = 120
duplicate_rows = 30

#Calculations
Total_Problematic_row =missing_rows+duplicate_rows
Problematic_row_percentages=(Total_Problematic_row/total_rows)*100
if(Problematic_row_percentages<=2):
    classification="Excellent"
elif(Problematic_row_percentages>2 and Problematic_row_percentages<=5):
    classification="Acceptable"
else:
    classification="Needs Cleaning"

#Output
print(f'''Total rows : {total_rows}
Probelematic rows: {Total_Problematic_row}
Problem percentage: {Problematic_row_percentages:.2f}%
Final Classification: {classification}''')

#Effective for multiline printing since it reduces redundant print statement without harming readability

