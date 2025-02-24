from simple_salesforce import Salesforce

# Connect to Salesforce
sf = Salesforce(
    username='your_salesforce_username',
    password='your_salesforce_password',
    security_token='your_salesforce_security_token',
    domain='login'  # or 'test' for sandbox
)

# Example: Create a Case (Ticket)
new_case = sf.Case.create({
    'Subject': 'Test Ticket',
    'Description': 'This is a test case from Popa Health.',
    'Priority': 'High',
    'Status': 'New'
})

print(f"Created Case ID: {new_case['id']}")
