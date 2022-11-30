import hddm
import numpy as np
#from IPython.parallel import Client
import multiprocessing as mp


#fit
def run_model(id):
    import hddm
    import os
    os.chdir('/Users/tiansuizi/Desktop/hoko/rhythm/hddm/exp9_hddm/hddm_regress/hddm_regress_oneparm')
    data_regress=hddm.load_csv("/Users/tiansuizi/Desktop/hoko/rhythm/hddm/exp9_hddm/all_data_25_2.csv")
    m_regress_a = hddm.models.HDDMRegressor(data_regress,
                                  ["a ~ 1 + x2 + x3 + x4 + x5 + x6"],
                                  group_only_regressors=True, keep_regressor_trace=True)

    m_regress_a.find_starting_values()
    m_regress_a.sample(5000, burn=1000, dbname='hddm_regress_a_traces_Chain%i'%id, db='pickle')
    m_regress.save('model_hddm_regress_a_%i'%id)
    return id

if __name__ == '__main__':
    p1=mp.Process(target=run_model,args=(1, ))
    p2=mp.Process(target=run_model,args=(2, ))
    p3=mp.Process(target=run_model,args=(3, ))



    # starting process 1&2&3
    p1.start()
    p2.start()
    p3.start()

    # wait until process 1&2 is finished
    p1.join()
    p2.join()
    p3.join()





