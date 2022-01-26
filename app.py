from flask import Flask, render_template

#app instance

app= Flask(__name__)


# app routes
@app.route('/')
def home():

    return render_template('home.html')

@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/register')
def register():

    return render_template('register.html')


    #run app 


if __name__=='__main__':
    app.run(debug=True)