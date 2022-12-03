import pickle
import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))


def predictCrop(Area, Item, Year, avg_rainfall, pest_tonnes, avg_temp):
    Countries = {'Albania': 0, 'Algeria': 1, 'Angola': 2, 'Argentina': 3,
    'Armenia': 4, 'Australia': 5, 'Austria': 6, 'Azerbaijan': 7, 'Bahamas': 8, 'Bahrain': 9, 'Bangladesh': 10,
    'Belarus': 11, 'Belgium': 12, 'Botswana': 13, 'Brazil': 14, 'Bulgaria': 15, 'Burkina Faso': 16, 'Burundi': 17,
    'Cameroon': 18, 'Canada': 19, 'Central African Republic': 20, 'Chile': 21, 'Colombia': 22, 'Croatia': 23,
    'Denmark': 24, 'Dominican Republic': 25, 'Ecuador': 26, 'Egypt': 27, 'El Salvador': 28, 'Eritrea': 29,
    'Estonia': 30, 'Finland': 31, 'France': 32, 'Germany': 33, 'Ghana': 34, 'Greece': 35, 'Guatemala': 36,
    'Guinea': 37, 'Guyana': 38, 'Haiti': 39, 'Honduras': 40, 'Hungary': 41, 'India': 42, 'Indonesia': 43,
    'Iraq': 44, 'Ireland': 45, 'Italy': 46, 'Jamaica': 47, 'Japan': 48, 'Kazakhstan': 49, 'Kenya': 50, 'Latvia': 51,
    'Lebanon': 52, 'Lesotho': 53, 'Libya': 54, 'Lithuania': 55, 'Madagascar': 56, 'Malawi': 57, 'Malaysia': 58,
    'Mali': 59, 'Mauritania': 60, 'Mauritius': 61, 'Mexico': 62, 'Montenegro': 63, 'Morocco': 64, 'Mozambique': 65,
    'Namibia': 66, 'Nepal': 67, 'Netherlands': 68, 'New Zealand': 69, 'Nicaragua': 70, 'Niger': 71, 'Norway': 72,
    'Pakistan': 73, 'Papua New Guinea': 74, 'Peru': 75, 'Poland': 76, 'Portugal': 77, 'Qatar': 78, 'Romania': 79,
    'Rwanda': 80, 'Saudi Arabia': 81, 'Senegal': 82, 'Slovenia': 83, 'South Africa': 84, 'Spain': 85, 'Sri Lanka': 86,
    'Sudan': 87, 'Suriname': 88, 'Sweden': 89, 'Switzerland': 90, 'Tajikistan': 91, 'Thailand': 92, 'Tunisia': 93,
    'Turkey': 94, 'Uganda': 95, 'Ukraine': 96, 'United Kingdom': 97, 'Uruguay': 98, 'Zambia': 99, 'Zimbabwe': 100}
    
    Items = {'Maize': 0, 'Potatoes': 1, 'Rice, paddy': 2, 'Sorghum': 3, 'Soybeans': 4,
    'Wheat': 5, 'Cassava': 6, 'Sweet potatoes': 7, 'Plantains and others': 8, 'Yams': 9}
    
    input=np.array([[Countries[Area], Items[Item], Year, avg_rainfall, pest_tonnes, avg_temp]]).astype(np.float64)
    prediction=model.predict(input)
    return float(prediction)

def webPageLoader():
    #st.title("CROP YEILD PREDICTION")
    html_temp = """
    <h2 style = "background-color:green; text-align: Centre; padding: 5px">CROP PREDICTION WEBPAGE</h2
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    Area = st.selectbox("Country:",['Select a country','Albania','Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
    'Belarus', 'Belgium', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cameroon', 'Canada', 'Central African Republic', 'Chile', 'Colombia', 'Croatia',
    'Denmark', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Eritrea',
    'Estonia', 'Finland', 'France', 'Germany', 'Ghana', 'Greece', 'Guatemala',
    'Guinea', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'India', 'Indonesia',
    'Iraq', 'Ireland', 'Italy', 'Jamaica', 'Japan', 'Kazakhstan', 'Kenya', 'Latvia',
    'Lebanon', 'Lesotho', 'Libya', 'Lithuania', 'Madagascar', 'Malawi', 'Malaysia',
    'Mali', 'Mauritania', 'Mauritius', 'Mexico', 'Montenegro', 'Morocco', 'Mozambique',
    'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Norway',
    'Pakistan', 'Papua New Guinea', 'Peru', 'Poland', 'Portugal', 'Qatar', 'Romania',
    'Rwanda', 'Saudi Arabia', 'Senegal', 'Slovenia', 'South Africa', 'Spain', 'Sri Lanka',
    'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Tajikistan', 'Thailand', 'Tunisia',
    'Turkey', 'Uganda', 'Ukraine', 'United Kingdom', 'Uruguay', 'Zambia', 'Zimbabwe'])
    
    Item = st.selectbox("Item:",['select an item','Maize', 'Potatoes', 'Rice, paddy', 'Sorghum', 'Soybeans',
    'Wheat', 'Cassava', 'Sweet potatoes', 'Plantains and others', 'Yams'])

    Year = st.text_input("Year(","Type Here")
    avg_rainfall = st.text_input("avg_rainfall","Type Here")
    pest_tonnes = st.text_input("pest_tonnes","Type Here")
    avg_temp = st.text_input("avg_temp","Type Here")

    if st.button("Predict"):
        output=predictCrop(Area, Item, Year, avg_rainfall, pest_tonnes, avg_temp)
        st.success('The yeild is: {} tonnes for {}'.format(output,Area))
webPageLoader()
