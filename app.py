from flask import Flask

#app instance

app= Flask(__name__)


# app route
@app.route('/')
def home():

    return "Hello"


    #run app


if __name__=='__main__':
    app.run(debug=True)