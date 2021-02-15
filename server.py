from flask import Flask,request,jsonify
import util
app=Flask(__name__)



@app.route("/hello")
def hello():
    return "hello"

@app.route('/image', methods=['POST'])
def classify_image():
    image_data = request.form.get("image_data")
    response = jsonify(util.prediction_class(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=="__main__":
    util.load_artifact()
    app.run(port=8080)
