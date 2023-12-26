import streamlit as st
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pickle
import joblib


laptop4=pd.read_pickle(open("laptop4.pkl","rb"))

Data_raw = pd.read_pickle(open("Data_raw.pkl","rb"))
st.image('header.jpeg')


st.title(':blue[Laptop Price Predictor]')
st.write("""-- This app predicts Laptop price for clients base on specification --

""")
st.write('Input your specification below to get a Price')


# Collects user input features into dataframe

def user_input_features():
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        # brand input
        Company = st.selectbox("Brand", Data_raw["Company"].unique())

    with middle_column:
        # laptop type
        Typename = st.selectbox("Type Name", Data_raw["TypeName"].unique())

    with right_column:
        #Inches
        inches = st.number_input("Inches (in inches)")
        

    # making 3 cols left_column, middle_column, right_column
    left_column, middle_column, right_column = st.columns(3)

    with left_column:
        # Ram size
        ram = st.selectbox("Ram (in GB)", laptop4["Ram"].unique())


    with middle_column:
        # Weight input
        weight = st.number_input("Weight of laptop in kg")
        

    with right_column:
        # Touchscreen
        Touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])
        


    # making 3 cols left_column, middle_column, right_column
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        # IPS display
        Ips = st.selectbox("IPS Display", ["No", "Yes"])


    with middle_column:
        # X resolution 
        x_resolution = st.selectbox('Screen Resolution X_axis',[1366, 1440, 1600, 1920, 2160, 2256, 2304, 2400, 2560, 2736, 2880,3200, 3840])
        
    with right_column:
        # Y resolution
        y_resolution = st.selectbox('Screen Resolution Y_axis',[768,  900, 1080, 1200, 1440, 1504, 1600, 1800, 1824, 2160])
        

    # making 3 cols left_column, middle_column, right_column
    left_column, middle_column,  right_column = st.columns(3)
    with left_column:
        # cpu input
        Cpu_brand = st.selectbox("CPU Brand", Data_raw["Cpu_brand"].unique())

    with middle_column:
        # hdd input
        hdd = st.selectbox("HDD(in GB)", [0, 128, 256, 512, 1024, 2048]) 


    with right_column:
        # ssd input
        SSD = st.selectbox("SSD(in GB)", [0, 8, 16, 32, 64, 128, 256, 512, 1024])


    #gpu input
    Gpu_brand=st.selectbox("GPU Brand",Data_raw["Gpu_brand"].unique())

    #os input
    os=st.selectbox("OS Type",Data_raw["os"].unique())


    company_dict = {
    0: 'Acer', 1: 'Apple', 2: 'Asus', 3: 'Chuwi', 4: 'Dell', 
    5: 'Fujitsu', 6: 'Google', 7: 'HP', 8: 'Huawei', 9: 'LG', 
    10: 'Lenovo', 11: 'MSI', 12: 'Mediacom', 13: 'Microsoft', 
    14: 'Razer', 15: 'Samsung', 16: 'Toshiba', 17: 'Vero', 18: 'Xiaomi'
    }

    # Convert company name to numerical value using the dictionary
    if Company in company_dict.values():
        Company = next(key for key, value in company_dict.items() if value == Company)



    typename_dic = {0: '2 in 1 Convertible', 1: 'Gaming', 2: 'Netbook', 3: 'Notebook', 4: 'Ultrabook', 5: 'Workstation'}

    # Convert company name to numerical value using the dictionary
    if Typename in typename_dic.values():
        Typename = next(key for key, value in typename_dic.items() if value == Typename)

   

    memory_dic = {0: 'AMD Processor', 1: 'Intel Core i3', 2: 'Intel Core i5', 3: 'Intel Core i7', 4: 'Other Intel Processor'}

    if Cpu_brand in memory_dic.values():
        Cpu_brand = next(key for key, value in memory_dic.items() if value == Cpu_brand)

    Gpu_brand_dic = {0: 'AMD', 1: 'Intel', 2: 'Nvidia'}
  
    if Gpu_brand in Gpu_brand_dic.values():
        Gpu_brand = next(key for key, value in Gpu_brand_dic.items() if value == Gpu_brand)

    OS_dic = {0: 'Mac', 1: 'Others/No OS/Linux', 2: 'Windows'}
    os = 'Mac'
    if os in OS_dic.values():
        os = next(key for key, value in OS_dic.items() if value == os)



    if Touchscreen=="Yes":
        Touchscreen=1
    else:
        Touchscreen=0

    if Ips == "Yes":
        Ips=1
    else:
        Ips=0
    ppi=((laptop4.X_res ** 2)+(laptop4.Y_res ** 2))**0.5/inches
    


    data = {'Company':Company, 'TypeName':Typename, 'Inches':inches, 'Ram':ram, 'Weight':weight, 'TouchScreen':Touchscreen, 'Ips':Ips, 'X_res':x_resolution,
       'Y_res':y_resolution, 'ppi':ppi, 'Cpu_brand':Cpu_brand, 'HDD':hdd, 'SSD':SSD, 'Gpu_brand':Gpu_brand, 'os':os
                }
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_features()

st.write(input_df)

def predict(data):
    clf = pd.read_pickle("pipe.pkl")
    return clf.predict(data)


# Apply model to make predictions
if st.button("Click here to Predict Price"):
    result = predict(input_df)

    st.title("The Predicted Price of the Laptop is Euro"+str(int(np.exp(result[0]))))

