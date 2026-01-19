import sys
import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

print('arguements', sys.argv)
month = int(sys.argv[1])
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})


print(f"Hello pipeline, month:{month}")