import tkinter as tk
from tkinter import messagebox
from sklearn.tree import DecisionTreeClassifier
import pandas as pd  

# Cargar el archivo CSV
data = pd.read_csv('cat-dog-classification.csv')

# Seleccionar las columnas necesarias (Peso y Tamaño)
X = data[['Weight', 'Height']].values  # Variables: Peso y Tamaño
y = data['Label'].apply(lambda x: 1 if x == 'Dog' else 0).values  # Etiqueta: 1 = Perro, 0 = Gato

# Crear el modelo de árbol de decisión
model = DecisionTreeClassifier()
model.fit(X, y)

# Función de predicción
def predecir():
    try:
        peso = float(entry_peso.get())
        tamano = float(entry_tamano.get())
        
        # Hacer la predicción
        prediccion = model.predict([[peso, tamano]])[0]
        
        if prediccion == 1:
            resultado = f"Con peso {peso} kg y tamaño {tamano} cm, es un PERRO."
        else:
            resultado = f"Con peso {peso} kg y tamaño {tamano} cm, es un GATO."
        
        # Mostrar el resultado en el mismo label
        result_label.config(text=resultado)
    except ValueError:
        result_label.config(text="Por favor ingresa valores válidos.")
    
# Crear la interfaz gráfica
root = tk.Tk()
root.title("Clasificador de Perro o Gato")
root.geometry('450x300')

# Etiquetas y campos de entrada
tk.Label(root, text="Peso (kg):").pack(pady=5)
entry_peso = tk.Entry(root)
entry_peso.pack(pady=5)

tk.Label(root, text="Tamaño (cm):").pack(pady=5)
entry_tamano = tk.Entry(root)
entry_tamano.pack(pady=5)

# Botón para predecir
tk.Button(root, text="Predecir", command=predecir).pack(pady=10)

# Etiqueta para mostrar la predicción
result_label = tk.Label(root, text="¡¡¡Presione el botón y Averigue!!!", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
