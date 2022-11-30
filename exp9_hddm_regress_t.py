import hddm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

m_regress_t = hddm.models.HDDMRegressor(data_regress,
                                  ["t ~ 1 + x2 + x3 + x4 + x5 + x6"],
                                  group_only_regressors=True, keep_regressor_trace=True)

m_regress_t.find_starting_values()
m_regress_t.sample(5000, burn=1000, dbname='modelB_1_traces_', db='pickle')

combined_model=m_regress_t

x1, x2, x3 = combined_model.nodes_db.node[['t_Intercept', 't_x2', 't_x3']]
x4, x5, x6 = combined_model.nodes_db.node[['t_x4', 't_x5', 't_x6']]
x1, x2, x3, x4, x5, x6 = x1.trace(), x2.trace(), x3.trace(), x4.trace(), x5.trace(), x6.trace()
t_non_rhythm_0 = x1
t_non_rhythm_2 = x1 + x2
t_non_rhythm_4 = x1 + x3
t_rhythm_0 = x1 + x4
t_rhythm_2 = x1 + x2 + x5
t_rhythm_4 = x1 + x3 + x6

t_rhythm=(x4 + x5 + x6) / 3

sns.set_context('talk', font_scale=1.5,rc={'line.linewidth':3.0})
plt.figure(figsize=(12, 9))
sns.kdeplot(t_rhythm_0, label="t_rhythnm_0: " + str(np.round(np.mean(t_rhythm_0), 3)))
sns.kdeplot(t_non_rhythm_0, label="t_non_rhythm_0: " + str(np.round(np.mean(t_non_rhythm_0), 3)))
sns.kdeplot(t_rhythm_2, label="t_rhythm_2: " + str(np.round(np.mean(t_rhythm_2), 3)))
sns.kdeplot(t_non_rhythm_2, label="t_non_rhythm_2: " + str(np.round(np.mean(t_non_rhythm_2), 3)))
sns.kdeplot(t_rhythm_4, label="t_rhythm_4: " + str(np.round(np.mean(t_rhythm_4), 3)))
sns.kdeplot(t_non_rhythm_4, label="t_non_rhythm_4: " + str(np.round(np.mean(t_non_rhythm_4), 3)))

sns.despine()#去掉边框
plt.xlabel('non-decision time')
plt.ylabel('Posterior probability')
h = plt.legend(['t_rhythm_0', 't_non_rhythm_0', 't_rhythm_2','t_non_rhythm_2','t_rhythm_4',
                't_non_rhythm_4'],bbox_to_anchor=(1, 1),prop={'size': 12})
plt.title('Posterior of non-decision time (n=25)')
plt.savefig('exp9_regress_t.pdf')

print("t:P(Rhythm > Non-Rhythm) = %f" % np.array((x4 + x5 + x6) / 3 > 0).mean())
print("t:(0:rhythm > nonrhythm) = %f" % np.array(x4 > 0).mean())
print("t:P(2:rhythm > nonrhythm) = %f" % np.array(x5 > 0).mean())
print("t:P(4:rhythm < nonrhythm) = %f" % np.array(x6 > 0).mean())
