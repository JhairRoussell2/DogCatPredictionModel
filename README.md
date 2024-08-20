# Gender Prediction Model

This repository contains a simple machine learning project that predicts gender based on height, weight, and shoe size. The project utilizes a Decision Tree Classifier from scikit-learn and provides a user-friendly interface built with Tkinter.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model](#model)
- [GUI](#gui)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Gender Prediction Model is a basic example of using machine learning for classification tasks. It predicts gender based on user inputted data like height, weight, and shoe size. The model is trained on a small, hardcoded dataset and the results are displayed through a simple graphical interface.

## Features

- **Machine Learning**: Demonstrates a basic Decision Tree Classifier for binary classification.
- **Graphical User Interface**: Built using Tkinter, the GUI allows users to enter data and see predictions in real-time.
- **Educational Tool**: Ideal for beginners learning about machine learning and Python GUI development.

## Requirements

- Python 3.x
- Libraries:
  - `scikit-learn`
  - `Tkinter` (included with Python)
  - `pandas` (optional, for future data handling)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/gender-prediction-model.git
   ```

2. Navigate to the project directory:

   ```bash
   cd gender-prediction-model
   ```

3. Install the required libraries:

   ```bash
   pip install scikit-learn
   ```

## Usage

1. Run the Python script to launch the GUI:

   ```bash
   python gender_prediction.py
   ```

2. Input your height, weight, and shoe size in the provided fields and click "Predict Gender."

3. The prediction (Male or Female) will be displayed on the screen.

## Data

The model is trained on a small dataset with the following features:
- **Height** (in cm)
- **Weight** (in kg)
- **Shoe Size**

The labels are:
- `1` for Male
- `0` for Female

## Model

The Gender Prediction Model is built using a Decision Tree Classifier from the `scikit-learn` library. The model is trained on a manually created dataset and is designed to demonstrate basic machine learning concepts.

## GUI

The GUI is implemented using Tkinter, a standard Python interface to the Tk GUI toolkit. It allows users to interact with the model by inputting data and receiving predictions in a simple and intuitive way.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

This README provides an overview of the project, instructions for installation and usage, and information about the data and model used. It’s a great starting point for anyone looking to understand and contribute to the project.
