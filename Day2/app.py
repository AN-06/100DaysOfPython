from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get form data
        bill = float(request.form['bill'])
        tip_percentage = int(request.form['tip_percentage'])
        people = int(request.form['people'])

        # Calculate total amount and per person amount
        total_tip = bill * (tip_percentage / 100)
        total_bill = bill + total_tip
        per_person = total_bill / people

        # Return result to the page
        return render_template('index.html', per_person=round(per_person, 2))
    except (ValueError, ZeroDivisionError):
        return render_template('index.html', error="Please enter valid inputs.")

if __name__ == "__main__":
    app.run(debug=True)
