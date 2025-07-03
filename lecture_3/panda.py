import pandas as pd

print("\n")

# Example of reading a CSV file using pandas
csv_path='file1.csv'
df=pd.read_csv(csv_path)
print(df)

print("\n")

# Example of reading an Excel file using pandas
excel_path='file1.xlsx'
df_excel=pd.read_excel(excel_path)
df_excel.head()  # Display the first few rows of the DataFrame
print(df_excel)

print("\n")