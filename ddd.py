


#"C:/Users/Jimenez Nava/PycharmProjects/pythonProject/entrenamiento/programa velez/Proyecto ECCI - MDO.xlsx"
import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from PIL import ImageTk, Image
import os


"""class VentanaInicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ORACULO")
        self.geometry("600x600")

        # Cargar la imagen con tk.PhotoImage
        self.imagen_tk = tk.PhotoImage(file="portada.png")

        # Crear un Label para mostrar la imagen
        label_imagen = tk.Label(self, image=self.imagen_tk)
        label_imagen.pack(pady=20)

        # Botón para ir a la Ventana 2
        boton = tk.Button(self, text="INICIO", command=self.abrir_ventana2)
        boton.pack(pady=10)

    def abrir_ventana2(self):
        self.withdraw()  # Oculta la Ventana de Inicio
        ventana2 = Ventana2(self)  # Abre la Ventana 2


class Ventana2(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("ORACULO")
        self.geometry("600x600")

        # Etiqueta en la Ventana 2
        label = tk.Label(self, text="ORACULO")
        label.pack(pady=20)

        # Cargar la imagen con tk.PhotoImage
        self.imagen_tk = tk.PhotoImage(file="portada_2.png")
        label_imagen = tk.Label(self, image=self.imagen_tk)
        label_imagen.pack(padx=10, pady=10)

        # Lista desplegable (Combobox)
        self.lista_opciones = ["MIN=SISTEMA MOTOR INYECION", "MAD= SISTEMA MOTOR ADMISION", ""]
        self.combobox = ttk.Combobox(self, values=self.lista_opciones, width=50)
        self.combobox.set("lista de nomenclatura")  # Valor por defecto
        self.combobox.pack(pady=30)

        # Cuadro de texto para ingresar el término de búsqueda
        self.cuadrotexto = tk.Entry(self, width=30)
        self.cuadrotexto.pack()

        # Botón para buscar en el archivo de Excel
        buscar = tk.Button(self, text="Buscar", command=self.buscar_en_excel)
        buscar.pack(padx=50, pady=10)

        # Botón para volver a la Ventana de Inicio
        boton = tk.Button(self, text="Volver a Inicio", command=self.volver_a_ventana_inicio)
        boton.pack(side="bottom", padx=50, pady=10)

        # Obtener la ruta del archivo Excel en la misma carpeta que el script .py
        self.file_path = os.path.join(os.path.dirname(__file__), "Proyecto ECCI - MDO.xlsx")

        try:
            self.df = pd.read_excel(self.file_path)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")
            self.df = None

    def buscar_en_excel(self):
        search_term = self.cuadrotexto.get().lower()
        if search_term and self.df is not None:
            # Filtrar el DataFrame para buscar en la columna 2
            #matches = self.df[self.df.iloc[:, 2].str.lower().str.contains(search_term, na=False)]
            matches = self.df[
                self.df.iloc[:, 2].str.lower().str.contains(search_term, na=False) |
                self.df.iloc[:, 3].str.lower().str.contains(search_term, na=False)
                ]
            if not matches.empty:
                # Mostrar solo las columnas 2 y 3
                result_df = matches.iloc[:, [2, 3]]
                self.abrir_ventana_resultados(result_df)
            else:
                messagebox.showinfo("Resultado", "No se encontraron coincidencias.")
        else:
            messagebox.showwarning("Advertencia",
                                   "No se ha ingresado ningún término de búsqueda o no se pudo cargar el archivo.")

    def abrir_ventana_resultados(self, result_df):
        VentanaResultados(self, result_df)

    def volver_a_ventana_inicio(self):
        self.destroy()  # Cierra la Ventana 2
        self.master.deiconify()  # Muestra de nuevo la Ventana de Inicio


class VentanaResultados(tk.Toplevel):
    def __init__(self, master, result_df):
        super().__init__(master)
        self.title("Resultados de la búsqueda")
        self.geometry("400x400")

        self.result_df = result_df

        # Crear una lista para mostrar los resultados
        self.listbox = tk.Listbox(self, width=50, height=20)
        self.listbox.pack(pady=20)

        # Insertar resultados en la lista
        for _, row in self.result_df.iterrows():
            self.listbox.insert(tk.END, f"{row.iloc[0]} - {row.iloc[1]}")

        # Bind del doble clic en un elemento de la lista
        self.listbox.bind("<Double-1>", self.abrir_imagen_seleccionada)

    def abrir_imagen_seleccionada(self, event):
        # Obtener el índice del elemento seleccionado
        seleccion = self.listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            # Obtener el nombre del elemento seleccionado
            nombre_seleccionado = self.result_df.iloc[indice, 0]

            # Intentar abrir la imagen con el mismo nombre
            nombre_imagen = f"{nombre_seleccionado}.png"  # Asume que la imagen es PNG
            if os.path.exists(nombre_imagen):
                ventana_imagen = VentanaImagen(self, nombre_imagen)
            else:
                messagebox.showerror("Error", f"No se encontró la imagen: {nombre_imagen}")


class VentanaImagen(tk.Toplevel):
    def __init__(self, master, nombre_imagen):
        super().__init__(master)
        self.title(nombre_imagen)

        # Cargar y mostrar la imagen
        self.imagen = ImageTk.PhotoImage(Image.open(nombre_imagen))
        label_imagen = tk.Label(self, image=self.imagen)
        label_imagen.pack(pady=20)


if __name__ == "__main__":
    ventana_inicio = VentanaInicio()
    ventana_inicio.mainloop() 

import tkinter as tk
from tkinter import Listbox


# Función para abrir la ventana de ayuda
def ayuda():
    ventana_ayuda = tk.Toplevel(root)  # Crear una nueva ventana secundaria
    ventana_ayuda.title("Ayuda")

    # Etiqueta de título
    titulo = tk.Label(ventana_ayuda, text="Lista de ayuda", font=("Arial", 14))
    titulo.pack(pady=10)

    # Lista de ayuda
    lista_ayuda = Listbox(ventana_ayuda, height=5)
    items_ayuda = ["Opción 1: Descripción de la opción",
                   "Opción 2: Descripción de la opción",
                   "Opción 3: Descripción de la opción",
                   "Opción 4: Descripción de la opción"]

    for item in items_ayuda:
        lista_ayuda.insert(tk.END, item)  # Agregar cada elemento a la lista

    lista_ayuda.pack(pady=10)

    # Botón para cerrar la ventana
    cerrar_boton = tk.Button(ventana_ayuda, text="Cerrar", command=ayuda.destroy)
    cerrar_boton.pack(pady=10)


# Ventana principal
root = tk.Tk()
root.title("Aplicación Principal")

# Botón de ayuda
boton_ayuda = tk.Button(root, text="Ayuda", command=ayuda)
boton_ayuda.pack(pady=20)

root.mainloop()"""

