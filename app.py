from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sql_injection', methods=['GET', 'POST'])
def sql_injection():
    if request.method == 'POST':
        username = request.form.get('username')
        query = f"SELECT * FROM users WHERE username = '{username}'"
        return f"Running query: {query}"
    return render_template('sql_injection.html')

@app.route('/xss', methods=['GET', 'POST'])
def xss():
    if request.method == 'POST':
        comment = request.form.get('comment')
        return f"תגובה התקבלה: {comment}"
    return render_template('xss.html')

@app.route('/parameter_tampering', methods=['GET', 'POST'])
def parameter_tampering():
    if request.method == 'POST':
        price = request.form.get('price')
        return f'המחיר ששילמת הוא: {price} ש"ח'
    return render_template('parameter_tampering.html')

if __name__ == '__main__':
    app.run(debug=True)
