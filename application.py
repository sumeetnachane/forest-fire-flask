import pickle
import os
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pf
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

## import ridge regressor and standard scaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

@app.route("/")
def index():
  return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
  if request.method=='POST':
    Temperature=float(request.form.get('Temperature'))
    RH=float(request.form.get('RH'))
    Ws=float(request.form.get('Ws'))
    Rain=float(request.form.get('Rain'))
    FFMC=float(request.form.get('FFMC'))
    DMC=float(request.form.get('DMC'))
    ISI=float(request.form.get('ISI'))
    Classes=float(request.form.get('Classes'))
    Region=float(request.form.get('Region'))

    new_data_scaled = standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]]) ## Ye data ko scaled krta hai like -0.11,0.11
    result=ridge_model.predict(new_data_scaled) ## Ye scaled data ko predict krega

    return render_template('home.html', results=round(result[0],2)) ## round and 2 likha to rounded format like 1.23 not 1.2349540
  else:
    return render_template('home.html')   

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
