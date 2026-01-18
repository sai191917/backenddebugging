from flask import Flask, render_template, request

app = Flask(__name__)

# List to store notes
notes_list = []


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        note = request.form.get('note')

        # Validation: Avoid empty notes
        if note and note.strip() != "":
            notes_list.append(note)

    return render_template('home.html', notes=notes_list)


if __name__ == '__main__':
    app.run(debug=True)