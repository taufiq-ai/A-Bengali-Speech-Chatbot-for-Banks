from flask import Flask, render_template
from agent import interactive_agent
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('conversation.html')

# @app.route('/goto_conversation') 
# def goto_conversation():
#     return render_template('conversation.html')


@app.route('/conversation', methods=["GET","POST"])
def conversation():
    interactive_agent()
    return render_template('conversation.html')

if __name__ == '__main__':
    app.run(debug=True)
