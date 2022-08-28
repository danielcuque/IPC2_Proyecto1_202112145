# GUI Libraries
import customtkinter as ctk
from tkinter import messagebox

# Classes
from data.base.classes.Patient import Patient
from data.base.classes.Cell import Cell
from data.base.nodes.NodeForDoublyList import NodeForDoublyList

# Helpers
from model.helpers.VerifyMatrix import VerifyMatrix


class SimulationFrame(ctk.CTkFrame):
    current_period = 0

    def __init__(self, master, patient):
        super().__init__()
        self.master = master
        self.patient: Patient = patient

        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=0)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
        self.create_simulation_frame()

    def create_simulation_frame(self):

        # Labels
        if self.patient.get_historial().get_historial_size() > 0:
            self.patient.set_matrix(
                self.patient.get_historial().get_head())
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

        self.label_current_period = ctk.CTkLabel(master=self,
                                                 text=f'Periodo actual: {self.current_period}',
                                                 height=30,
                                                 corner_radius=6,
                                                 text_font=("Roboto Medium", -16), text_color="white",
                                                 fg_color=("white", "gray38"))
        self.label_current_period.grid(
            column=0, row=3, sticky="nswe", padx=15, pady=15)

        self.label_infected_cells = ctk.CTkLabel(master=self,
                                                 text=f'Celdas infectadas: {self.patient.get_infected_cells()}',
                                                 height=30,
                                                 corner_radius=6,
                                                 text_font=("Roboto Medium", -16), text_color="white",
                                                 fg_color=("white", "gray38"))
        self.label_infected_cells.grid(
            column=0, row=4, sticky="nswe", padx=15, pady=15)

        self.healthy_cells = ctk.CTkLabel(master=self,
                                          text=f'Celdas sanas: {self.patient.get_healthy_cells()}',
                                          height=30,
                                          corner_radius=6,
                                          text_font=("Roboto Medium", -16), text_color="white",
                                          fg_color=("white", "gray38"))
        self.healthy_cells.grid(
            column=0, row=5, sticky="nswe", padx=15, pady=15)

        # Buttons
        self.simuate_prev_period_button = ctk.CTkButton(master=self,
                                                        text="Período anterior",
                                                        command=self.display_prev_period)
        self.simuate_prev_period_button.grid(
            column=1, row=0, sticky="nswe", padx=15, pady=15)

        self.simulate_all_button = ctk.CTkButton(master=self,
                                                 text="Ir al estado final",
                                                 command=self.simulate_all_periods)
        self.simulate_all_button.grid(
            column=1, row=1, sticky="nswe", padx=15, pady=15)

        self.simulate_next_period_button = ctk.CTkButton(master=self,
                                                         text="Siguiente período",
                                                         command=self.simulate_next_period)
        self.simulate_next_period_button.grid(
            column=1, row=2, sticky="nswe", padx=15, pady=15)

        self.label_illness = ctk.CTkLabel(master=self,
                                          text=f'Gravedad: {self.patient.disease_severity}',
                                          height=30,
                                          corner_radius=6,
                                          text_font=("Roboto Medium", -16), text_color="white",
                                          fg_color=("white", "gray38"))
        self.label_illness.grid(
            column=1, row=3, sticky="nswe", padx=15, pady=15)

        self.label_period_number = ctk.CTkLabel(master=self,
                                                text=f'N: {self.patient.period_number}',
                                                height=30,
                                                corner_radius=6,
                                                text_font=("Roboto Medium", -16), text_color="white",
                                                fg_color=("white", "gray38"))
        self.label_period_number.grid(
            column=1, row=4, sticky="nswe", padx=15, pady=15)

        self.label_period_span = ctk.CTkLabel(master=self,
                                              text=f'N1: {self.patient.period_span}',
                                              height=30,
                                              corner_radius=6,
                                              text_font=("Roboto Medium", -16), text_color="white",
                                              fg_color=("white", "gray38"))
        self.label_period_span.grid(
            column=1, row=5, sticky="nswe", padx=15, pady=15)

        # Frame to display matrix
        self.frame_matrix = ctk.CTkFrame(master=self)
        self.display_matrix(self.patient.get_node())
        self.frame_matrix.grid(
            column=0, row=6, columnspan=2, padx=15, pady=15)

    def display_matrix(self, matrix: NodeForDoublyList):
        color = "gray38"
        txt_color = "white"
        for r in range(matrix.get_body().get_size()):
            for c in range(matrix.get_body().get_size()):
                cell: Cell = matrix.get_body().get_cell_by_row_number(r, c)
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
                self.label_matrix.grid(
                    column=c, row=r, padx=2, pady=2)

    def simulate_all_periods(self):
        while self.patient.periods > 0:
            self.get_next_period()
        self.display_information()

    def get_next_period(self):

        if self.patient.get_periods() > 0:
            patient_historial = self.patient.get_historial()
            # Si el periodo actual es igual al tamaño de la matriz, significa que el siguiente periodo va a ser nuevo
            if patient_historial.get_size() == 0:
                patient_historial.insert_new_period(self.patient.get_matrix())

            historial_size = patient_historial.get_size()

            if self.current_period == (historial_size - 1):
                VerifyMatrix().create_new_period(self.patient)

            elif self.current_period < (historial_size - 1):
                # Si el periodo actual es menor que el tamaño del historial, significa que la matriz existe
                self.simulate_existing_period()

            # Mostramos la matriz actual
            self.current_period += 1
        else:
            messagebox.showerror("Error", "No hay períodos para simular")

    def simulate_next_period(self):
        self.get_next_period()
        self.display_information()

    def display_prev_period(self):
        # Si el periodo actual es diferente de 0, significa que no es el estado inicial
        if self.current_period-1 == 0:
            self.patient.set_matrix(
                self.patient.get_historial().get_head())
            # Actualizamos el periodo actual
            self.current_period -= 1
            self.display_information()
        elif self.current_period-1 > 0:
            self.patient.set_matrix(self.patient.matrix.get_prev())
            # Actualizamos el periodo actual
            self.current_period -= 1
            self.display_information()
        else:
            messagebox.showerror("Error", "No hay períodos para simular")

    def simulate_existing_period(self):
        next_matrix = self.patient.matrix.get_next()
        self.patient.set_matrix(next_matrix)

    def display_information(self):
        self.display_matrix(self.patient.get_node())
        self.label_rest_periods.configure(
            text=f'Periodos restantes: {self.patient.get_periods()}')
        self.label_infected_cells.configure(
            text=f'Celdas infectadas: {self.patient.get_infected_cells()}')
        self.healthy_cells.configure(
            text=f'Celdas sanas: {self.patient.get_healthy_cells()}')
        self.label_current_period.configure(
            text=f'Periodo actual: {self.current_period}')
        self.label_period_number.configure(
            text=f'N: {self.patient.period_number}')
        self.label_period_span.configure(
            text=f'N1: {self.patient.period_span}')
        self.label_illness.configure(
            text=f'Enfermedad: {self.patient.disease_severity}')
