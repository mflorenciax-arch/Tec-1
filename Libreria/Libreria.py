import customtkinter as ctk
from tkinter import messagebox

# Configuración de la app
ctk.set_appearance_mode("System")  # "Light", "Dark" o "System"
ctk.set_default_color_theme("blue")

# Función que verifica la división
def verificar_divisor():
    try:
        numero_principal = int(entrada_nro.get())
        divisor_elegido = int(desplegable.get())

        if numero_principal % divisor_elegido == 0:
            mensaje = f"¡Correcto! {divisor_elegido} es divisor de {numero_principal}."
            messagebox.showinfo("Resultado", mensaje)
        else:
            mensaje = f"No, {numero_principal} no es divisible por {divisor_elegido}."
            messagebox.showwarning("Resultado", mensaje)

    except ValueError:
        messagebox.showerror("Error", "Ingresá un número válido.")

# Crear ventana
ventana = ctk.CTk()
ventana.title("Validador de Divisores")
ventana.geometry("400x300")

# Texto
label1 = ctk.CTkLabel(ventana, text="Ingresá un número:", font=("Arial", 14))
label1.pack(pady=10)

# Entrada de número
entrada_nro = ctk.CTkEntry(ventana, placeholder_text="Ej: 50")
entrada_nro.pack(pady=5)

# Texto divisor
label2 = ctk.CTkLabel(ventana, text="Elegí un divisor:", font=("Arial", 14))
label2.pack(pady=10)

# Lista de opciones del 1 al 10
opciones = [str(i) for i in range(1, 11)]
desplegable = ctk.CTkComboBox(ventana, values=opciones)
desplegable.pack(pady=5)
desplegable.set("1")

# Botón
boton = ctk.CTkButton(
    ventana,
    text="VERIFICAR",
    command=verificar_divisor
)
boton.pack(pady=20)

# Ejecutar app
ventana.mainloop()

