import tkinter as tk
from tkinter import messagebox
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Datos de ejemplo: [Peso (kg), Tamaño (cm)]
X = [[4, 25],  # Gato
     [3, 20],  # Gato
     [10, 50], # Perro
     [9, 48],  # Perro
     [5, 30]]  # Gato
y = [0, 0, 1, 1, 0]  # 0 = Gato, 1 = Perro

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
result_label = tk.Label(root, text="¡¡Presione el botón y Averigue!!!", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
