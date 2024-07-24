
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity


# Read the CSV file into a DataFrame
df = pd.read_csv('small.csv')

# Features to be used for similarity calculation
features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

# Create a graph
G = nx.Graph()

# Add nodes for each song
for idx, row in df.iterrows():
    G.add_node(row['track_name'], emotion=row['emotion'])

# Calculate similarity based on Euclidean distance
def calculate_similarity(song1, song2):
    # Select features for the two songs
    features1 = [song1[feature] for feature in features]
    features2 = [song2[feature] for feature in features]

    # Calculate Euclidean distance as dissimilarity metric
    similarity = euclidean_distances([features1], [features2])[0][0]
    return similarity

# Add edges between songs based on similarity
for i in range(len(df)):
    for j in range(i+1, len(df)):
        similarity = calculate_similarity(df.iloc[i], df.iloc[j])
        if similarity > 0.9995:  # Adjust this threshold based on your needs
            G.add_edge(df.iloc[i]['track_name'], df.iloc[j]['track_name'], weight=similarity)


# with open("similarity_scores.txt", "w") as file:
#     # Iterate over all pairs of songs
#     for i in range(len(df)):
#         for j in range(i+1, len(df)):
#             # Calculate similarity
#             similarity = calculate_similarity(df.iloc[i], df.iloc[j])
#             # Write similarity score to the file
#             file.write(f"Song 1: {df.iloc[i]['track_name']}, Song 2: {df.iloc[j]['track_name']}, Similarity: {similarity}\n")


# Visualization
pos = nx.spring_layout(G)  # Positioning nodes using spring layout algorithm
nx.draw(G, pos, with_labels=True, font_size=8, node_size=100)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)
plt.show()

# import networkx as nx

# # Assuming G is your graph object

# # Save the graph to a file
# nx.write_graphml(G, "graph_data.graphml")
