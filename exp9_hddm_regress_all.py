import hddm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

##6个条件，a,v,t都放进去

data_regress1 = hddm.load_csv("/Users/tiansuizi/Desktop/hoko/rhythm/hddm/exp9_hddm/all_data_25_2.csv")
m_regress_1 = hddm.models.HDDMRegressor(data_regress1,
                                  ["v ~ 1 + x2 + x3 + x4 + x5 + x6",
                                        "a ~ 1 + x2 + x3 + x4 + x5 + x6",
                                        "t ~ 1 + x2 + x3 + x4 + x5 + x6"],
                        group_only_regressors=False, keep_regressor_trace=True)

m_regress_1.find_starting_values()
m_regress_1.sample(5000, burn=1000, dbname='modelB_1_traces_', db='pickle')

combined_model=m_regress_1

##plot v
x1, x2, x3 = combined_model.nodes_db.node[['v_Intercept', 'v_x2', 'v_x3']]
x4, x5, x6 = combined_model.nodes_db.node[['v_x4', 'v_x5', 'v_x6']]
x1, x2, x3, x4, x5, x6 = x1.trace(), x2.trace(), x3.trace(), x4.trace(), x5.trace(), x6.trace()
v_non_rhythm_0 = x1
v_non_rhythm_2 = x1 + x2
v_non_rhythm_4 = x1 + x3
v_rhythm_0 = x1 + x4
v_rhythm_2 = x1 + x2 + x5
v_rhythm_4 = x1 + x3 + x6

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
plt.savefig('exp9_regressall_v.pdf')


print("v:P(Rhythm < Non-Rhythm) = %f" % np.array((x4 + x5 + x6) / 3 < 0).mean())
print("v:P(0:rhythm < nonrhythm) = %f" % np.array(x4 < 0).mean())
print("v:P(2:rhythm < nonrhythm) = %f" % np.array(x5 < 0).mean())
print("v:P(4:rhythm < nonrhythm) = %f" % np.array(x6 < 0).mean())

###plot a###
x1, x2, x3 = combined_model.nodes_db.node[['a_Intercept', 'a_x2', 'a_x3']]
x4, x5, x6 = combined_model.nodes_db.node[['a_x4', 'a_x5', 'a_x6']]
x1, x2, x3, x4, x5, x6 = x1.trace(), x2.trace(), x3.trace(), x4.trace(), x5.trace(), x6.trace()
a_non_rhythm_0 = x1
a_non_rhythm_2 = x1 + x2
a_non_rhythm_4 = x1 + x3
a_rhythm_0 = x1 + x4
a_rhythm_2 = x1 + x2 + x5
a_rhythm_4 = x1 + x3 + x6

a_rhythm=(x4 + x5 + x6) / 3



sns.set_context('talk', font_scale=1.5,rc={'line.linewidth':3.0})
plt.figure(figsize=(12, 9))
sns.kdeplot(a_rhythm_0, label="a_rhythnm_0: " + str(np.round(np.mean(a_rhythm_0), 3)))
sns.kdeplot(a_non_rhythm_0, label="a_non_rhythm_0: " + str(np.round(np.mean(a_non_rhythm_0), 3)))
sns.kdeplot(a_rhythm_2, label="a_rhythm_2: " + str(np.round(np.mean(a_rhythm_2), 3)))
sns.kdeplot(a_non_rhythm_2, label="a_non_rhythm_2: " + str(np.round(np.mean(a_non_rhythm_2), 3)))
sns.kdeplot(a_rhythm_4, label="a_rhythm_4: " + str(np.round(np.mean(a_rhythm_4), 3)))
sns.kdeplot(a_non_rhythm_4, label="a_non_rhythm_4: " + str(np.round(np.mean(a_non_rhythm_4), 3)))

sns.despine()#去掉边框
plt.xlabel('response boundary')
plt.ylabel('Posterior probability')
h = plt.legend(['a_rhythm_0', 'a_non_rhythm_0', 'a_rhythm_2','a_non_rhythm_2','a_rhythm_4',
                'a_non_rhythm_4'],bbox_to_anchor=(1, 1),prop={'size': 12})
plt.title('Posterior of respone boundary (n=25)')
plt.savefig('exp9_regressall_a.pdf')


# hypothesis testing

print("a:P(Rhythm > Non-Rhythm) = %f" % np.array((x4 + x5 + x6) / 3 > 0).mean())
print("a:(0:rhythm > nonrhythm) = %f" % np.array(x4 > 0).mean())
print("a:P(2:rhythm > nonrhythm) = %f" % np.array(x5 > 0).mean())
print("a:P(4:rhythm > nonrhythm) = %f" % np.array(x6 > 0).mean())


#plot t
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
plt.savefig('exp9_regressall_t.pdf')

print("t:P(Rhythm > Non-Rhythm) = %f" % np.array((x4 + x5 + x6) / 3 > 0).mean())
print("t:(0:rhythm > nonrhythm) = %f" % np.array(x4 > 0).mean())
print("t:P(2:rhythm > nonrhythm) = %f" % np.array(x5 > 0).mean())
print("t:P(4:rhythm > nonrhythm) = %f" % np.array(x6 > 0).mean())

m_regress_1.save('model_regress_all_1')

m = hddm.load('model_regress_all_1')

m_regress_1=hddm.load("/Users/tiansuizi/Desktop/hoko/rhythm/hddm/exp9_hddm/hddm_regress/hddm_regress_vat_all/model_regress_all_1")