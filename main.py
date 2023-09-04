# conda install -c conda-forge fastapi uvicorn
import pickle
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# /api_v1/mlmodelwithregression with dict params
# method : post
@app.post('/api_v1/mlmodelwithregression')
def mlmodelwithregression(data: dict):
    print('data with dict {}'.format(data))
    # data dict to 변수 활당
    texture_mean = data['texture_mean']
    perimeter_mean = data['perimeter_mean']

    # pkl 파일 존재 확인 코드 필요

    result_predict = 0
    # 학습 모델 불러와 예측
    with open('datasets/BreastCancerWisconsin_Regression.pkl', 'rb') as regression_file:
        loaded_model = pickle.load(regression_file)
        input_labels = [[texture_mean, perimeter_mean]]  # 학습했던 설명변수 형식 맞게 적용
        result_predict = loaded_model.predict(input_labels)
        print('Predict radius_mean Result : {}'.format(result_predict))
        pass

    # 예측값 리턴
    result = {'radius_mean': result_predict[0]}
    return result

# postman: datatype: raw, json.
# body: {"texture_mean": 16.34, "perimeter_mean":87.21}
# returns data of "radius_mean": 13.454633198988523
