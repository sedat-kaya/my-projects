from flask import Flask # bu python kodu, flaskten gerekli/ilgili kütüphaneyi çeker/indirir

app = Flask(__name__) # bu satırda app objesi oluşturuyor

@app.route('/') # bu satıra dekoreytır deniyor. "/" web sit. ana sayfayı ifade eder ve komutumuz anasayfayı dizayn eder
def hello():
    return "Hello World from Flask!!!" # bu kod bloğu ile artık internet sit. dizayn edilmeye başlanıyor
# bundan sonra gelecek kod bloklarıyla sitemizi dizayn/dekore etmeye devam ederiz

@app.route('/second') # anasayfadan sonra kullanıcı second derse alttaki yazı karşısına çıksın/çıkar
def second():
    return 'Bize Her Yer Trabzon!!!!'
# çalıştırdıktan sonra browser da localhost:5000/second yazarak arasak karşımıza ilgili metin çıkar

@app.route('/third/subthird') # web sit 3. sayfanın bir alt sayfasına aşagıdaki metni yazdırır
def third():
    return 'This is the subpage of third page'

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'


if __name__ == '__main__':
    app.run(debug=True)  # burası hata ayıklama modudur. yukarda yapılan yanlışta komut çalışmaz 
   
# if bloğu ile herşey yolundaysa komutu çalıştır diyor
# flask in ana çatısı yukarıdaki 3 komuttur.[1-3-24]
# biz flask ile bir web sitesi ayağa kaldıracağız








