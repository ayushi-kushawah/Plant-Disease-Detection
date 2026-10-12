import matplotlib.pyplot as plt

# Epochs
epochs = list(range(1, 11))

# Loss values (you already used)
train_loss = [1.2, 0.9, 0.7, 0.5, 0.4, 0.3, 0.25, 0.2, 0.18, 0.15]
val_loss   = [1.3, 1.0, 0.8, 0.6, 0.5, 0.45, 0.4, 0.38, 0.35, 0.33]

# Accuracy values
train_acc = [55, 65, 72, 80, 85, 88, 90, 92, 93, 95]
val_acc   = [50, 60, 68, 75, 80, 83, 85, 87, 88, 90]

# ------------------- LOSS GRAPH -------------------
plt.figure()
plt.plot(epochs, train_loss, label='Train Loss')
plt.plot(epochs, val_loss, label='Validation Loss')
plt.title('Training vs Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# Save loss graph
plt.savefig("loss_graph.png")

# Show loss graph
plt.show()

# ------------------- ACCURACY GRAPH -------------------
plt.figure()
plt.plot(epochs, train_acc, label='Train Accuracy')
plt.plot(epochs, val_acc, label='Validation Accuracy')
plt.title('Training vs Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy (%)')
plt.legend()

# Save accuracy graph
plt.savefig("accuracy_graph.png")

# Show accuracy graph
plt.show()