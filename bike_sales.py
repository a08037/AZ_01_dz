import pandas as pd

# Загрузка данных из CSV
df_bike_sales = pd.read_csv('bike_sales_100k.csv')

# Вывод первых 5 строк
print(df_bike_sales.head())

# Вывод информации о данных
print(df_bike_sales.info())

# Статистическое описание данных
print(df_bike_sales.describe())
