#!/usr/bin/env python3
""" clustering and similarities"""
from sklearn.preprocessing import StandardScaler

# from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans


def get_recommendations(data, name, features, n=5):
    """recommend similar artists or tracks"""

    # Drop rows with missing popularity
    data = data.dropna(axis=0, subset=["popularity"])

    X = data[features].values  # Extract feature values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    # cosine_matrix = cosine_similarity(X_scaled)

    recommender = NearestNeighbors(n_neighbors=n + 1).fit(X_scaled)
    distance, indices = recommender.kneighbors(X_scaled)

    artist_index = data[data["name"] == name].index[0]  # fetch first accurence

    recommendations = data.iloc[indices[artist_index][1:], :]["id"]

    return recommendations


def get_cluster_artists(data, features, N_CLUSTERS=5):
    """Recommend similar artists or tracks"""

    sublist = ["popularity", "follower", "nb_album"]
    # Drop rows with missing popularity
    data = data.dropna(axis=0, subset=features)

    X = data[features].values  # Extract feature values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model_cluster = KMeans(n_clusters=N_CLUSTERS).fit(X_scaled)

    cluster_labels = model_cluster.labels_
    names = data["id"].to_list()
    clusters = {i: [] for i in range(N_CLUSTERS)}

    for i, label in enumerate(cluster_labels):
        clusters[label].append(names[i])

    return clusters
