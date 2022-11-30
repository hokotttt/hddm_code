import hddm
import numpy as np
from kabuki.analyze import gelman_rubin
#from IPython.parallel import Client

# print(hddm.__version__)


    data_stimcoding = hddm.load_csv("/Users/tiansuizi/Desktop/hoko/rhythm/hddm/exp9_hddm/data_stimcoding_25_2_longrt.txt")

    # model A
    m_stimcoding = hddm.HDDMStimCoding(data_stimcoding, include='z', stim_col='stim', split_param='v',
                            depends_on={'a': ['change_number', 'rhythm'], 'v': ['change_number', 'rhythm'],
                                        'z': ['change_number', 'rhythm'], 't': ['change_number', 'rhythm']})

    m_stimcoding.find_starting_values()
    m_stimcoding.sample(10000, burn=2000, dbname='modelA_traces', db='pickle')


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

combined_model=m_stimcoding
z_non_rhythm_0, z_non_rhythm_2, z_non_rhythm_4 = combined_model.nodes_db.node[['z(0.0)', 'z(2.0)', 'z(4.0)']]
z_rhythm_0, z_rhythm_2, z_rhythm_4 = combined_model.nodes_db.node[['z(0.1)', 'z(2.1)', 'z(4.1)']]
t_non_rhythm_0, t_non_rhythm_2, t_non_rhythm_4 = combined_model.nodes_db.node[['t(0.0)', 't(2.0)', 't(4.0)']]
t_rhythm_0, t_rhythm_2, t_rhythm_4 = combined_model.nodes_db.node[['t(0.1)', 't(2.1)', 't(4.1)']]
a_non_rhythm_0, a_non_rhythm_2, a_non_rhythm_4 = combined_model.nodes_db.node[['a(0.0)', 'a(2.0)', 'a(4.0)']]
a_rhythm_0, a_rhythm_2, a_rhythm_4 = combined_model.nodes_db.node[['a(0.1)', 'a(2.1)', 'a(4.1)']]
v_non_rhythm_0, v_non_rhythm_2, v_non_rhythm_4 = combined_model.nodes_db.node[['v(0.0)', 'v(2.0)', 'v(4.0)']]
v_rhythm_0, v_rhythm_2, v_rhythm_4 = combined_model.nodes_db.node[['v(0.1)', 'v(2.1)', 'v(4.1)']]

hddm.analyze.plot_posterior_nodes(
    [t_non_rhythm_0, t_non_rhythm_2, t_non_rhythm_4, t_rhythm_0, t_rhythm_2, t_rhythm_4])
plt.xlabel('non-decision time')
plt.ylabel('Posterior probability')
h = plt.legend(['Non-rhythm % change 0','Non-rhythm % change 2','Non-rhythm % change 4',
            'Rhythm % change 0','Rhythm % change 2','Rhythm % change 4'], frameon=False)
plt.title('Posterior of non-decision time (n=25)')

plt.show()
plt.savefig('hddm_non-decision time.pdf')

print("t: P(0:rhythm > nonrhythm) = %f"% np.array(t_non_rhythm_0.trace() < t_rhythm_0.trace()).mean())
print("t: P(2:rhythm > nonrhythm) = %f"% np.array(t_non_rhythm_2.trace() < t_rhythm_2.trace()).mean())
print("t: P(4:rhythm > nonrhythm) = %f"% np.array(t_non_rhythm_4.trace() < t_rhythm_4.trace()).mean())


hddm.analyze.plot_posterior_nodes(
    [z_non_rhythm_0, z_non_rhythm_2, z_non_rhythm_4, z_rhythm_0, z_rhythm_2, z_rhythm_4])
plt.xlabel('bias')
plt.ylabel('Posterior probability')
h = plt.legend(['Non-rhythm % change 0','Non-rhythm % change 2','Non-rhythm % change 4',
            'Rhythm % change 0','Rhythm % change 2','Rhythm % change 4'], frameon=False)
plt.show()
plt.title('Posterior of bias (n=25)')
plt.savefig('hddm_bias.pdf')

print("Z: P(0:rhythm > nonrhythm) = %f"% np.array(z_non_rhythm_0.trace() > z_rhythm_0.trace()).mean())
print("Z: P(2:rhythm > nonrhythm) = %f"% np.array(z_non_rhythm_2.trace() > z_rhythm_2.trace()).mean())
print("Z: P(4:rhythm > nonrhythm) = %f"% np.array(z_non_rhythm_4.trace() > z_rhythm_4.trace()).mean())



hddm.analyze.plot_posterior_nodes(
    [a_non_rhythm_0, a_non_rhythm_2, a_non_rhythm_4,a_rhythm_0, a_rhythm_2, a_rhythm_4])
plt.xlabel('threshold')
plt.ylabel('Posterior probability')

h = plt.legend(['Non-rhythm % change 0','Non-rhythm % change 2','Non-rhythm % change 4',
            'Rhythm % change 0','Rhythm % change 2','Rhythm % change 4'], frameon=False)

plt.title('Posterior of boundary (n=25)')
plt.show()
plt.savefig('hddm_boundary.pdf')


print("a: P(0:rhythm > nonrhythm) = %f"% np.array(a_non_rhythm_0.trace() < a_rhythm_0.trace()).mean())
print("a: P(2:rhythm > nonrhythm) = %f"% np.array(a_non_rhythm_2.trace() < a_rhythm_2.trace()).mean())
print("a: P(4:rhythm > nonrhythm) = %f"% np.array(a_non_rhythm_4.trace() < a_rhythm_4.trace()).mean())

hddm.analyze.plot_posterior_nodes(
    [v_non_rhythm_0, v_non_rhythm_2, v_non_rhythm_4, v_rhythm_0, v_rhythm_2, v_rhythm_4])
plt.xlabel('Drifting rate')
plt.ylabel('Posterior probability')
h = plt.legend(['Non-rhythm % change 0','Non-rhythm % change 2','Non-rhythm % change 4',
            'Rhythm % change 0','Rhythm % change 2','Rhythm % change 4'], frameon=False)
plt.title('Posterior of drifting rate (n=25)')

plt.show()
plt.savefig('hddm_drifting rate.pdf')

print("v: P(0:rhythm < nonrhythm) = %f"% np.array(v_non_rhythm_0.trace() > v_rhythm_0.trace()).mean())
print("v: P(2:rhythm < nonrhythm) = %f"% np.array(v_non_rhythm_2.trace() > v_rhythm_2.trace()).mean())
print("v: P(4:rhythm < nonrhythm) = %f"% np.array(v_non_rhythm_4.trace() > v_rhythm_4.trace()).mean())
