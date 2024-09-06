from sklearn.cluster import KMeans

def apply_kmeans(rfm_scaled, n_clusters=4):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(rfm_scaled)
    return kmeans

