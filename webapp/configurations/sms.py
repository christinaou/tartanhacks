from twilio.rest import Client

def main(number, name):
	# Your Account Sid and Auth Token from twilio.com/user/account
	account_sid = "AC793ee9eddad7ccf009b794965d16e392"
	auth_token = "39c708ac87ce5e58441a68e59f167d22"
	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    to="+" + number,
	    body="Equerry Alert: \n" + name + " has notified us of an emergency. The poice are on their way.\n\nAlert location: 5000 Forbes Ave",
	    from_="+16502097726"
    )

	print(message.sid)