# Zero Trust Policy Engine Simulation
def verify_access(user, password, mfa_token, resource_requested):
    # Database of users and their roles
    users_db = {
        "admin_user": {"pass": "secure123", "role": "Admin", "mfa": "888999"},
        "staff_user": {"pass": "staff456", "role": "Employee", "mfa": "111222"}
    }

    # Step 1: Verify Identity (Authentication)
    if user not in users_db or users_db[user]["pass"] != password:
        return "DENIED: Invalid Credentials"

    # Step 2: Verify MFA (Second Factor)
    if users_db[user]["mfa"] != mfa_token:
        return "DENIED: MFA Verification Failed"

    # Step 3: Verify Permissions (RBAC)
    user_role = users_db[user]["role"]
    
    if resource_requested == "Finance_Server" and user_role != "Admin":
        return f"DENIED: User {user} with role {user_role} cannot access Finance."
    
    return f"ACCESS GRANTED: Welcome to {resource_requested}."

# Testing the Zero Trust Model
print(verify_access("staff_user", "staff456", "111222", "Finance_Server"))