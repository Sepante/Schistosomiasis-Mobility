import numpy as np

N = 10
def init_values( agents, w_resources ):
    agents['resource'] = 1
    w_resources['amount'] = 1   
    agents['state'] = 0
    agents['future'] = 0

    w_resources['pollution'] = 0   
    
    N = len(agents)   
    
    seed = np.random.randint(N)   
    agents[seed]['state'] = 1
    agents[seed]['future'] = 1

    #print(seed)
    
def get_resource( agents, i, w_resources, resource_extraction ):
    #prob = np.exp( agents[i]['resource']) / ( agents[i]['resource'] +  ) )
    p = (1 - agents[i]['resource']) * ( 0.7 )
#    print(p)
#    print('before=', agents['resource'] )

    if np.random.random() < p:
        w_choice = np.random.randint( len(w_resources) )
        ###temp
        duration_spent = 1.2 - w_resources[w_choice]['amount']
        
        if agents[i]['state'] == 0:
            w_a_infection_prob = duration_spent * w_resources[w_choice]['pollution']
            #print('water to agent infection prob: ', w_a_infection_prob)
            if np.random.random() < w_a_infection_prob:
                agents[i]['future'] = 1
        
        elif agents[i]['state'] == 1:
            a_w_infection_prob = duration_spent
            w_resources[w_choice]['pollution'] += a_w_infection_prob
        
        agents[i]['resource'] = 1
        #print('extracted')

        if w_resources[w_choice]['amount'] >= resource_extraction:
            w_resources[w_choice]['amount'] -= resource_extraction
            
            
#        print(i, ' goes to ', w_choice)
#        print('in=', agents['resource'] )

        return i, w_choice

def update(agents):
    agents['state'] = agents['future']
            
def spend_time(agents, w_resources, resource_spend, resource_generation, pollution_removal):
    agents['resource'] -= resource_spend
    
#    w_resources['amount'] += resource_generation
    low_w_resources = np.where( w_resources['amount'] <= 1 )[0]
#    if len( low_w_resources ):
    w_resources[ low_w_resources ]['amount'] += resource_generation
    w_resources['pollution'] *= pollution_removal
    
        
        
        
        
        
        