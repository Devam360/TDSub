from flask import Flask, render_template

#Interaction
web=Flask(__name__)

#Mapping
@web.route('/')

#inputs
def index():
    return render_template('index.html')

#main
if(__name__=="__main__"):
    web.run(debug=True)