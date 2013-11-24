from flask import Flask, request, redirect, session
import twilio.twiml

# ???????????????????????????
SECRET_KET = 'khscjafhdkjasdf'
app = Flask(__name__)
app.config.from_object(__name__)

callers = {
	"+18572058821": "Katie Thomas"
}

@app.route("/", methods=['GET', 'POST'])
def hello_monkey(): 
	"""
	Respond with the number of text messages between two parties.
	"""

	counter = session.get('counter', 0)

	counter += 1

	session['counter'] = counter

	from_number = request.values.get("From")
	if from_number in callers: 
		name = callers[from_number]
	else:
		name = "Monkey"

	message = "".join([name, " has messaged ", request.values.get('To'), str(counter), " times."])
	
	resp = twilio.twiml.Response()
	resp.sms(message)
	return str(resp)

if __name__ == "__main__": 
	app.run(debug = True)