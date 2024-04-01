import matplotlib.pyplot as plt
import numpy as np

n = np.array([0, 10, 100, 200, 300, 400, 500])
search_time = np.array([0.000001, 0.000056, 0.000123, 0.000183, 0.000254, 0.000278, 0.000300])
plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.semilogy(n, search_time, marker='o', label='Binary search', linestyle='-')
plt.ylabel('Time (seconds)')
plt.xlabel('Number of paitents (n)')
plt.title('Time Complexity of Binary Search')
plt.legend()


plt.tight_layout()
plt.show()