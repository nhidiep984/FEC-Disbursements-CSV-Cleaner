import pandas as pd

file_path = input("Input file path: ")
df = pd.read_csv(file_path, low_memory=False)
df2 = df[['committee_name', 'report_year', 'report_type', 'entity_type_desc','recipient_name','disbursement_description','disbursement_amount']]
df2.to_csv('cleaned_file.csv', index=False)



