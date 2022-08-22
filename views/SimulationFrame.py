import customtkinter as ctk


class SimulationFrame(ctk.CTkFrame):
    def __init__(self, master, pacient):
        super().__init__()
        self.master = master
        self.pacient = pacient

        self.grid_rowconfigure((0, 1, 2), weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.columnconfigure((0, 1), weight=1)
        self.create_simulation_frame()

    def create_simulation_frame(self):
        self.label_name = ctk.CTkLabel(master=self,
                                       text=f'Paciente: {self.pacient.get_body().name}',
                                       height=50,
                                       corner_radius=6,
                                       text_font=("Roboto Medium", -16), text_color="white",
                                       fg_color=("white", "gray38"),
                                       )
        self.label_name.grid(
            column=0, row=0, sticky="nswe", padx=15, pady=15)

        self.label_age = ctk.CTkLabel(master=self,
                                      text=f'Edad: {self.pacient.get_body().age}',
                                      height=50,
                                      corner_radius=6,
                                      text_font=("Roboto Medium", -16), text_color="white",
                                      fg_color=("white", "gray38"),
                                      )
        self.label_age.grid(
            column=0, row=1, sticky="nswe", padx=15, pady=15)

        self.rest_periods = ctk.CTkLabel(master=self,
                                         text=f'Periodos restantes: {self.pacient.get_body().periods}',
                                         height=50,
                                         corner_radius=6,
                                         text_font=("Roboto Medium", -16), text_color="white",
                                         fg_color=("white", "gray38"),
                                         )
        self.rest_periods.grid(
            column=0, row=2, sticky="nswe", padx=15, pady=15)

        self.simulate_button = ctk.CTkButton(master=self,
                                             text="Simular",
                                             command=self.simulate)
        self.simulate_button.grid(
            column=1, row=2, sticky="nswe", padx=15, pady=15)

        self.frame_matrix = ctk.CTkFrame(master=self)
        self.display_matrix()
        self.frame_matrix.grid(
            column=0, row=3, columnspan=2, padx=15, pady=15)

    def display_matrix(self):
        matrix = self.pacient.get_body().get_matrix()
        for r in range(matrix.size):
            for c in range(matrix.size):
                self.label_matrix = ctk.CTkLabel(master=self.frame_matrix,
                                                 text="0",
                                                 corner_radius=6,
                                                 width=10,
                                                 height=10,
                                                 text_font=("Roboto Medium", -15), text_color="white",
                                                 fg_color=(
                                                     "white", "gray38"))
                self.label_matrix.grid(
                    column=c, row=r, padx=1, pady=1)

    def simulate(self):
        print("a")
