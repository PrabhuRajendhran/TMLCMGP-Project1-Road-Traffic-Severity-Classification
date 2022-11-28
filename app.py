import streamlit as st
import joblib
import os

model = joblib.load(os.path.join(r"G:\TMLC MGP Nov 2022\Project 1 - Road Traffic Severity Classification\Model", "model.joblib"))
print(model)

#creating option list for dropdown menu
options_day = ['Sunday', "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
options_age = ['18-30', '31-50', 'Over 51', 'Unknown', 'Under 18']

options_acc_area = ['Other', 'Office areas', 'Residential areas', ' Church areas',
       ' Industrial areas', 'School areas', '  Recreational areas',
       ' Outside rural areas', ' Hospital areas', '  Market areas',
       'Rural village areas', 'Unknown', 'Rural village areasOffice areas',
       'Recreational areas']
       
options_cause = ['No distancing', 'Changing lane to the right',
       'Changing lane to the left', 'Driving carelessly',
       'No priority to vehicle', 'Moving Backward',
       'No priority to pedestrian', 'Other', 'Overtaking',
       'Driving under the influence of drugs', 'Driving to the left',
       'Getting off the vehicle improperly', 'Driving at high speed',
       'Overturning', 'Turnover', 'Overspeed', 'Overloading', 'Drunk driving',
       'Unknown', 'Improper parking']
options_vehicle_type = ['Automobile', 'Lorry (41-100Q)', 'Other', 'Pick up upto 10Q',
       'Public (12 seats)', 'Stationwagen', 'Lorry (11-40Q)',
       'Public (13-45 seats)', 'Public (> 45 seats)', 'Long lorry', 'Taxi',
       'Motorcycle', 'Special vehicle', 'Ridden horse', 'Turbo', 'Bajaj', 'Bicycle']
options_driver_exp = ['5-10yr', '2-5yr', 'Above 10yr', '1-2yr', 'Below 1yr', 'No Licence', 'unknown']
options_lanes = ['Two-way (divided with broken lines road marking)', 'Undivided Two way',
       'other', 'Double carriageway (median)', 'One way',
       'Two-way (divided with solid lines road marking)', 'Unknown']

st.set_page_config(page_title="Accident Severity Prediction App", page_icon="🚧", layout="wide")

st.markdown("<h1 style='text-align: center;'>Accident Severity Prediction App 🚧</h1>", unsafe_allow_html=True)
#st.header("Accident Severity Prediction App 🚧")

with st.form('prediction_form'):

    st.subheader("Enter the input for following features:")
    
    hour = st.slider("Pickup Hour: ", 0, 23, value=0, format="%d")
    day_of_week = st.selectbox("Select Day of the Week: ", options=options_day)
    casualties = st.slider("Hour of Accident: ", 1, 8, value=0, format="%d")
    accident_cause = st.selectbox("Select Accident Cause: ", options=options_cause)
    vehicles_involved = st.slider("Pickup Hour: ", 1, 7, value=0, format="%d")
    vehicle_type = st.selectbox("Select Vehicle Type: ", options=options_vehicle_type)
    driver_age = st.selectbox("Select Driver Age: ", options=options_age)
    accident_area = st.selectbox("Select Accident Area: ", options=options_acc_area)
    driving_experience = st.selectbox("Select Driving Experience: ", options=options_driver_exp)
    lanes = st.selectbox("Select Lanes: ", options=options_lanes)

    submit = st.form_submit_button("Predict")

if submit:
    st.write(f"The predicted severity is:  Ulalalalaaa ")