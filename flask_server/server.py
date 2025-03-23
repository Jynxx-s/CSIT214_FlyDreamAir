from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../templates', static_folder='../static')


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('home.html', name=name)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)