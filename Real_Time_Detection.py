import psutil
import joblib
import numpy as np
import time

# Load trained model
model = joblib.load("ransomware_detector.pkl")

def detect_ransomware():
    while True:
        # Collect system metrics
        cpu = psutil.cpu_percent()
        disk = psutil.disk_usage('/').percent
        processes = len(psutil.pids())
        file_mods = random.randint(0, 100)  # Simulate file modifications

        # Create feature vector
        features = np.array([[cpu, disk, processes, file_mods]])
        prediction = model.predict(features)[0]

        if prediction == 1:  
            print("🚨 WARNING: Possible Ransomware Detected!")
            stop_suspicious_processes()

        time.sleep(2)  # Check every 2 seconds

def stop_suspicious_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] and ("unknown" in proc.info['name'].lower() or "encryptor" in proc.info['name'].lower()):
            print(f"🛑 Stopping suspicious process: {proc.info['name']}")
            psutil.Process(proc.info['pid']).terminate()

# Start monitoring
detect_ransomware()
