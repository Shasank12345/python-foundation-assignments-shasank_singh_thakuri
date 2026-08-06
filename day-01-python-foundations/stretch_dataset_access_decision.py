'''Program to Create:
        user_role = "analyst"
        is_active = True
        requested_dataset = "sales_data"
    We have 
    Allowed roles:
        ["analyst", "scientist", "engineer"]
    & Restricted datasets:
    ["salary_data", "personal_data"] 
    Access is granted only when:
        The user is active.
        The role is allowed.
        The dataset is not restricted.
'''


Allowed_roles = ["analyst", "scientist", "engineer"]
Restricted_datasets = ["salary_data", "personal_data"]


#Function to check
def check_access(role: str, is_active: bool, requested_dataset: str):
    if not is_active:
        print("Access denied because the user is inactive.")  
    elif role not in Allowed_roles:
        print("Access denied because the role is not allowed.")
    elif requested_dataset in Restricted_datasets:
        print("Access denied because the dataset is restricted.")
    else:
        print("Access granted.")


# GIVEN SCENARIO
user_role = "analyst"
is_active = True
requested_dataset = "sales_data"
status=check_access(user_role, is_active, requested_dataset)

# scenario where role is not allowed
status=check_access("intern", True, "sales_data")

# scenario where user is inactive
check_access("scientist", False, "sales_data")

# scenario where dataset is restricted
check_access("engineer", True, "personal_data")

# scenario where access is granted
check_access("engineer", True, "intern_data")