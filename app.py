
from flask import Flask, render_template ,redirect,request
import pickle
anemia = pickle.load(open('trained_model','rb'))
app = Flask(__name__)




@app.route('/',methods=['GET'])

def index():
    return "Welcome to animea detection webapp"

@app.route('/get-hemoglobin-result')

def hemobloginCalc():
    r= float(request.args.get('r'))
    g= float(request.args.get('g'))
    b= float(request.args.get('b'))
    gender= float(request.args.get('gender'))
    hb = anemia.predict([[r, g,	b, gender]])
    result = {}
    result['hb']=hb[0]
    return result

if __name__ == "__main__":
    app.run(debug=True)