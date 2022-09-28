import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import preprocessing





#Data import
penangHousing = pd.read_csv('housing.csv')

#print(penangHousing.head())
penangHousing = pd.DataFrame(penangHousing)
#print(penangHousing)

#Data Preprocessing

label = preprocessing.LabelEncoder()

#Price
penangHousing['Price'] = penangHousing['Price'].str.replace('RM','')
penangHousing['Price'] = penangHousing['Price'].str.replace(" ",'')
penangHousing['Price'] = penangHousing['Price'].astype(float)

#Location
penangHousing['Location'] = label.fit_transform(list(penangHousing['Location']))
penangHousing['Location'] = penangHousing['Location'].astype(float)
#BuildArea
penangHousing['BuildArea'] = penangHousing['BuildArea'].str.replace('sq.ft.','')
penangHousing['BuildArea'] = penangHousing['BuildArea'].str.replace(" ",'')
penangHousing['BuildArea'] = penangHousing['BuildArea'].astype(float)

#noOfBedrooms
penangHousing['NoOfBedrooms'] = label.fit_transform(list(penangHousing['NoOfBedrooms']))
penangHousing['NoOfBedrooms'] = penangHousing['NoOfBedrooms'].astype(float)
#noOfBathrooms
penangHousing['NoOfBathrooms'] = label.fit_transform(list(penangHousing['NoOfBathrooms']))
penangHousing['NoOfBathrooms'] = penangHousing['NoOfBathrooms'].astype(float)

penangHousing.to_csv('housingData_clean.csv')