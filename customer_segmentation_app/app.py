from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model dan scaler
model = joblib.load('model/kmeans_model.pkl')
scaler = joblib.load('model/scaler.pkl')

segment_map = {
    0: 'Occasional Buyers',
    1: 'Loyal High-Spenders',
    2: 'Dormant Customers',
    3: 'Potential Loyalists'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    segment = None
    if request.method == 'POST':
        recency = int(request.form['recency'])
        frequency = float(request.form['frequency'])
        monetary = float(request.form['monetary'])

        frequency_log = np.log1p(frequency)
        monetary_log = np.log1p(monetary)
        data = scaler.transform([[recency, frequency_log, monetary_log]])
        cluster = model.predict(data)[0]
        segment = f"{segment_map[cluster]} (Cluster {cluster})"

    return render_template('index.html', segment=segment)

if __name__ == '__main__':
    app.run(debug=True)