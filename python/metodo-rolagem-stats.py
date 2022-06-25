import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Role Playing Games are an important hobby in my life, specially Dungeons and Dragons.
# There are many options for rolling stats in D&D and this code was written in order to analyse and compare
# 2 methods for rolling stats in the character creation segment of the game. Our in group discussion of wich method would be better generated this study.
# The "tradicional" method consists in rolling a 4d6 (4 6 sided dice), removing the smaller number rolled and sum the resulting three.
# The "novo" method consists in rolling 2d6, adding it together and than adding annother 6 on top of it.
# Each method has 1000 interactions as a sample and was compared simply by visualization.
# A Statystical test for comparing two means will be added.


# Defining s as the number of interactions
s = 1000

# Rolling the 'novo' method (2d6+6)
dado_1=np.random.random_integers(1,6,s)
dado_2=np.random.random_integers(1,6,s)

novo = dado_1 + dado_2 + 6


# Rolling the 'tradicional' method (4d6 minus the lower)
d1=np.random.random_integers(1,6,s)
d2=np.random.random_integers(1,6,s)
d3=np.random.random_integers(1,6,s)
d4=np.random.random_integers(1,6,s)

# Appending the 4 rolls in a list
lista=[]
aux=[]

for i in range(s):
    aux = [d1[i],d2[i],d3[i],d4[i]]
    lista.append(aux)
    aux=[]
    
# Removing the lower roll of the list    
for i in range(s):
    lista[i].remove(min(lista[i]))
    
# Sum the resulting 3 rolls    
tradicional = []
for i in range(s):
    aux = sum(lista[i])
    tradicional.append(aux)
    aux=[]


# Creating a Pandas DF to use the Describe function
df = pd.DataFrame(novo, columns=['novo'])
df['tradicional'] = tradicional

print(df.describe().T)

# Plotting the distributions of each method 
sns.displot(data=df,
            x="novo",
            kde=True)
plt.title('Método Novo')


sns.displot(data=df,
            x="tradicional",
            kde=True)
plt.title('Método Tradicional')