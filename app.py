from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)

public_key = "pk_test_OXMMuSKnLQkMNZXouzU7J4Jh00j6OzqSRg"

stripe.api_key = "sk_test_JQmUvn5YYGyVB070I5ox5xzT00qNGr6v3E"

@app.route('/')
def index():
    return render_template('index.html', public_key=public_key)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/payment',methods=['POST'])
def payment():

    # CUSTOMER INFO
    customer = stripe.Customer.create(email=request.form['stripeEmail'],
                                    source=request.form['stripeToken'])
                                
    # PAYMENT INFO
    charge = stripe.Charge.create(
        customer = customer.id,
        amount = 2000,
        currency='usd',
        description='Donation'
    )
    return redirect(url_for('thankyou'))

if __name__ == '__main__':
    app.run(debug=True)
