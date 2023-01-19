from flask import Flask
app = Flask(__name__)

from flask import render_template 


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorite_5')
def favorite_5():
    artists = ['Kazuma Kaneko', 'Megumi Shiraishi', 'Ayami Kojima', 'Dean Dodrill', 'HR Giger']
    return render_template('favorite_5.html', artists=artists)

if __name__ == '__main__':
    app.run(debug=True)

