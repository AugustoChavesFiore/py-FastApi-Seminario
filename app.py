from fastapi import FastAPI
#cors
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar los datos desde el archivo CSV
data = pd.read_csv("velocidad-max-viento.csv")

@app.get("/data")
def read_root(): 
    df=pd.DataFrame(data)
    df= df.drop_duplicates()
    stats = df['km/h'].describe()
    mean_speed_by_year = df.groupby(df['fecha'].str.slice(0, 4))['km/h'].mean()
    return {"stats": stats.to_dict(), "mean_speed_by_year": mean_speed_by_year.to_dict(), "data": df.to_dict()}