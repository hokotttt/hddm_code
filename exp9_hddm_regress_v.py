import hddm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data_regress1 = hddm.load_csv("/Users/tiansuizi/Desktop/hoko/rhythm/hddm/exp9_hddm/all_data_25_2.csv")

m_regress_v = hddm.models.HDDMRegressor(data_regress,
                                  ["v ~ 1 + x2 + x3 + x4 + x5 + x6"],
                                  group_only_regressors=True, keep_regressor_trace=True)

m_regress_v.find_starting_values()
m_regress_v.sample(5000, burn=1000, dbname='modelB_1_traces_', db='pickle')

combined_model=m_regress_v

x1, x2, x3 = combined_model.nodes_db.node[['v_Intercept', 'v_x2', 'v_x3']]
x4, x5, x6 = combined_model.nodes_db.node[['v_x4', 'v_x5', 'v_x6']]
x1, x2, x3, x4, x5, x6 = x1.trace(), x2.trace(), x3.trace(), x4.trace(), x5.trace(), x6.trace()
v_non_rhythm_0 = x1
v_non_rhythm_2 = x1 + x2
v_non_rhythm_4 = x1 + x3
v_rhythm_0 = x1 + x4
v_rhythm_2 = x1 + x2 + x5
v_rhythm_4 = x1 + x3 + x6

v_rhythm=(x4 + x5 + x6) / 3
# hypothesis testing
# print("P(Rhythm > Non-Rhythm) = %f" % np.array((x4 + x5 + x6) / 3 < 0).mean())
# print("P(change 2 > change 0) = %f" % np.array(x2 > 0).mean())
# print("P(change 4 < change 0) = %f" % np.array((x3 - x2) > 0).mean())
# print("P(change 4 2 0 is different) = %f" % np.logical_or(np.array((x3 - x2) > 0),np.array(x2 > 0)).mean())

print("P(Rhythm < Non-Rhythm) = %f" % np.array((x4 + x5 + x6) / 3 < 0).mean())
print("P(0:rhythm < nonrhythm) = %f" % np.array(x4 < 0).mean())
print("P(2:rhythm < nonrhythm) = %f" % np.array(x5 < 0).mean())
print("P(4:rhythm < nonrhythm) = %f" % np.array(x6 < 0).mean())



sns.set_context('talk', font_scale=1.5,rc={'line.linewidth':3.0})
plt.figure(figsize=(12, 9))
sns.kdeplot(v_rhythm_0, label="v_rhythnm_0: " + str(np.round(np.mean(v_rhythm_0), 3)))
sns.kdeplot(v_non_rhythm_0, label="v_non_rhythm_0: " + str(np.round(np.mean(v_non_rhythm_0), 3)))
sns.kdeplot(v_rhythm_2, label="v_rhythm_2: " + str(np.round(np.mean(v_rhythm_2), 3)))
sns.kdeplot(v_non_rhythm_2, label="v_non_rhythm_2: " + str(np.round(np.mean(v_non_rhythm_2), 3)))
sns.kdeplot(v_rhythm_4, label="v_rhythm_4: " + str(np.round(np.mean(v_rhythm_4), 3)))
sns.kdeplot(v_non_rhythm_4, label="v_non_rhythm_4: " + str(np.round(np.mean(v_non_rhythm_4), 3)))

sns.despine()#去掉边框
plt.xlabel('Drifting rate')
plt.ylabel('Posterior probability')
h = plt.legend(['v_rhythm_0', 'v_non_rhythm_0', 'v_rhythm_2','v_non_rhythm_2','v_rhythm_4',
                'v_non_rhythm_4'],bbox_to_anchor=(1, 1),prop={'size': 12})
plt.title('Posterior of drift-rate (n=25)')
plt.savefig('exp9_regress_v.pdf')

############################################








