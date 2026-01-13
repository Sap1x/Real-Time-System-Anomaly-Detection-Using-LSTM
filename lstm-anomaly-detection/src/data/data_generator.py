import numpy as np
import pandas as pd

def generate_system_data(
    n_samples=10000,
    anomaly_ratio=0.05,
    seed=42
):
    np.random.seed(seed)

    time = np.arange(n_samples)

    cpu = np.random.normal(50, 10, n_samples)
    memory = np.random.normal(60, 8, n_samples)
    network = np.random.normal(100, 20, n_samples)

    data = pd.DataFrame({
        "time": time,
        "cpu": cpu,
        "memory": memory,
        "network": network,
        "anomaly": 0
    })

    # Inject anomalies
    n_anomalies = int(n_samples * anomaly_ratio)
    anomaly_indices = np.random.choice(n_samples, n_anomalies, replace=False)

    data.loc[anomaly_indices, "cpu"] += np.random.normal(50, 10, n_anomalies)
    data.loc[anomaly_indices, "memory"] += np.random.normal(40, 10, n_anomalies)
    data.loc[anomaly_indices, "network"] += np.random.normal(80, 20, n_anomalies)
    data.loc[anomaly_indices, "anomaly"] = 1

    return data


if __name__ == "__main__":
    df = generate_system_data()
    df.to_csv("data/simulated/system_metrics.csv", index=False)
    print("✅ Simulated system metrics generated")
