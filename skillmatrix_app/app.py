from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('data/skills.csv')
    table_html = df.to_html(classes='table table-striped', index=False)
    return render_template('index.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
