from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/halaman-berikutnya')
def halaman_berikutnya():
    return 'Ini adalah halaman berikutnya'

if __name__ == '__main__':
    app.run(debug=True)
