import numpy as np                                                                                                         
import plotext as pt                                                                                                      
np.random.seed(31)                                                                                                         
n=10                                                                                                                        
p = np.arange(0.1,1.1,0.1)                                                                                                 
samples = 1000                                                                                                         
                                                                                                                        
emperical_probability = []                                                                                                  
analytical_probability = []                                                                                                
                                                                                                                            
for pr in p :                                                                                                              
    sucess = 0                                                                                                           
    analytical = n*p*(1-p)**n-1                                                                                             
    analytical_probability.append(analytical)   
