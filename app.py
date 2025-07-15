import eda, prediction
import streamlit as st

with st.sidebar:
    st.write('# Page Navigation')

    page = st.selectbox('Pilih Halaman', 
                        ['EDA', 'Predict Rating'])
    
    st.write('# About')
    st.markdown('''Page ini berisikan hasil analisis data terhadap
                pemain di FIFA 2024\n\n dan juga prediksi rating pemain
                berdasarkan atribut yang dimiliki''')

if page == 'EDA':
    eda.run()

else:
    prediction.run()
    