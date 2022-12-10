import joblib
dictionary_list = joblib.load('dictionary_list.joblib')
print(dictionary_list)
x ={'Age': 14, 'Stream': 3, 'Internships': 0, 'CGPA': 5, 'Hostel': 0, 'HistoryOfBacklogs': 0}
for i in dictionary_list:
            if i == x:
                print("pass")