!pip install pyxlsb
import pandas as pd    
import pyxlsb          
import numpy as np

dataframe = pd.read_excel("stc- Jawwy TV Data Set_T3.xlsb",index_col=0)
dataframe.shape
dataframe.head()
dataframe.describe()
dataframe.isnull().any()
import matplotlib.pyplot as plt
import plotly 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
movie_features_df=dataframe.pivot_table(index='program_name',columns='user_id_maped',values='rating').fillna(0)
movie_features_df.head()
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
movie_features_df_matrix = csr_matrix(movie_features_df.values)
model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
model_knn.fit(movie_features_df_matrix)
movie_features_df_selection= movie_features_df.reset_index()
movie_features_df_selection[['program_name']]
dataframe[['program_name']].head(10)

program_name='Moana'
recomendations=5
query_index = np.random.choice(movie_features_df.shape[0])
distances, indices = model_knn.kneighbors(movie_features_df.
                     iloc[movie_features_df_selection.index[movie_features_df_selection['program_name'] == program_name].tolist()[0],:].values.reshape(1, -1),
n_neighbors = recomendations+1)

for i in range(0, len(distances.flatten())):
    if i == 0:
        print('Recommendations for {0}:\n'.format(movie_features_df.index[movie_features_df_selection.index[movie_features_df_selection['program_name'] == program_name].tolist()[0]]))
    else:
        print('{0}: {1}, with distance of {2}:'.format(i, movie_features_df.index[indices.flatten()[i]], distances.flatten()[i]))
