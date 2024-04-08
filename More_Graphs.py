import numpy as np
import matplotlib.pyplot as plt

# Data
T = np.arange(1, 82)
FC = np.array([
    7, 1, 28, 9, 15, 14, 8, 16, 8, 9, 5, 14, 5, 3, 3, 8, 14, 7, 9, 13, 4, 14, 9, 23,
    11, 20, 6, 3, 6, 5, 4, 1, 8, 7, 2, 4, 1, 14, 4, 3, 5, 2, 4, 11, 6, 0, 5, 3, 2, 
    1, 0, 3, 0, 0, 1, 5, 5, 2, 7, 6, 1, 5, 1, 3, 6, 11, 3, 5, 6, 2, 0, 0, 1, 1, 1,
    0, 0, 1, 0, 0, 1
])

# Time Between Failures (TBF)
tbf = []
last_failure_time = 0
for i in range(len(FC)):
    if FC[i] == 0:
        tbf.append(T[i] - last_failure_time)
    else:
        last_failure_time = T[i]

# Pad tbf with zeros to match the length of T
tbf.extend([1] * (len(T) - len(tbf)))
tbf = np.array(tbf)

# Failure Intensity (FI)
fi = np.divide(FC, tbf)

# Reliability
reliability = np.cumprod(1 - (fi / 100))

# Plotting
fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Time Between Failures (TBF) plot
axs[0].plot(T[:len(tbf)], tbf, label='Time Between Failures')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('TBF')
axs[0].set_title('Time Between Failures')
axs[0].legend()

# Failure Intensity (FI) plot
axs[1].plot(T, fi, label='Failure Intensity')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('FI')
axs[1].set_title('Failure Intensity')
axs[1].legend()

# Reliability plot
axs[2].plot(T, reliability, label='Reliability')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Reliability')
axs[2].set_title('Reliability')
axs[2].legend()

plt.tight_layout()
plt.show()

# Discussion on acceptable range of failure rate
mean_failure_rate = np.mean(fi)
std_failure_rate = np.std(fi)
acceptable_range_lower_bound = mean_failure_rate - 2 * std_failure_rate
acceptable_range_upper_bound = mean_failure_rate + 2 * std_failure_rate

print("Mean failure rate:", mean_failure_rate)
print("Standard deviation of failure rate:", std_failure_rate)
print("Acceptable range of failure rate:", acceptable_range_lower_bound, "to", acceptable_range_upper_bound)

FC_Removed_Outliers = np.array([7, 1, 9, 15, 14, 8, 16, 8, 9, 5, 14, 5, 3, 3, 8, 14, 7, 9, 13, 4, 14, 9, 23, 11,
                                 20, 6, 3, 6, 5, 4, 1, 8, 7, 2, 4, 1, 14, 4, 3, 5, 2, 4, 11, 6, 0, 5, 3, 2,
                                 1, 0, 3, 0, 0, 1, 5, 5, 2, 7, 6, 1, 5, 1, 3, 6, 11, 3, 5, 6, 2, 0, 0, 1,
                                 1, 1, 0, 0, 1, 0, 0, 1])

T_Removed_Outliers = np.arange(1, len(FC_Removed_Outliers) + 1)

# failure rate after removing outliers
tbf_removed_outliers = []
last_failure_time = 0
for i in range(len(FC_Removed_Outliers)):
    if FC_Removed_Outliers[i] == 0:
        tbf_removed_outliers.append(T_Removed_Outliers[i] - last_failure_time)
    else:
        last_failure_time = T_Removed_Outliers[i]

tbf_removed_outliers.extend([1] * (len(T_Removed_Outliers) - len(tbf_removed_outliers)))

fi_removed_outliers = np.divide(FC_Removed_Outliers, tbf_removed_outliers)

mean_failure_rate_removed_outliers = np.mean(fi_removed_outliers)
std_failure_rate_removed_outliers = np.std(fi_removed_outliers)
acceptable_range_lower_bound_removed_outliers = mean_failure_rate_removed_outliers - 2 * std_failure_rate_removed_outliers
acceptable_range_upper_bound_removed_outliers = mean_failure_rate_removed_outliers + 2 * std_failure_rate_removed_outliers

print("Mean failure rate after removing outliers:", mean_failure_rate_removed_outliers)
print("Standard deviation of failure rate after removing outliers:", std_failure_rate_removed_outliers)
print("Acceptable range of failure rate after removing outliers:", acceptable_range_lower_bound_removed_outliers, "to", acceptable_range_upper_bound_removed_outliers)



