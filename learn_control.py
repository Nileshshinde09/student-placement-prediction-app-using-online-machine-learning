
import joblib

class learn_control:
    dictionary_list = []
    def learn_control_processing(x):
        dictionary_list = joblib.load('dictionary_list.joblib')
        cont = 0
        if len(dictionary_list)<9:
            dictionary_list.append(x)
        else:
            dictionary_list.pop(0)
            dictionary_list.append(x)
        print(len(dictionary_list))
        for i in dictionary_list:
            if i == x:
                cont +=1
        joblib.dump(dictionary_list,'dictionary_list.joblib')
        if cont >=3:
            return -1
        else:
            return 1
    

