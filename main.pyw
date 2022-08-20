from tkinter import filedialog, messagebox
import customtkinter as ctk

# Views


# Helpers
from model.helpers.WindowPosition import WindowPosition
from model.simulation.UploadInformation import UploadInformation

# # Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")

# # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    # Size of the window
    APP_WIDTH = 700
    APP_HEIGHT = 500

    def __init__(self):
        super().__init__()

        # Set minimum size of window
        self.minsize(self.APP_WIDTH, self.APP_HEIGHT)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # Position of the app
        self.geometry(WindowPosition().get_window_position(self.winfo_screenwidth(
        ), self.winfo_screenheight(), self.APP_WIDTH, self.APP_HEIGHT))

        self.title("Simulación de enfermedades")

        # Custom grid layout (2x2)
        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Create widgets
        self.upload_file_button = ctk.CTkButton(
            self, text="Cargar archivo",
            command=self.upload_files)
        self.upload_file_button.grid(
            row=0, column=0, sticky="nsew", padx=15, pady=15)

        self.simulate_button = ctk.CTkButton(
            master=self, text="Simular",
            state="disabled",
            command=self.simulate)
        self.simulate_button.grid(
            row=0, column=3, sticky="nsew", padx=15, pady=15)

    def upload_files(self):
        fileRoute = filedialog.askopenfilename(
            initialdir="/Desktop", title="Select file",
            filetypes=(("XML", "*.xml"), ("all files", "*.*")))
        isCorrect = UploadInformation().xPath(fileRoute)
        if isCorrect:
            self.simulate_button.configure(state="normal")
            messagebox.showinfo(
                "Información", "Archivo cargado correctamente")
        else:
            self.simulate_button.configure(state="disabled")
            messagebox.showerror(
                "Error", "El archivo no es correcto, por favor revisar información")

    def simulate(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
