from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route to display the band name generator and handle submissions
@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize band_name to None
    band_name = None  
    if request.method == 'POST':
        city = request.form['city']
        pet = request.form['pet']
        band_name = f"{city} {pet}"  # Generate the band name
        return redirect(url_for('result', band_name=band_name))  # Redirect to result route with the band name
    return render_template('day1.html', band_name=band_name)  # Render without band name on initial load

@app.route('/result')
def result():
    band_name = request.args.get('band_name')  # Get the band name from the query parameters
    return render_template('day1.html', band_name=band_name)  # Render the template with the band name

if __name__ == '__main__':from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Route to display the band name generator and handle submissions
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        pet = request.form['pet']
        band_name = f"{city} {pet}"  # Generate the band name
        return render_template('day1.html', band_name=band_name)  # Render with band name

    return render_template('day1.html', band_name=None)  # Render without band name on initial load

if __name__ == '__main__':
    app.run(debug=True)

    app.run(debug=True)
