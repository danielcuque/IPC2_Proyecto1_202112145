import customtkinter as ctk
from data.base.classes.Cell import Cell
from data.base.classes.Patient import Patient


class SimulationFrame(ctk.CTkFrame):
    def __init__(self, master, patient):
        super().__init__()
        self.master = master
        self.patient: Patient = patient

        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=0)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
        self.create_simulation_frame()

    def create_simulation_frame(self):

        # Labels
        self.label_name = ctk.CTkLabel(master=self,
                                       text=f'Paciente: {self.patient.name}',
                                       height=30,
                                       corner_radius=6,
                                       text_font=("Roboto Medium", -14), text_color="white",
                                       fg_color=("white", "gray38"),
                                       )
        self.label_name.grid(
            column=0, row=0, sticky="nswe", padx=15, pady=15)

        self.label_age = ctk.CTkLabel(master=self,
                                      text=f'Edad: {self.patient.age}',
                                      height=30,
                                      corner_radius=6,
                                      text_font=("Roboto Medium", -14), text_color="white",
                                      fg_color=("white", "gray38"),
                                      )
        self.label_age.grid(
            column=0, row=1, sticky="nswe", padx=15, pady=15)

        self.label_rest_periods = ctk.CTkLabel(master=self,
                                               text=f'Periodos restantes: {self.patient.periods}',
                                               height=30,
                                               corner_radius=6,
                                               text_font=("Roboto Medium", -16), text_color="white",
                                               fg_color=("white", "gray38"))
        self.label_rest_periods.grid(
            column=0, row=2, sticky="nswe", padx=15, pady=15)

        self.infected_cells = ctk.CTkLabel(master=self,
                                           text=f'Celdas infectadas: {self.patient.get_infected_cells().size}',
                                           height=30,
                                           corner_radius=6,
                                           text_font=("Roboto Medium", -16), text_color="white",
                                           fg_color=("white", "gray38"))
        self.infected_cells.grid(
            column=0, row=3, sticky="nswe", padx=15, pady=15)

        self.healthy_cells = ctk.CTkLabel(master=self,
                                          text=f'Celdas sanas: {self.patient.get_healthy_cells()}',
                                          height=30,
                                          corner_radius=6,
                                          text_font=("Roboto Medium", -16), text_color="white",
                                          fg_color=("white", "gray38"))
        self.healthy_cells.grid(
            column=0, row=4, sticky="nswe", padx=15, pady=15)

        # Buttons
        self.simuate_prev_period_button = ctk.CTkButton(master=self,
                                                        text="Período anterior",
                                                        command=self.simulate_prev_period)
        self.simuate_prev_period_button.grid(
            column=1, row=0, sticky="nswe", padx=15, pady=15)

        self.simulate_all_button = ctk.CTkButton(master=self,
                                                 text="Simular todo",
                                                 command=self.simulate_all)
        self.simulate_all_button.grid(
            column=1, row=1, sticky="nswe", padx=15, pady=15)

        self.simulate_next_period_button = ctk.CTkButton(master=self,
                                                         text="Siguiente período",
                                                         command=self.simulate_next_period)
        self.simulate_next_period_button.grid(
            column=1, row=2, sticky="nswe", padx=15, pady=15)

        # Frame to display matrix
        self.frame_matrix = ctk.CTkFrame(master=self)
        self.display_matrix()
        self.frame_matrix.grid(
            column=0, row=5, columnspan=2, padx=15, pady=15)

        self.patient.get_neighbors_cell_state()

    def display_matrix(self):
        color = "gray38"
        txt_color = "white"
        for r in range(self.patient.get_size()):
            for c in range(self.patient.get_size()):
                cell: Cell = self.patient.get_cell_by_row_number(r, c)
                if cell.is_infected == 1:
                    color = "#ebdbb0"
                    txt_color = "black"
                else:
                    color = "gray38"
                    txt_color = "white"
                self.label_matrix = ctk.CTkLabel(master=self.frame_matrix,
                                                 text=f'{cell.get_is_infected()}',
                                                 corner_radius=6,
                                                 width=10,
                                                 height=10,
                                                 text_font=("Roboto Medium", -15), text_color=txt_color,
                                                 bg_color=color)
                #  fg_color=("white", "gray38"))
                self.label_matrix.grid(
                    column=c, row=r, padx=2, pady=2)

    def simulate_all(self):
        print("a")

    def simulate_next_period(self):
        self.patient.simulate_next_period()
        self.display_matrix()
        self.label_rest_periods.config(
            text=f'Periodos restantes: {self.patient.periods}')
        self.healthy_cells.config(
            text=f'Celdas sanas: {self.patient.get_healthy_cells()}')
        if self.patient.periods == 0:
            self.simulate_button.config(state="normal")
            self.simulate_next_period.config(state="disabled")

    def simulate_prev_period(self):
        self.patient.simulate_prev_period()
        self.display_matrix()
        self.label_rest_periods.config(
            text=f'Periodos restantes: {self.patient.periods}')
        self.healthy_cells.config(
            text=f'Celdas sanas: {self.patient.get_healthy_cells()}')
        if self.patient.periods == 0:
            self.simulate_button.config(state="normal")
            self.simulate_next_period.config(state="disabled")
