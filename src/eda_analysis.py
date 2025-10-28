import matplotlib.pyplot as plt
import seaborn as sns
from data_processing import load_and_clean_data

data = load_and_clean_data()

plt.figure(figsize=(10, 5))
plt.plot(data['price'])
plt.title('Price Trend')
plt.xlabel('Index')
plt.ylabel('Price')
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()