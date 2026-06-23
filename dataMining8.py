import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

from sklearn_extra.cluster import KMedoids

X, y_true = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=0.6,
    random_state=42
)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=4,
    init='k-means++',
    n_init=10,
    max_iter=300,
    random_state=42
)

y_kmeans = kmeans.fit_predict(X_scaled)

print("=== K-MEANS ===")
print("Centroid:")
print(kmeans.cluster_centers_)
print("Inertia:", kmeans.inertia_)
print("Iterasi:", kmeans.n_iter_)

inertias = []
k_range = range(2, 11)

for k in k_range:
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    model.fit(X_scaled)
    inertias.append(model.inertia_)

plt.figure(figsize=(8,5))
plt.plot(k_range, inertias, 'bo-')
plt.title('Elbow Method')
plt.xlabel('Jumlah Cluster (k)')
plt.ylabel('Inertia')
plt.show()

diffs = np.diff(inertias)
diffs2 = np.diff(diffs)

optimal_k = np.argmax(diffs2) + 3
print("Optimal k (Elbow):", optimal_k)

sil_scores = []

for k in range(2,11):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    sil_scores.append(
        silhouette_score(X_scaled, labels)
    )

plt.figure(figsize=(8,5))
plt.plot(range(2,11), sil_scores, 'ro-')
plt.title('Silhouette Score')
plt.xlabel('Jumlah Cluster (k)')
plt.ylabel('Score')
plt.show()

print(
    "Optimal k (Silhouette):",
    np.argmax(sil_scores)+2
)

print(
    "Best Score:",
    max(sil_scores)
)


plt.figure(figsize=(8,6))

plt.scatter(
    X_scaled[:,0],
    X_scaled[:,1],
    c=y_kmeans,
    cmap='viridis'
)

plt.scatter(
    kmeans.cluster_centers_[:,0],
    kmeans.cluster_centers_[:,1],
    color='red',
    marker='x',
    s=200
)

plt.title("K-Means Clustering")
plt.show()

outliers = np.array([
    [8,8],
    [9,9],
    [-3,8],
    [5,-4]
])

X2 = np.vstack([X, outliers])

X2_scaled = StandardScaler().fit_transform(X2)

kmeans2 = KMeans(
    n_clusters=3,
    random_state=42
)

kmedoids = KMedoids(
    n_clusters=3,
    random_state=42
)

labels_kmeans = kmeans2.fit_predict(X2_scaled)
labels_kmedoids = kmedoids.fit_predict(X2_scaled)

fig, axes = plt.subplots(1,2, figsize=(12,5))

axes[0].scatter(
    X2_scaled[:,0],
    X2_scaled[:,1],
    c=labels_kmeans,
    cmap='viridis'
)

axes[0].set_title("K-Means")

axes[1].scatter(
    X2_scaled[:,0],
    X2_scaled[:,1],
    c=labels_kmedoids,
    cmap='viridis'
)

axes[1].set_title("K-Medoids")

plt.show()

print("\n=== PERBANDINGAN ===")
print("K-Means Inertia :", kmeans2.inertia_)
print("K-Medoids Inertia :", kmedoids.inertia_)