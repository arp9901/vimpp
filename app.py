#.\env\scripts\activate

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")          
def hello_world():
    return 'Hello World';
    # pass
    # return render_template('index.html')
    # return "Hello World!"

# @app.route("/product")
# def products():          
#     return "This is products page!"  ##if default function i.e '@app.route("/")' is not returning anything then it will make this return as default

if __name__ == '__main__':
    app.run(debug=True)


# this is my file structure

# now 
# index.html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     this is my page 2
# </body>
# </html>

# app.py 

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")          
# def hello_world():
#     return 'Hello World';
#     # pass
#     # return render_template('index.html')
#     # return "Hello World!"

# # @app.route("/product")
# # def products():          
# #     return "This is products page!"  ##if default function i.e '@app.route("/")' is not returning anything then it will make this return as default

# if __name__ == '__main__':
#     app.run(debug=True)
    
# now here i've deployed this in vercel and and made index.html as source (root) file as is in frontend now i want 