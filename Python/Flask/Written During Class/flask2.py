from flask import Flask, render_template
import os
#interaction
app=Flask(__name__)

picfolder= os.path.join('static')
app.config["UPLOAD FOLDER"]=picfolder
#mapping
@app.route('/')

#inputs
def first():
    pic=os.path.join(app.config["UPLOAD FOLDER"],'cars.jpg')
    return render_template("home.html", user_image=pic)
#mapping
@app.route('/second')

#inputs
def second():
    return render_template("second.html")
#main
if(__name__=="__main__"):
    app.run(debug=True)