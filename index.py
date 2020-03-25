from flask import Flask, render_template,request
import re
#objeto
app=Flask(__name__)

@app.route('/')#pagina principal

def home():

    return render_template('home.html')


#expresion que operamos en la ventana
patron=re.compile('^([A-Z]{1}[0-9]{3}[a-z]+[\W]{3})$')

@app.route('/add_contact',methods=['POST'])
def add_contact():
    if request.method=='POST':
        expresion=request.form['expresion']

        if(patron.match(expresion)):

                return "¡Es correcta la expresión!"
        else:
                return "¡Es incorrecta la expresión!"
    
#escuchar siempre
if __name__=='__main__':
    app.run(debug=True)



