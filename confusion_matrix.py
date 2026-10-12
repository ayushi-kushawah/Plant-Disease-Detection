import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Class labels
classes = ["Aloevera", "Amla", "Bhrami", "Bringaraja", "Coriender",
           "Curry", "Ekka", "Hibiscus", "Lemon", "Mint",
           "Neem", "Papaya", "Tulsi"]

# Create a simulated confusion matrix
np.random.seed(42)
matrix = np.zeros((len(classes), len(classes)))

for i in range(len(classes)):
    matrix[i][i] = np.random.randint(65, 85)  # strong diagonal (correct predictions)

# Plot
plt.figure(figsize=(10,8))
sns.heatmap(matrix, annot=True, cmap="Blues", fmt=".0f",
            xticklabels=classes, yticklabels=classes)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")

# Save image
plt.savefig("confusion_matrix.png")

plt.show()
