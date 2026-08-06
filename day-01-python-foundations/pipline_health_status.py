'''Program to Calculate the failure rate Using these rules:
        ->Healthy: Failure rate is at most 2% and runtime is at most 20 minutes.
        ->Warning: Failure rate is more than 2% but at most 5%.
        ->Critical: Failure rate is more than 5%.
    & Display the failure rate and final pipeline status.'''



#Function to Check
def check_pipline_status(rows_loaded: int ,rows_failed: int,runtime_minute: int)->dict:
    total_rows=rows_loaded+rows_failed
    failure_rate=(rows_failed/total_rows)*100 if total_rows>0 else 0 #So that it wont throw divison by 0 error
    message=None
    if(failure_rate<=2):
        if(runtime_minute<20):
            status="Healthy"
        else:
            status="Warning"
            message="High runtime"
    elif(failure_rate>2 and failure_rate<=5):
        status="Warning"
    else:
        status="critical"

    return {
        "failure_rate":failure_rate,
        "status":status,
        "message": message if message is not None else ''
    }

#function to display
def display_result(result :dict):
    if result['message']=='':
        print(f"The final status of Pipline is {result['status']} with the failure rate of {result['failure_rate']}% respectively")
        
    else:
        print(f'''The final status of Pipline is {result['status']} with the failure rate of {result['failure_rate']}% respectively
        & The {result["status"]} is due to {result['message']}''')

        





#given scenario
result1 =check_pipline_status(9800, 200, 18) 
display_result(result1)

# test1
result2 =check_pipline_status(9500, 500, 15)
display_result(result2)

#test2
result3 =check_pipline_status(9900, 100, 30)
display_result(result3)

