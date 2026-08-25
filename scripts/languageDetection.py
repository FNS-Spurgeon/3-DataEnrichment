import pandas as pd
from langid import langid

list_lang = []
csv_file_path = "vol2-1826-1850-allusions.csv"
df = pd.read_csv(csv_file_path)

for i in df["Quotation"]:
    if type(i) == str:
        language = langid.classify(i)
        list_lang.append(language[0])
    else:
        list_lang.append("N/A")

df["language"] = list_lang
df.to_csv("vol2-1801-1825-allusions-enriched.csv", index=False)
