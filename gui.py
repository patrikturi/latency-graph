import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from threading import Timer

data1 = {'Country': ['US','CA','GER','UK','FR'],
         'GDP_Per_Capita': [45000,42000,52000,49000,47000]
        }
df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])


data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
         'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
        }
df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])


data3 = {'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],
         'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
        }  
df3 = DataFrame(data3,columns=['Interest_Rate','Stock_Index_Price'])
 

root= tk.Tk()

# TODO: interpolate https://stackoverflow.com/questions/61645402/smoothing-out-a-line-chart-with-matplotlib


figure2 = plt.Figure(figsize=(12,6), dpi=100)
ax2 = figure2.add_subplot(111, ylim=(0,14)) # min y
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
df.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('Year Vs. Unemployment Rate')

def tick():
    print('.')
    ax2.clear()
    data2['Unemployment_Rate'][3] = 15.0
    df2.update(data2)
    df = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
    df.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
    line2.draw()

root.after(1000, tick)
root.mainloop()
