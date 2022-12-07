import joblib
def prediction(x_data):
    model = joblib.load("model.joblib")
    if x_data:
        print(x_data)
        y_pred = model.predict_one(x_data)      
        model = model.learn_one(x_data, y_pred)
        joblib.dump(model,"model.joblib")
    return y_pred

