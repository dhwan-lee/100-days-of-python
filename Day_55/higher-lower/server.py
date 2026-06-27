from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)
@app.route('/')
def greeting():
    return '<div style="display: flex; flex-direction: column; align-items: center; justify-content: center">' \
            '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">' \
            '</div>'

@app.route('/<int:guess>')
def guess_number(guess):
    if guess < random_number:
        return  '<h1 style="text-align: center; color: red;">Too low, try again!</h1>' \
                '<div style="text-align: center">' \
                    '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">' \
                '</div>'
    
    if guess > random_number:
        return  '<h1 style="text-align: center; color: purple;">Too high, try again!</h1>' \
                '<div style="text-align: center">' \
                    '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">' \
                '</div>'
    
    if guess == random_number:
        return  '<h1 style="text-align: center; color: green;">You found me!</h1>' \
                '<div style="text-align: center">' \
                    '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">' \
                '</div>'


if __name__ == "__main__":
    app.run(debug=True, port=5000)