import pandas as pd
import openpyxl


workbook = openpyxl.load_workbook('app/schedule/handler/xlsx/1k_18.11-23.11.2024.xlsx')
sheet = workbook.active

# Читаем данные в DataFrame (удобный формат для визуализации)
data = pd.DataFrame(sheet.values)

print(data.head())