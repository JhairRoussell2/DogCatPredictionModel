from tkinter import *
from sklearn.tree import DecisionTreeClassifier

# Sample data: [Height, Weight, Shoe Size]
X = [
    [180, 75, 42],  # Male 1
    [165, 60, 38],  # Female 1
    [170, 65, 40],  # Male 2
    [160, 55, 37],  # Female 2
    [175, 70, 41],  # Male 3
    [155, 50, 36],  # Female 3
    [185, 80, 43],  # Male 4
    [162, 58, 38],  # Female 4
    [172, 68, 40],  # Male 5
    [158, 52, 37],  # Female 5
    [178, 73, 42],  # Male 6
    [160, 54, 37],  # Female 6
    [182, 78, 43],  # Male 7
    [167, 63, 39],  # Female 7
    [174, 70, 41],  # Male 8
    [157, 51, 36],  # Female 8
    [181, 76, 42],  # Male 9
    [159, 53, 37],  # Female 9
    [179, 74, 42],  # Male 10
    [164, 59, 38],  # Female 10
]

# Corresponding labels: 1 for Male, 0 for Female
Y = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
# Create and train the decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X, Y)

# Create the Tkinter window
root = Tk()
root.title('Gender Prediction Model')
root.geometry('350x200')

# Add labels and entry fields for Height, Weight, and Shoe Size
Label(root, text="Enter Height:").pack(pady=5)
height_entry = Entry(root)
height_entry.pack(pady=5)

Label(root, text="Enter Weight:").pack(pady=5)
weight_entry = Entry(root)
weight_entry.pack(pady=5)

Label(root, text="Enter Shoe Size:").pack(pady=5)
shoesize_entry = Entry(root)
shoesize_entry.pack(pady=5)

# Function to make the prediction and display the result
def predict_gender():
    # Get input values
    height = int(height_entry.get())
    weight = int(weight_entry.get())
    shoesize = int(shoesize_entry.get())
    
    # Predict gender
    new_data = [[height, weight, shoesize]]
    prediction = clf.predict(new_data)
    
    # Display the result
    result = "Male" if prediction[0] == 1 else "Female"
    result_label.config(text="Prediction: " + result)

# Add a button to trigger the prediction
Button(root, text="Predict Gender", command=predict_gender).pack(pady=10)

# Label to display the prediction result
result_label = Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
