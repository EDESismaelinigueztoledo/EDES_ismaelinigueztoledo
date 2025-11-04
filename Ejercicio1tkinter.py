import tkinter as tk
from tkinter import messagebox, ttk

# --- Funciones principales ---

def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

def tabla_multiplicar(numero):
    """Genera la tabla de multiplicar del número del 1 al 10"""
    tabla = ""
    for i in range(1, 11):
        tabla += f"{numero} x {i} = {numero * i}\n"
    return tabla


# --- Funciones de interfaz ---

def mostrar_conversion():
    """Ventana para convertir Celsius a Fahrenheit"""
    ventana_conv = tk.Toplevel(root)
    ventana_conv.title("Conversión de Temperatura")
    ventana_conv.geometry("350x200")
    
    tk.Label(ventana_conv, text="Ingrese grados Celsius:", font=("Arial", 12)).pack(pady=10)
    entrada_celsius = tk.Entry(ventana_conv, font=("Arial", 12))
    entrada_celsius.pack(pady=5)

    resultado_label = tk.Label(ventana_conv, text="", font=("Arial", 12, "bold"))
    resultado_label.pack(pady=10)

    def convertir():
        try:
            celsius = float(entrada_celsius.get())
            fahrenheit = celsius_a_fahrenheit(celsius)
            resultado_label.config(text=f"{celsius:.2f} °C = {fahrenheit:.2f} °F")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
    
    tk.Button(ventana_conv, text="Convertir", command=convertir, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=10)
    tk.Button(ventana_conv, text="Cerrar", command=ventana_conv.destroy, bg="#f44336", fg="white", font=("Arial", 11)).pack()


def mostrar_tabla():
    """Ventana para mostrar la tabla de multiplicar"""
    ventana_tabla = tk.Toplevel(root)
    ventana_tabla.title("Tabla de Multiplicar")
    ventana_tabla.geometry("400x350")

    tk.Label(ventana_tabla, text="Ingrese un número entero:", font=("Arial", 12)).pack(pady=10)
    entrada_num = tk.Entry(ventana_tabla, font=("Arial", 12))
    entrada_num.pack(pady=5)

    texto_tabla = tk.Text(ventana_tabla, height=10, width=30, font=("Consolas", 12))
    texto_tabla.pack(pady=10)

    def generar_tabla():
        try:
            numero = int(entrada_num.get())
            tabla = tabla_multiplicar(numero)
            texto_tabla.delete("1.0", tk.END)
            texto_tabla.insert(tk.END, tabla)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número entero válido.")
    
    tk.Button(ventana_tabla, text="Generar", command=generar_tabla, bg="#2196F3", fg="white", font=("Arial", 11)).pack(pady=5)
    tk.Button(ventana_tabla, text="Cerrar", command=ventana_tabla.destroy, bg="#f44336", fg="white", font=("Arial", 11)).pack(pady=5)


# --- Ventana principal (menú) ---

root = tk.Tk()
root.title("Menú Principal")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="=== MENÚ PRINCIPAL ===", font=("Arial", 16, "bold")).pack(pady=20)

ttk.Button(root, text="1) Conversión de Temperatura", command=mostrar_conversion).pack(pady=10, ipadx=10, ipady=5)
ttk.Button(root, text="2) Tabla de Multiplicar", command=mostrar_tabla).pack(pady=10, ipadx=10, ipady=5)
ttk.Button(root, text="3) Salir", command=root.destroy).pack(pady=10, ipadx=10, ipady=5)

root.mainloop()