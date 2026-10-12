import matplotlib.pyplot as plt

# Epochs
epochs = list(range(1, 11))

# Accuracy values
train_acc = [55, 65, 72, 80, 85, 88, 90, 92, 93, 95]
val_acc   = [50, 60, 68, 75, 80, 83, 85, 87, 88, 90]

# Plot graph
plt.figure()
plt.plot(epochs, train_acc, label='Train Accuracy')
plt.plot(epochs, val_acc, label='Validation Accuracy')

plt.title('Training vs Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy (%)')
plt.legend()

# Save graph
plt.savefig("accuracy_graph.png")

# Show graph
plt.show()