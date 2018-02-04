from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACbb4d405452ebcf53e91ccffa9d670077"
# Your Auth Token from twilio.com/console
auth_token  = "3aa3a00bfeba486ca180c1c0fdbccc59"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15193621105",
    from_="+12267900348",
    body="yooo working?")

print(message.sid)
