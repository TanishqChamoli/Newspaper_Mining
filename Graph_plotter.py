from pandas import DataFrame
import matplotlib.pyplot as plt
   
Data = {'Year': [8,7,6,5,4,3,2,1,30,29,28],
        'Unemployment_Rate': [8, 84, 85, 84, 82, 62, 84, 79, 74, 79, 94]
       }
  
df = DataFrame(Data,columns=['Year','Unemployment_Rate'])
df.plot(x ='Year', y='Unemployment_Rate', kind = 'scatter')
plt.show()