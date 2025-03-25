import os 

folder_path=os.path.join(os.getcwd(),'artifacts')
data_ingestion=os.path.join(folder_path,'data_ingestion')

print(f"Creating main directory at {folder_path}")
print(f"Creating data ingestion directory at {data_ingestion}")
os.makedirs(folder_path,exist_ok=True)
os.makedirs(data_ingestion,exist_ok=True)

