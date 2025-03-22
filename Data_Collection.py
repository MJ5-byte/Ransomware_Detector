import psutil
import time
import pandas as pd
import random

# Define parameters
data = []
labels = []  # 0 = Normal, 1 = Ransomware-like activity

# Collect normal activity (safe behavior)
print("Collecting normal system activity data...")
for _ in range(50):
    cpu = psutil.cpu_percent(interval=1)
    disk = psutil.disk_usage('/').percent
    processes = len(psutil.pids())
    file_mods = random.randint(0, 5)  # Normal file modification rate
    data.append([cpu, disk, processes, file_mods])
    labels.append(0)

# Simulate ransomware activity
print("Simulating ransomware-like activity data...")
for _ in range(50):
    cpu = random.uniform(80, 100)  # High CPU usage
    disk = random.uniform(70, 100)  # High Disk usage
    processes = len(psutil.pids()) + random.randint(10, 20)  # More processes running
    file_mods = random.randint(50, 100)  # High file modification rate
    data.append([cpu, disk, processes, file_mods])
    labels.append(1)

# Save data to CSV
df = pd.DataFrame(data, columns=["CPU_Usage", "Disk_Usage", "Processes", "File_Modifications"])
df["Label"] = labels
df.to_csv("ransomware_data.csv", index=False)

print("✅ Data collection complete! Saved as ransomware_data.csv")
