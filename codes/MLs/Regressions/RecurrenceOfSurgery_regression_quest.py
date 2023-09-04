bone_density = float(input('골밀도 : '))
duration_of_pain = float(input('통증기간(월) : '))

import pickle

with open('codes/datasets/RecurrenceOfSurgery_Regression.pkl', 'rb') as regression_file:
    loaded_model = pickle.load(regression_file)
    input_labels = [[bone_density, duration_of_pain]]
    result_predict = loaded_model.predict(input_labels)
    print('Predict Age Result : {}'.format(result_predict))
    