import library0_01 as lb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print(lb.AND(0,0))
print(lb.AND(1,0))
print(lb.AND(0,1))
print(lb.AND(1,1))
print()
print(lb.NAND(0,0))
print(lb.NAND(1,0))
print(lb.NAND(0,1))
print(lb.NAND(1,1))
print()
print(lb.OR(0,0))
print(lb.OR(1,0))
print(lb.OR(0,1))
print(lb.OR(1,1))
print()
print(lb.XOR(0,0))
print(lb.XOR(1,0))
print(lb.XOR(0,1))
print(lb.XOR(1,1))

x = np.arange(-5, 5, 0.1)

fig = plt.figure()
plt.plot(x, lb.step_func(x))

fig = plt.figure()
plt.plot(x, lb.sigmoid(x))

fig = plt.figure()
y1 = lb.sigmoid(x)
y2 = lb.step_func(x)
plt.plot(x, y1, label = 'sigmoid')
plt.plot(x, y2, linestyle = '--', label = 'step_function')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-0.1, 1.1)

fig = plt.figure()
plt.plot(x, lb.relu(x))

df = pd.read_table('data\\movies.dat', sep = '::',
                   header = None, names = ['movies_id',
                                           'title',
                                           'genres'])
df['genres'] = df['genres'].str.split('|')

all_genres = []
for genres in df['genres']:
    all_genres.extend(genres)
    
uni_genres = list(set(all_genres))
genre_list = sorted(uni_genres)

for genre in genre_list:
    target_genre = 'Genre_' + genre
    df[target_genre] = df['genres'].apply(lambda x:
                                          lb.genre_to_binary(x,genre))
        
print(df)

df2 = pd.read_table('data\\movies.dat', sep = '::',
                   header = None, names = ['movies_id',
                                           'title',
                                           'genres'])
genres_split = df2['genres'].str.get_dummies('|')

genres_columns = genres_split.columns

for col in genres_columns:
    df2[f'Genres_{col}'] = genres_split[col]
    
print(df2)

df = pd.read_table('data\\movies.dat', sep = '::',
                   header = None, names = ['movies_id',
                                           'title',
                                           'genres'])

df_dummies = df['genres'].str.get_dummies(sep = '|')

df_dummies = df_dummies.add_prefix('Genres_')
movies_windic = df.join(df_dummies)
print(movies_windic)