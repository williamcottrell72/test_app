# Kickstarter!!!!!!!!!!!!!!!!!!
import numpy as np
import pickle
import pandas

pipeline=pickle.load(open('./model/gscv_rf.pkl','rb'))
# pipeline=pickle.load(open('./model/dummy.pkl','rb'))
df_city=pickle.load(open('./model/city_density.pkl','rb'))
pop_dct=pickle.load(open('./model/pop_dct','rb'))

dct_density={df_city.iloc[i,0]:df_city.iloc[i,1] for i in range(len(df_city))}
dct_pop={df_city.iloc[i,0]:df_city.iloc[i,1] for i in range(len(df_city))}


# features['population'], features['density']

example = {
  'goal': 3,  # int
  'duration': 4,    # M or F
  'month': 22,    # int
  'level_num': 1,  # int
  'popularity': 0,  # int
  'density': 7.25,
   'population': 10# float
}





def month_conv(x):
    if x=='Jan':
        return 1
    elif x=='Feb':
        return 2
    elif x=='Mar':
        return 3
    elif x=='Apr':
        return 4
    elif x=='May':
        return 5
    elif x=='June':
        return 6
    elif x=='July':
        return 7
    elif x=='Aug':
        return 8
    elif x=='Sep':
        return 9
    elif x=='Oct':
        return 10
    elif x=='Nov':
        return 11
    elif x=='Dec':
        return 12


def make_prediction(features):

    #print(features['city'])
    cit=features['city']
    popularity=dct_pop[cit]

    mnth=month_conv(features['month2'])




    density=dct_density[cit]
    print(f"The density is {density}")
    pop=dct_pop[cit]
    X = np.array([pop, density,popularity,
                   features['num_levels'], mnth, features['duration2'],
                   features['goal2']]).reshape(1,-1)
    prob = pipeline.predict_proba(X)[0, 1]
    # prob = features['population']+features['density']

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
