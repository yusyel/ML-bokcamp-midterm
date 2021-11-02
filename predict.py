
# %%
import pickle

from flask import Flask
from flask import request
from flask import jsonify
import xgboost as xgb

input_file = 'model.bin'

with open(input_file, 'rb') as f_in:
    (dv, model) = pickle.load(f_in)
# %%

app = Flask('chd')


@app.route('/predict', methods=['POST'])
def predict():
    x = request.get_json()
    features = dv.get_feature_names()
    d_vector = dv.transform([x])

    d_matrix = xgb.DMatrix(d_vector, feature_names=features)

    y_pred = model.predict(d_matrix)
    sonuc = y_pred >= 0.5
    result = {
        'Patients CHD risk probability': float(y_pred),
        'Patient CHD risk result': bool(sonuc)
    }
    
    return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

# %%