"""import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from PIL import ImageTk, Image
from tkinter import Listbox
import os


class VentanaInicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ORACULO")
        self.geometry("600x600")

        # Cargar la imagen con tk.PhotoImage
        self.imagen_tk = tk.PhotoImage(file="portada.png")

        # Crear un Label para mostrar la imagen
        label_imagen = tk.Label(self, image=self.imagen_tk)
        label_imagen.pack(pady=20)

        # Botón para ir a la Ventana 2
        boton = tk.Button(self, text="INICIO", command=self.abrir_ventana2)
        boton.pack(pady=10)

    def abrir_ventana2(self):
        self.withdraw()  # Oculta la Ventana de Inicio
        ventana2 = Ventana2(self)  # Abre la Ventana 2


class Ventana2(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("ORACULO")
        self.geometry("600x600")

        # Etiqueta en la Ventana 2
        label = tk.Label(self, text="ORACULO")
        label.pack(pady=20)

        # Cargar la imagen con tk.PhotoImage
        self.imagen_tk = tk.PhotoImage(file="portada_2.png")
        label_imagen = tk.Label(self, image=self.imagen_tk)
        label_imagen.pack(padx=10, pady=10)

        # Cuadro de texto para ingresar el término de búsqueda
        self.cuadrotexto = tk.Entry(self, width=30)
        self.cuadrotexto.pack()

        # Botón para buscar en el archivo de Excel
        buscar = tk.Button(self, text="Buscar", command=self.buscar_en_excel)
        buscar.pack(padx=50, pady=10)

        # Botón de ayuda
        ayuda = tk.Button(self, text="Ayuda", command=self.abrir_ventana_ayuda)
        ayuda.pack(padx=50, pady=10)

        # Botón para volver a la Ventana de Inicio
        boton = tk.Button(self, text="Volver a Inicio", command=self.volver_a_ventana_inicio)
        boton.pack(side="bottom", padx=50, pady=10)

        # Obtener la ruta del archivo Excel en la misma carpeta que el script .py
        self.file_path = os.path.join(os.path.dirname(__file__), "Proyecto ECCI - MDO.xlsx")

        try:
            self.df = pd.read_excel(self.file_path)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")
            self.df = None

    def buscar_en_excel(self):
        search_term = self.cuadrotexto.get().lower()
        if search_term and self.df is not None:
            matches = self.df[
                self.df.iloc[:, 2].str.lower().str.contains(search_term, na=False) |
                self.df.iloc[:, 3].str.lower().str.contains(search_term, na=False)
                ]
            if not matches.empty:
                result_df = matches.iloc[:, [2, 3]]
                self.abrir_ventana_resultados(result_df)
            else:
                messagebox.showinfo("Resultado", "No se encontraron coincidencias.")
        else:
            messagebox.showwarning("Advertencia",
                                   "No se ha ingresado ningún término de búsqueda o no se pudo cargar el archivo.")

    def abrir_ventana_resultados(self, result_df):
        VentanaResultados(self, result_df)

    def volver_a_ventana_inicio(self):
        self.destroy()  # Cierra la Ventana 2
        self.master.deiconify()  # Muestra de nuevo la Ventana de Inicio

    # Función para abrir la ventana de ayuda
    def abrir_ventana_ayuda(self):
        ventana_ayuda = tk.Toplevel(self)  # Crear una nueva ventana secundaria
        ventana_ayuda.title("Ayuda")
        ventana_ayuda.geometry("400x400")

        # Etiqueta de título
        titulo = tk.Label(ventana_ayuda, text="Lista de ayuda", font=("Arial", 14))
        titulo.pack(pady=10)

        # Lista de ayuda
        lista_ayuda = Listbox(ventana_ayuda, height=10, width=40)
        items_ayuda = ["MIN: Motor inyeccion",
                       "MAD: Motor admisión",
                       "MEL: Motor electrico",
                       "MES: Motor escape",
                       "MDI: Motor distribucón",
                       "MRE: Motor refirgracióm",
                       "MLU: Motor lubricación"]

        for item in items_ayuda:
            lista_ayuda.insert(tk.END, item)  # Agregar cada elemento a la lista

        lista_ayuda.pack(pady=10)

        # Botón para cerrar la ventana
        cerrar_boton = tk.Button(ventana_ayuda, text="Cerrar", command=ventana_ayuda.destroy)
        cerrar_boton.pack(pady=10)


class VentanaResultados(tk.Toplevel):
    def __init__(self, master, result_df):
        super().__init__(master)
        self.title("Resultados de la búsqueda")
        self.geometry("400x400")

        self.result_df = result_df

        # Crear una lista para mostrar los resultados
        self.listbox = tk.Listbox(self, width=50, height=20)
        self.listbox.pack(pady=20)

        # Insertar resultados en la lista
        for _, row in self.result_df.iterrows():
            self.listbox.insert(tk.END, f"{row.iloc[0]} - {row.iloc[1]}")

        # Bind del doble clic en un elemento de la lista
        self.listbox.bind("<Double-1>", self.abrir_imagen_seleccionada)

    def abrir_imagen_seleccionada(self, event):
        seleccion = self.listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            nombre_seleccionado = self.result_df.iloc[indice, 0]
            nombre_imagen = f"{nombre_seleccionado}.png"  # Asume que la imagen es PNG
            if os.path.exists(nombre_imagen):
                ventana_imagen = VentanaImagen(self, nombre_imagen)
            else:
                messagebox.showerror("Error", f"No se encontró la imagen: {nombre_imagen}")


class VentanaImagen(tk.Toplevel):
    def __init__(self, master, nombre_imagen):
        super().__init__(master)
        self.title(nombre_imagen)

        # Cargar y mostrar la imagen
        self.imagen = ImageTk.PhotoImage(Image.open(nombre_imagen))
        label_imagen = tk.Label(self, image=self.imagen)
        label_imagen.pack(pady=20)


if __name__ == "__main__":

    ventana_inicio = VentanaInicio()
    ventana_inicio.mainloop() """

