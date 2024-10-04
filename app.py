from flask import Flask, request, render_template
from synthese import resume
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/translate")
def translate():
    return render_template('translate.html')

@app.route("/summarize", methods=['GET', 'POST'])
def summarize():
    
    text = request.form.get('text')
    if text == None:
        text = ''
    
    # Vérifiez si le texte n'est pas vide ou None
    if text:
        text_to_resume = resume(text)  # Si le texte est valide, appelez la fonction resume
    else:
        text_to_resume = "Aucun texte n'a été fourni à résumer."
    
    return render_template('summarize.html', text_to_show=text_to_resume, text_entered=text)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)