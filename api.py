# Kickstarter!!!!!!!!!!!!!!!!!!
import numpy as np
import pickle

pipeline=pickle.load(open('./model/gscv_rf.pkl','rb'))
# pipeline=pickle.load(open('./model/dummy.pkl','rb'))


example = {
  'goal': 3,  # int
  'duration': 4,    # M or F
  'month': 22,    # int
  'level_num': 1,  # int
  'popularity': 0,  # int
  'density': 7.25,
   'population': 10# float
}

def make_prediction(features):
    X = np.array([features['population'], features['density'], features['popularity'],
                   features['level_num'], features['month'], features['duration'],
                   features['goal']]).reshape(1,-1)
    prob = pipeline.predict_proba(X)[0, 1]
    prob = features['population']+features['density']

# print("IS this shit still working????")
#
# def make_prediction(features):
#
#     # X = np.array([features['population'], features['density'], features['popularity'],
#     #                features['level_num'], features['month'], features['duration'],
#     #                features['goal']]).reshape(1,-1)
#     prob = 12

    result = {
        'prediction': int(prob > 0.5),
        'prob_succeed': prob}
    return result


if __name__ == '__main__':
    print(make_prediction(example))
