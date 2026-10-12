# 🌿 AI Plant Disease Detection System

An AI-powered web application that detects plant diseases from leaf images using deep learning.

## Features

- Upload plant leaf images for analysis
- Predict plant diseases using a CNN-based model
- Support for multiple plant species
- Simple web interface built with Flask

## Tech Stack

- **Language:** Python
- **Backend:** Flask
- **Deep Learning:** PyTorch
- **Frontend:** HTML, CSS, Bootstrap

## Project Structure

```text
Plant_AI/
├── Flask/          # Web application, backend, and templates
├── Models/         # Trained model files
├── TestImages/     # Sample test images
├── requirements.txt
├── accuracy_graph.py
├── confusion_matrix.py
├── graph.py
├── README.md
└── .gitignore
```

## Run Locally

1. Clone this repository using its GitHub URL.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   On Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the Flask application:

   ```bash
   cd Flask
   python app.py
   ```

6. Open the local address printed in the terminal.

## Future Improvements

- Display prediction confidence scores
- Provide disease prevention and treatment suggestions
- Explore mobile application support