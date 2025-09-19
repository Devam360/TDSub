from flask import Flask, render_template, request

#Interaction
web= Flask(__name__)
#Mapping
@web.route('/')
@web.route('/register')
#Inputs
def home():
    return render_template('register.html')
#Mapping
@web.route('/confirmation', methods=['POST','GET'])
#inputs
def register():
    if request.method == 'POST':
        n=request.form.get('name')
        c=request.form.get('city')
        p=request.form.get('phone number')
        return render_template("confirm.html", name=n, city=c, phone_number=p)
#main
if __name__ == "__main__":
    web.run(debug=True)
