import pandas

f = pandas.read_csv("C:/Users/Usuario/Desktop/ANA/UNIVERSIDAD/SEGUNDO/PROGRAMACION SIN CALVO/TRABAJO FINAL ARCHIVOS/air_traffic_data.csv")

print(f.head)

for i in range(10):
    print(f["Operating Airline"][i])

print(f.iloc[2,1])