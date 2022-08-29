from tkinter import filedialog, messagebox
import customtkinter as ctk
from model.helpers.VerifyMatrix import VerifyMatrix
from model.simulation.GenerateReport import GenerateReport

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
    APP_WIDTH: int = 1096
    APP_HEIGHT: int = 750

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
        self.side_menu.grid_rowconfigure(11, minsize=10)
        # Create widgets
        self.upload_file_button = ctk.CTkButton(
            self.side_menu, text="Cargar archivo",
            command=self.upload_files)
        self.upload_file_button.grid(
            row=0, column=0, sticky="nsew", padx=15, pady=15)

        # Components
        self.side_title = ctk.CTkLabel(self.side_menu, text="Simulaciones de:")
        self.side_title.grid(row=1, column=0, pady=10, padx=10)

        self.report_button = ctk.CTkButton(
            self.side_menu, text="Reporte", command=self.create_report)
        self.report_button.grid(
            row=11, column=0, sticky="nsew", padx=10, pady=20)

        ''' ====== Simulation frame ====== '''
        self.simulation_frame = ctk.CTkLabel(master=self,
                                             text="No hay patientes cargados",
                                             height=50,
                                             corner_radius=6,
                                             text_font=("Roboto Medium", -25), text_color="white",
                                             fg_color=("white", "gray38"),
                                             )
        self.simulation_frame.grid(
            row=0, column=1, sticky="nswe", padx=10, pady=10)

    def upload_files(self):
        file_route = filedialog.askopenfilename(
            initialdir="/", title="Select file",
            filetypes=(("XML", "*.xml"), ("all files", "*.*")))
        is_correct = UploadInformation().xPath(file_route)
        if is_correct:
            self.change_message()
            self.put_buttons_to_simulate()
            messagebox.showinfo(
                "Información", "Archivo cargado correctamente")
        else:
            messagebox.showerror(
                "Error", "El archivo o la ruta no es correcta, por favor revisa e intenta de nuevo")

    def create_button_for_patient(self, name, index):
        button_for_patient = ctk.CTkButton(
            self.side_menu, text=name, command=lambda: self.display_frame_simulation(name))
        button_for_patient.grid(
            row=index, column=0, sticky="nsew", padx=10, pady=10)

    def put_buttons_to_simulate(self):
        patient_data = UploadInformation().patients_list
        tmp = patient_data.get_head()
        count = 2
        while tmp is not None:
            self.create_button_for_patient(tmp.get_body().get_name(), count)
            count += 1
            tmp = tmp.get_next()

    def change_message(self):
        self.simulation_frame.configure(
            text="Escoger un patiente para simular")

    def display_frame_simulation(self, name):
        patient_data = UploadInformation().patients_list.get_patient(name)
        if patient_data is not None:
            self.simulation_frame = SimulationFrame(
                self, patient_data)
            self.simulation_frame.grid(
                row=0, column=1, sticky="nswe", padx=10, pady=10)

    @staticmethod
    def create_report():
        if UploadInformation().patients_list.get_head() is not None:
            VerifyMatrix().create_simulation_to_all_patients()
            generate_report = GenerateReport()
            create_new_report = generate_report.generate_report()
            if create_new_report:
                messagebox.showinfo(
                    "Información", "Reporte creado correctamente")
            else:
                messagebox.showerror(
                    "Error", "No se pudo crear el reporte, por favor intenta de nuevo")
        else:
            messagebox.showerror(
                "Error", "No hay patientes cargados, por favor carga uno")


if __name__ == "__main__":
    app = App()
    app.mainloop()
