import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

from sklearn_extra.cluster import KMedoids

data = {
    'Umur': [20, 22, 25, 27, 30, 35, 40, 42, 45, 50],
    'Pengeluaran': [2, 3, 2.5, 3.5, 4, 7, 8, 7.5, 9, 10]
}

df = pd.DataFrame(data)

print(df)

X = df[['Umur', 'Pengeluaran']]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


inertia = []

for k in range(1, 10):
    model = KMeans(
        n_clusters=k,
        random_state=42
    )

    model.fit(X_scaled)

    inertia.append(model.inertia_)

plt.plot(range(1,10), inertia, marker='o')
plt.xlabel("Jumlah Cluster")
plt.ylabel("Inertia")
plt.title("Metode Elbow")
plt.show()

for k in range(2,6):

    model = KMeans(
        n_clusters=k,
        random_state=42
    )

    labels = model.fit_predict(X_scaled)

    score = silhouette_score(
        X_scaled,
        labels
    )

    print(f"K={k}, Score={score:.3f}")

kmeans = KMeans(
    n_clusters=2,
    random_state=42
)

df['Cluster'] = kmeans.fit_predict(X_scaled)
print(df)

plt.scatter(
    df['Umur'],
    df['Pengeluaran'],
    c=df['Cluster']
)

plt.xlabel("Umur")
plt.ylabel("Pengeluaran")
plt.title("Hasil Clustering")
plt.show()

print(kmeans.cluster_centers_)


#kmedoid
from sklearn_extra.cluster import KMedoids

kmedoids = KMedoids(
    n_clusters=2,
    random_state=42
)

df['Cluster'] = kmedoids.fit_predict(X_scaled)

print(kmedoids.medoid_indices_)

print(df.iloc[kmedoids.medoid_indices_])