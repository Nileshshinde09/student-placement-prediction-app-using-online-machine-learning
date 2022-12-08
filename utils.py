import joblib
import streamlit as st
class utils:
    def __init__(self,age:int,streams:int,Internships:int,cgpa:int
                ,Hostel:int,HistoryOfBacklogs:int) -> None:
           
        def prediction(x_data) -> bool:
            model = joblib.load("model.joblib")
            if x_data:
                print(x_data)
                y_pred = model.predict_one(x_data)      
                model = model.learn_one(x_data, y_pred)
                joblib.dump(model,"model.joblib")
            return y_pred

        def predict()->None:
            x = {'Age': age,'Stream': streams,'Internships': Internships,'CGPA': cgpa,'Hostel':Hostel,'HistoryOfBacklogs': HistoryOfBacklogs}
            if int(prediction(x)): 
                st.success('Congratulations probably ,You will get placed :thumbsup:')
            else: 
                st.error('Sorry but, Probably you will not get placed :thumbsdown:') 

        st.button('Predict', on_click=predict)

class processing(utils):
    def __init__(self,Stream:int,streams:int,cgpa:int,
                Internships:int,age:int,HistoryOfBacklogs:int,Hostel:int) -> None:
        for i in streams:
            if Stream ==i:
                streams = streams.index(i)
        Hostel = int(Hostel)
        HistoryOfBacklogs =int(HistoryOfBacklogs)
        age = int(age)
        Internships = int(Internships)
        cgpa = int(cgpa)
        utils(age,streams,Internships,cgpa,Hostel,HistoryOfBacklogs)
    

        
