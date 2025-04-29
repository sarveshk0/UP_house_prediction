import pandas as pd
import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

data = pd.read_csv('Cleaned_data.csv', index_col=0)
print(data.columns)  # Columns of the loaded data

pipe=pickle.load(open('RidgeModel.pkl','rb'))

@app.route('/')
def index():

    City=sorted(data['City'].unique())
    return render_template('index.html', City=City)

@app.route('/predict', methods=['POST'])
def predict():
    City=request.form.get('City')
    Apartement=request.form.get('Apartement')
    Area=request.form.get('Area')
    Rupee_per_area=request.form.get('Rupee_per_area(sq-feet)')

    print(City, Apartement, Area, Rupee_per_area)
    input= pd.DataFrame([[City, Apartement, Area, Rupee_per_area]],
                        columns=['City', 'Apartement', 'Area', 'Rupee_per_area(sq-feet)'])
    print(input)
    prediction = pipe.predict(input)[0] * 1e5
    print(prediction)
    
    return str(np.round(prediction,2))




if __name__ == "__main__":
    app.run(debug=True, port=5000)    

    