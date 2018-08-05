from flask import Flask, abort, render_template, jsonify, request
from api import make_prediction

app=Flask('KickstarterApp')

@app.route('/predict',methods=['POST'])
def do_prediction():
    if not request.json:
        abort(400)

    data=request.json
    print(data)
    print("Zup yo")

    response=make_prediction(data)
    print("zuppppppp")


    return jsonify(response)


@app.route('/')
def index():
    return render_template('index.html')



app.run(debug=True)
