import pandas as pd

data = {'distritos': ['hyo', 'tambo', 'chilca', 'cajas', 'hualhas'],
        'pob': [1000, 500, 300, 200, 100],
        'parques': [2, 3, 2, 2, 2]
        }

df = pd.DataFrame(data)

print('DataFrame: ')
print(df)
print()

print(df[(df['pob'] > 250) & (df['distritos'] == 'tambo')])


