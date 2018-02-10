from twilio.rest import Client

def main(number):
	# Your Account Sid and Auth Token from twilio.com/user/account
	account_sid = "AC793ee9eddad7ccf009b794965d16e392"
	auth_token = "39c708ac87ce5e58441a68e59f167d22"
	client = Client(account_sid, auth_token)

	call = client.calls.create(
	    to="+" + number,
	    from_="+16502097726",
	    url="http://demo.twilio.com/docs/voice.xml"
	)

	print(call.sid)
