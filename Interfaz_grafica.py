import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        operacion = seleccion_operacion.get()

        if operacion == "Suma":
            resultado = num1 + num2
        elif operacion == "Resta":
            resultado = num1 - num2
        elif operacion == "Multiplicación":
            resultado = num1 * num2
        elif operacion == "División":
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2

        messagebox.showinfo("Resultado", f"El resultado es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese números válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear cuadros de texto
etiqueta_num1 = tk.Label(ventana, text="Número 1:")
etiqueta_num1.grid(row=0, column=0)
entrada_num1 = tk.Entry(ventana)
entrada_num1.grid(row=0, column=1)

etiqueta_num2 = tk.Label(ventana, text="Número 2:")
etiqueta_num2.grid(row=1, column=0)
entrada_num2 = tk.Entry(ventana)
entrada_num2.grid(row=1, column=1)

# Crear cuadro de lista para selección de operación
seleccion_operacion = tk.StringVar(ventana)
seleccion_operacion.set("Suma")
opciones_operacion = ["Suma", "Resta", "Multiplicación", "División"]
menu_operacion = tk.OptionMenu(ventana, seleccion_operacion, *opciones_operacion)
menu_operacion.grid(row=2, column=0, columnspan=2)

# Crear botón de calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=3, column=0, columnspan=2)

# Ejecutar la ventana principal
ventana.mainloop()
