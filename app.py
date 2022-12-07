import streamlit as st
from util import prediction


st.title("Will you get placed ?")
age = st.slider("Choose age ",14,30)
Stream = st.selectbox("Choose Stream",['Electronics And Communication', 'Computer Science','Information Technology', 'Mechanical', 'Electrical', 'Civil'])
Internships = st.slider("Choose Internships",0,3)
cgpa = st.slider("Choose CGPA ",5,10)
Hostel = st.select_slider("Choose Hostel No.", ['0','1'])
HistoryOfBacklogs = st.select_slider("History Of Backlogs", ['0','1'])

streams =['Civil','Computer Science','Electrical','Electronics And Communication','Information Technology','Mechanical']
for i in streams:
    if Stream ==i:
        streams = streams.index(i)
Hostel = int(Hostel)
HistoryOfBacklogs =int(HistoryOfBacklogs)
age = int(age)
Internships = int(Internships)
cgpa = int(cgpa)


def predict(): 
    x = {'Age': age,'Stream': streams,'Internships': Internships,'CGPA': cgpa,'Hostel':Hostel,'HistoryOfBacklogs': HistoryOfBacklogs}
    if int(prediction(x)) == 1: 
        st.success('Congratulations probably ,You will get placed :thumbsup:')
    else: 
        st.error('Sorry but, Probably you will not get placed :thumbsdown:') 

trigger = st.button('Predict', on_click=predict)