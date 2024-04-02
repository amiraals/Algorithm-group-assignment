import time
import matplotlib.pyplot as plt
from collections import deque

def add_to_consultation_queue_time(n):
    consultation_queue = deque()
    start_time = time.time()
    for i in range(n):
        consultation_queue.append(i)
    end_time = time.time()
    return end_time - start_time

patients_range = list(range(1000, 10001, 1000))
t = [add_to_consultation_queue_time(num_patients) for num_patients in patients_range]

plt.figure(figsize=(10, 5))
plt.plot(patients_range, t, marker='o')
plt.title('Time Complexity of Add to Consultation Queue')
plt.xlabel('Number of patients (n)')
plt.ylabel('Time Taken (s)')
plt.show()
