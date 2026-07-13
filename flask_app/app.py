from flask import Flask , render_template

#create an instance of the flask class
#"__name__" is a special variable that tells flask where to look for resources

app = Flask(__name__)

#Decorator: maps the url '/'

@app.route('/')

#Define a function to display text welcome to flask

def home():
    #write the text that can be displayed on ur browser
    return '<h1>Welcome to Flask Framework! </h1>'

#Route to about
@app.route('/about')

def about():
    return '<h2> i love flask frameork</h2>'

@app.route('/myStory')

def myStory():
    return '<h2> i have just started flask </h2?'

@app.route('/contact')

def contact():
    return '<h3> this is my contact: Nkubira </h3>'

#Dynamic Routing
@app.route('/contact/<name>')

def contact(name):
    return f"Welcome to {name}"

@app.route('/myStory/<title>')

def myStory(title):
    return f'<h2> {title} i have just started flask </h2?'

#Profile create Dynamic Route
@app.route('/user/<string:username>/<int:user_id>')

#defined the profile function
def profile(username,user_id):
    #data passed from python to the template
    return render_template('profile.html', username=username, user_id=user_id)


#Template inheritance

#To ensure the server runs only if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)

#Templates
#Allows us to dynamically insert datain them

#what is routing? its  all about connecting ur URL to the python fuction.
