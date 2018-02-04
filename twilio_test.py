from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACbb4d405452ebcf53e91ccffa9d670077"
auth_token = "3aa3a00bfeba486ca180c1c0fdbccc59"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+15193621105",
    from_="+12267900348",
    body="Testing this again!")