import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
sig, df = pickle.load(open("model.pkl","rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    input=[x for x in request.form.values()]
    try:
        title=input[0]
        idx=df.index[df['title']==title][0]
        sigs=list(enumerate(sig[idx]))
        sigs=sorted(sigs,key= lambda x:x[1],reverse=True)
        req=sigs[0:11]
        mov=[i[0] for i in req]
        if idx in mov:
            mov.remove(idx)
        temp=df['title'].iloc[mov]
        df_out = temp.to_frame()
        output=[x for x in df_out['title']]
    except:
        output='Enter valid title.'

    return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)
