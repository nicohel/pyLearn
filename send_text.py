from twilio.rest import TwilioRestClient

account_sid = "AC94d76ab2ce61d67b41b9a191d7bef091" # Your Account SID from www.twilio.com/console
auth_token  = "59cb01528ed64170f9477debc304b817"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello my love! Can I interest you in some dinner?",
    to="+15103938277",    # Replace with your phone number
    from_="+16507536042") # Replace with your Twilio number

print(message.sid)
