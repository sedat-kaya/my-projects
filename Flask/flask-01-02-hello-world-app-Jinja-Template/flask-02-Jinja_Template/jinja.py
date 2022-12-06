from flask import Flask, render_template # bu uygulama dosyasında template kullanacağımızdan tamplate kiralıyoruz

app = Flask(__name__)

@app.route('/') # bu kod bloğu wwb sit ayrı dekore eder
def head():
    return render_template('index.html', number1 = 117000, number2 = 229000)
# yukarıda : index.html kiralanmıştır

@app.route('/sum') # bu kod bloğu wwb sit ayrı dekore eder
def number():
    var1, var2 = 15000, 30000
    return render_template('body.html', value1 = var1, value2 = var2, sum = var1+var2)
# yukarda index.html kiralanmıştı burda body.html kiralanmış


if __name__ == '__main__':
    app.run(debug=True) # buraya başka bir port girmezsek 5000 portta çalışır