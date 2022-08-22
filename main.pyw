from tkinter import filedialog, messagebox
import customtkinter as ctk

# Data
from model.simulation.UploadInformation import UploadInformation

# Helpers
from model.helpers.WindowPosition import WindowPosition
from model.simulation.UploadInformation import UploadInformation

# Views
from views.SimulationFrame import SimulationFrame

# # Modes: "System" (standard), "Dark", "Light"
ctk.set_appearance_mode("dark")

# # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    # Size of the window
    APP_WIDTH: int = 950
    APP_HEIGHT: int = 700

    def __init__(self):
        super().__init__()

        # Set minimum size of window
        self.minsize(self.APP_WIDTH, self.APP_HEIGHT)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # Position of the app
        self.geometry(WindowPosition().get_window_position(self.winfo_screenwidth(
        ), self.winfo_screenheight(), self.APP_WIDTH, self.APP_HEIGHT))

        self.title("Simulación de enfermedades")

        # Custom grid layout (2x1)
        # create 2x1 grid system
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create a side menu
        self.side_menu = ctk.CTkFrame(self,
                                      width=200, corner_radius=0)
        self.side_menu.grid(row=0, column=0, sticky="nswe")

        '''====== Side menu buttons ======'''
        self.side_menu.grid_rowconfigure(0, minsize=10)
        self.side_menu.grid_rowconfigure(5, weight=1)
        self.side_menu.grid_rowconfigure(8, minsize=20)

        # Create widgets
        self.upload_file_button = ctk.CTkButton(
            self.side_menu, text="Cargar archivo",
            command=self.upload_files)
        self.upload_file_button.grid(
            row=0, column=0, sticky="nsew", padx=15, pady=15)

        # Components
        self.side_title = ctk.CTkLabel(self.side_menu, text="Simulaciones de:")
        self.side_title.grid(row=1, column=0, pady=10, padx=10)

        ''' ====== Simulation frame ====== '''
        self.simulation_frame = ctk.CTkLabel(master=self,
                                             text="No hay pacientes cargados",
                                             height=50,
                                             corner_radius=6,
                                             text_font=("Roboto Medium", -25), text_color="white",
                                             fg_color=("white", "gray38"),
                                             )
        self.simulation_frame.grid(
            row=0, column=1, sticky="nswe", padx=10, pady=10)

    def upload_files(self):
        fileRoute = filedialog.askopenfilename(
            initialdir="/Desktop", title="Select file",
            filetypes=(("XML", "*.xml"), ("all files", "*.*")))
        isCorrect = UploadInformation().xPath(fileRoute)
        if isCorrect:
            self.change_message()
            self.put_buttons_to_simulate()
            messagebox.showinfo(
                "Información", "Archivo cargado correctamente")
        else:
            messagebox.showerror(
                "Error", "El archivo o la ruta no es correcta, por favor revisa e intenta de nuevo")

    def create_button_for_pacient(self, name, index):
        button_for_pacient = ctk.CTkButton(
            self.side_menu, text=name, command=lambda: self.display_frame_simulation(name))
        button_for_pacient.grid(
            row=index, column=0, sticky="nsew", padx=10, pady=10)

    def put_buttons_to_simulate(self):
        pacient_data = UploadInformation().pacients_list
        tmp = pacient_data.get_next()
        count = 2
        while tmp is not None:
            self.create_button_for_pacient(tmp.get_body().get_name(), count)
            count += 1
            tmp = tmp.get_next()

    def change_message(self):
        self.simulation_frame.configure(
            text="Escoger un paciente para simular")

    def display_frame_simulation(self, name):
        pacient_data = UploadInformation().pacients_list
        tmp = pacient_data.get_next()
        while tmp is not None:
            if tmp.get_body().get_name() == name:
                self.simulation_frame = SimulationFrame(self, tmp)
                self.simulation_frame.grid(
                    row=0, column=1, sticky="nswe", padx=10, pady=10)
                break
            tmp = tmp.get_next()


if __name__ == "__main__":
    app = App()
    app.mainloop()
