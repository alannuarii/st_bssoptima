import pandas as pd
from joblib import load
from sklearn.preprocessing import PolynomialFeatures

# Inisiasi model dan PolynomialFeatures
model_cap_rul = 'models/capacity_to_rul/capacity_to_rul.pkl'
poly = PolynomialFeatures(degree=2, include_bias=False)  # Gunakan degree yang sama saat pelatihan

# Fungsi untuk memprediksi RUL berdasarkan kapasitas
def cap_to_rul(input):
    # Membuat data input
    data = {'Capacity': [input]}
    feature = pd.DataFrame(data)

    # Transformasi fitur menggunakan PolynomialFeatures
    feature_poly = poly.fit_transform(feature)  # Transformasikan input ke bentuk polinomial

    # Load model yang sudah disimpan
    loaded_model = load(model_cap_rul)

    # Prediksi RUL menggunakan model yang sudah dilatih
    rul = loaded_model.predict(feature_poly)

    return rul[0]
