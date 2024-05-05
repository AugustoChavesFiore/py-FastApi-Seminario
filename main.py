import pandas as pd
import matplotlib.pyplot as plt

data_csv = pd.read_csv('velocidad-max-viento.csv', encoding='utf-8')


df=pd.DataFrame(data_csv)

df= df.drop_duplicates()

# Calcular estadísticas descriptivas de la velocidad del viento en nudos
print("Estadísticas descriptivas de la velocidad del viento en nudos:")
print(df['km/h'].describe())


mean_speed_by_year = df.groupby(df['fecha'].str.slice(0, 4))['km/h'].mean()
print("Media de la velocidad del viento en km/h por año:")


mean_speed_by_year.plot(kind='line', title='Media de velocidad del viento por año (km/h)')
plt.xlabel('Año')
plt.ylabel('Velocidad del viento (km/h)')
plt.grid()
plt.show()



