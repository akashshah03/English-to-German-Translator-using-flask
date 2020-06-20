from flask import Flask,jsonify
from flask import request
from flask import render_template
from translate import Translator

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html") # this should be the name of your html file

@app.route('/', methods=['POST','GET'])
def my_form_post():
    text1 = request.form['text1']
    translator= Translator(to_lang="German")
    translation = translator.translate(text1)
    p=translation
    return render_template("result.html",text=text1,result=p)

if __name__ == '__main__':
    app.run()