import pandas as pd
import joblib

from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/fitness.csv")

goal_encoder = LabelEncoder()
diet_encoder = LabelEncoder()
exp_encoder = LabelEncoder()

df["Fitness_Goal"] = goal_encoder.fit_transform(df["Fitness_Goal"])
df["Diet_Preference"] = diet_encoder.fit_transform(df["Diet_Preference"])
df["Experience_Level"] = exp_encoder.fit_transform(df["Experience_Level"])

X = df[
    [
        "Age",
        "Weight_KG",
        "Height_CM",
        "BMI",
        "Fitness_Goal",
        "Diet_Preference",
        "Experience_Level"
    ]
]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

nn = NearestNeighbors(
    n_neighbors=5
)

nn.fit(X_scaled)

joblib.dump(nn, "data/nn.pkl")

print("Nearest Neighbor Model Saved")