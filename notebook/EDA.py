
import pandas as pd
import ydata_profiling
from ydata_profiling import ProfileReport

file = "data/general_results.csv"
output_path = "output/rapport_general_results.html" 
df = pd.read_csv(file, sep=';')  

print(df.head())
print(df.shape)  # nombre de lignes / colonnes, utile à checker avant de lancer le profiling

profile = ProfileReport(df, title="Rapport de profiling - general_results") # analyse du dataframe et titre du rapport
profile.to_file(output_path)