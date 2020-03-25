from flask import Flask, render_template

#objeto
app=Flask(__name__)

@app.route('/')#pagina principal

def home():

    return render_template('home.html')


#escuchar siempre
if __name__=='__main__':
    app.run()

