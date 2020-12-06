import numpy as np
from functions import *
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path



N = 14
w_num = 3
T = 20

resource_spend, resource_generation, pollution_removal = 0.1, 0.2, 0.9

resource_extraction = 0.04

agents = np.recarray((N), dtype=[('state', int), ('future', int), ('resource', float)])
w_resources = np.recarray((w_num), dtype=[('pollution', float), ('amount', float)])

agents_history = np.recarray((T, N), dtype=[('state', int), ('future', int), ('resource', float)])
w_resources_history = np.recarray((T, w_num), dtype=[('pollution', float), ('amount', float)])

interaction_history = []

results = pd.DataFrame( np.zeros( (1,3), int)  )
results.columns = ['t', 'agent', 'resource']




init_values( agents, w_resources )

#print(agents['state'])

for t in range(T):
    spend_time(agents, w_resources, resource_spend, resource_generation, pollution_removal)
    for i in range(N):
        interaction = get_resource(agents, i, w_resources, resource_extraction)
        
        if interaction:
            i, w_choice = interaction
            interaction_history.append( [t, i, w_choice] )
#            print('out=', agents['resource'])



    update(agents)    
    agents_history[t] = agents
    w_resources_history[t] = w_resources

        
        #spend_time(agents, w_resources)
interaction_history = pd.DataFrame( interaction_history )
interaction_history.columns = ['t', 'agent', 'w_resource']

target_dir = "../Results/"
Path( target_dir ).mkdir(parents=True, exist_ok=True)


np.save(target_dir + 'agents_history', agents_history)
np.save(target_dir + 'w_resources_history', w_resources_history)
interaction_history.to_csv(target_dir + 'interaction_history.csv', index = False)