import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from PIL import ImageTk, Image
from tkinter import Listbox
import os


class VentanaInicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ORACULO")
        self.geometry("600x600")

        # Cargar la imagen con tk.PhotoImage
        self.imagen_tk = tk.PhotoImage(file="portada.png")

        # Crear un Label para mostrar la imagen
        label_imagen = tk.Label(self, image=self.imagen_tk)
        label_imagen.pack(pady=20)

        # Botón para ir a la Ventana 2
        boton = tk.Button(self, text="INICIO", command=self.abrir_ventana2)
        boton.pack(pady=10)

    def abrir_ventana2(self):
        self.withdraw()  # Oculta la Ventana de Inicio
        ventana2 = Ventana2(self)  # Abre la Ventana 2


class Ventana2(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("ORACULO")
        self.geometry("600x600")

        # Etiqueta en la Ventana 2
        label = tk.Label(self, text="ORACULO")
        label.pack(pady=20)

        # Cargar la imagen con tk.PhotoImage
        self.imagen_tk = tk.PhotoImage(file="portada_2.png")
        label_imagen = tk.Label(self, image=self.imagen_tk)
        label_imagen.pack(padx=10, pady=10)

        # Cuadro de texto para ingresar el término de búsqueda
        self.cuadrotexto = tk.Entry(self, width=30)
        self.cuadrotexto.pack()

        # Asignar la tecla Enter para realizar la búsqueda
        self.cuadrotexto.bind('<Return>', self.buscar_en_excel)

        # Botón para buscar en el archivo de Excel
        buscar = tk.Button(self, text="Buscar", command=self.buscar_en_excel)
        buscar.pack(padx=50, pady=10)

        # Botón de ayuda
        ayuda = tk.Button(self, text="Ayuda", command=self.abrir_ventana_ayuda)
        ayuda.pack(padx=50, pady=10)

        # Botón para volver a la Ventana de Inicio
        boton = tk.Button(self, text="Volver a Inicio", command=self.volver_a_ventana_inicio)
        boton.pack(side="bottom", padx=50, pady=10)

        # Obtener la ruta del archivo Excel en la misma carpeta que el script .py
        self.file_path = os.path.join(os.path.dirname(__file__), "Proyecto ECCI - MDO.xlsx")

        try:
            self.df = pd.read_excel(self.file_path)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {str(e)}")
            self.df = None

    def buscar_en_excel(self, event=None):  # Se agrega "event=None" para soportar el bind de Enter
        search_term = self.cuadrotexto.get().lower()
        if search_term and self.df is not None:
            matches = self.df[
                self.df.iloc[:, 2].str.lower().str.contains(search_term, na=False) |
                self.df.iloc[:, 3].str.lower().str.contains(search_term, na=False)
                ]
            if not matches.empty:
                result_df = matches.iloc[:, [2, 3]]
                self.abrir_ventana_resultados(result_df)
            else:
                messagebox.showinfo("Resultado", "No se encontraron coincidencias.")
        else:
            messagebox.showwarning("Advertencia",
                                   "No se ha ingresado ningún término de búsqueda o no se pudo cargar el archivo.")

    def abrir_ventana_resultados(self, result_df):
        VentanaResultados(self, result_df)

    def volver_a_ventana_inicio(self):
        self.destroy()  # Cierra la Ventana 2
        self.master.deiconify()  # Muestra de nuevo la Ventana de Inicio

    # Función para abrir la ventana de ayuda
    def abrir_ventana_ayuda(self):
        ventana_ayuda = tk.Toplevel(self)  # Crear una nueva ventana secundaria
        ventana_ayuda.title("Ayuda")
        ventana_ayuda.geometry("400x400")

        # Etiqueta de título
        titulo = tk.Label(ventana_ayuda, text="Lista de ayuda", font=("Arial", 14))
        titulo.pack(pady=10)

        # Lista de ayuda
        lista_ayuda = Listbox(ventana_ayuda, height=10, width=40)
        items_ayuda = ["MIN: Motor inyeccion",
                       "MAD: Motor admisión",
                       "MEL: Motor electrico",
                       "MES: Motor escape",
                       "MDI: Motor distribucón",
                       "MRE: Motor refirgracióm",
                       "MLU: Motor lubricación"]

        for item in items_ayuda:
            lista_ayuda.insert(tk.END, item)  # Agregar cada elemento a la lista

        lista_ayuda.pack(pady=10)

        # Botón para cerrar la ventana
        cerrar_boton = tk.Button(ventana_ayuda, text="Cerrar", command=ventana_ayuda.destroy)
        cerrar_boton.pack(pady=10)


class VentanaResultados(tk.Toplevel):
    def __init__(self, master, result_df):
        super().__init__(master)
        self.title("Resultados de la búsqueda")
        self.geometry("400x400")

        self.result_df = result_df

        # Crear una lista para mostrar los resultados
        self.listbox = tk.Listbox(self, width=50, height=20)
        self.listbox.pack(pady=20)

        # Insertar resultados en la lista
        for _, row in self.result_df.iterrows():
            self.listbox.insert(tk.END, f"{row.iloc[0]} - {row.iloc[1]}")

        # Bind del doble clic en un elemento de la lista
        self.listbox.bind("<Double-1>", self.abrir_imagen_seleccionada)

    def abrir_imagen_seleccionada(self, event):
        seleccion = self.listbox.curselection()
        if seleccion:
            indice = seleccion[0]
            nombre_seleccionado = self.result_df.iloc[indice, 0]
            nombre_imagen = f"{nombre_seleccionado}.png"  # Asume que la imagen es PNG
            if os.path.exists(nombre_imagen):
                ventana_imagen = VentanaImagen(self, nombre_imagen)
            else:
                messagebox.showerror("Error", f"No se encontró la imagen: {nombre_imagen}")


class VentanaImagen(tk.Toplevel):
    def __init__(self, master, nombre_imagen):
        super().__init__(master)
        self.title(nombre_imagen)

        # Cargar y mostrar la imagen
        self.imagen = ImageTk.PhotoImage(Image.open(nombre_imagen))
        label_imagen = tk.Label(self, image=self.imagen)
        label_imagen.pack(pady=20)


if __name__ == "__main__":
    ventana_inicio = VentanaInicio()
    ventana_inicio.mainloop()


