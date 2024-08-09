import streamlit as st
import joblib 
import pandas as pd

st.title("Driver License Status")

st.header("Please answer the following questions!")

def user_inputs():
    data = {
        "Type" : [st.selectbox("Type", ["HDR", "PDR", "VDR"])],
        "Drug Test" : [st.selectbox("Drug Test", ["Complete", "Needed", "Not Applicable"])],
        "WAV Course" :[st.selectbox("WAV Course", ["Complete", "Needed", "Not Applicable"])],
        "Defensive Driving" : [st.selectbox("Defensive Driving", ["Complete", "Needed", "Not Applicable"])],
        "Driver Exam" : [st.selectbox("Driver Exam", ["Complete", "Needed", "Not Applicable"])],
        "Medical Clearance Form" : [st.selectbox("Medical Clearance Form", ["Complete", "Needed", "Not Applicable"])]
    }
    df = pd.DataFrame(data)
    return df

def label_encoder(df):
    df['Type'] = df['Type'].map({"HDR":0,"PDR":1, "VDR":2})
    df['Drug Test'] = df['Drug Test'].map({"Complete":0,"Needed":1, "Not Applicable":2})
    df['WAV Course'] = df['WAV Course'].map({"Complete":0,"Needed":1, "Not Applicable":2})
    df['Defensive Driving'] = df['Defensive Driving'].map({"Complete":0,"Needed":1, "Not Applicable":2})
    df['Driver Exam'] = df['Driver Exam'].map({"Complete":0,"Needed":1, "Not Applicable":2})
    df['Medical Clearance Form'] = df['Medical Clearance Form'].map({"Complete":0,"Needed":1, "Not Applicable":2})
    return df

def main():
    df = user_inputs()
    df = label_encoder(df)
    model = joblib.load('project1.pkl')
    value = model.predict(df)

    if st.button("Proceed"):
        st.write("Your current status: ")
        if value[0]==0:
            st.write("Approved - License Issued")
        elif value[0]==1:
            st.write("Denied")
        elif value[0]==2:
            st.write("Incomplete")
        elif value[0]==3:
            st.write("Pending Fitness Interview")
        else:
            st.write("Under Review")

if __name__ == "__main__":
    main()
    