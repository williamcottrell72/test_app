# Kickstarter!!!!!!!!!!!!!!!!!!
import numpy as np
import pickle
#import pandas







def make_prediction(features):

    #print(features['city'])
    # cit=features['city']
    # popularity=pop_dct[features['category']]

    # mnth=month_conv(features['month2'])
    #
    #
    # population=population_dct[cit]
    #
    # density=dct_density[cit]

    # print(f"The density is {density}")

    # X = np.array([features['goal2'], features['duration2'],mnth,features['num_levels'],popularity,density,population]).reshape(1,-1)
    # prob = pipeline.predict_proba(X)[0, 1]



    st=features['nature']
# print("IS this shit still working????")
#
# def make_prediction(features):
#
#     # X = np.array([features['population'], features['density'], features['popularity'],
#     #                features['level_num'], features['month'], features['duration'],
#     #                features['goal']]).reshape(1,-1)
#     prob = 12

    result = {
        'prediction': int(0 > 0.5),
        'prob_succeed': 0,
        'nature':st}
    return result


if __name__ == '__main__':
    print(make_prediction(example))
