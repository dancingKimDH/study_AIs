concavity_mean = float(input('Concavity Mean : '))
perimeter_worst = float(input('Perimeter Worst : '))

import pickle

with open('codes/datasets/BreastCancerWisconsin_Regression.pkl', 'rb') as regression_file:
    loaded_model = pickle.load(regression_file)
    input_labels = [[concavity_mean, perimeter_worst]]
    result_predict = loaded_model.predict(input_labels)
    print('Predict Diagnosis : {}'.format(result_predict))