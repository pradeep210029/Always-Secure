from twilio.rest import Client


def sendSMS():
    account_sid = 'ACb5b8c6a90fa9c2653b824595113f84b4'
    auth_token = '8b30ac20c7fd44b4e56ee3ebe8559a32'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Someone is trying to open your account forcefully",
        from_='+15075123576',
        to='+918873811931'
        
    )



print("done")