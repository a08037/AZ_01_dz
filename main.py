import pandas as pd

# Загрузка файла с данными
file_path = 'dz.csv'  # Укажите путь к вашему файлу
df = pd.read_csv(file_path)

# Группировка данных по городу и расчет средней зарплаты
mean_salary_by_city = df.groupby('City')['Salary'].mean()

# Вывод результатов
print(mean_salary_by_city)
