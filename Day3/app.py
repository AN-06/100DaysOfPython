from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def treasure_island():
    if request.method == 'POST':
        step = session.get('step', 1)
        
        if step == 1:
            session['choice1'] = request.form.get('choice1', '').lower()
            if session['choice1'] == "left":
                session['step'] = 2
            else:
                result = "You fell into a hole. Game Over."
                session.clear()
                return render_template('index.html', result=result)
        
        elif step == 2:
            session['choice2'] = request.form.get('choice2', '').lower()
            if session['choice2'] == "wait":
                session['step'] = 3
            else:
                result = "You got attacked by an angry trout. Game Over."
                session.clear()
                return render_template('index.html', result=result)
        
        elif step == 3:
            session['choice3'] = request.form.get('choice3', '').lower()
            if session['choice3'] == "red":
                result = "It's a room full of fire. Game Over."
            elif session['choice3'] == "yellow":
                result = "You found the treasure. You Win!"
            elif session['choice3'] == "blue":
                result = "You enter a room of beasts. Game Over."
            else:
                result = "You chose a door that doesn't exist. Game Over."
            session.clear()
            return render_template('index.html', result=result)
        
    else:
        session.clear()
        session['step'] = 1
    
    return render_template('index.html', result=None, step=session.get('step', 1))

if __name__ == '__main__':
    app.run(debug=True)