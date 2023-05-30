from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        nilai = 10
        return render_template('results.html', name=name , nilai = 10)
    
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
