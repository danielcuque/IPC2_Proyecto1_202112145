import customtkinter as ctk
from tkinter import messagebox
from data.base.classes.Cell import Cell
from data.base.classes.Patient import Patient
from data.historial.ListPatientHistorial import ListPatientHistorial
from data.simulation.DoubleLinkedList_Y import DoubleLinkedList_Y
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
        self.display_matrix(self.patient.get_matrix())
        self.frame_matrix.grid(
            column=0, row=6, columnspan=2, padx=15, pady=15)

    def display_matrix(self, matrix: DoubleLinkedList_Y):
        color = "gray38"
        txt_color = "white"
        for r in range(matrix.get_size()):
            for c in range(matrix.get_size()):
                cell: Cell = matrix.get_cell_by_row_number(r, c)
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

    def simulate_all(self):
        print("a")

    def simulate_next_period(self):
        if self.patient.get_periods() > 0:
            patient_historial = self.patient.get_historial()
            # Al principio el historial estará vacío
            if patient_historial.get_historial_size() == 0:
                patient_historial.insert_in_emptylist(
                    self.patient.get_matrix())

            # Si el periodo actual es menor que el tamaño del historial, entonces se crea una nueva matriz
            historial_size = patient_historial.get_historial_size()

            # Si el periodo actual es igual al tamaño de la matriz, significa que el siguiente periodo va a ser nuevo
            if self.current_period == (historial_size - 1):
                self.simulate_new_period(patient_historial)

            elif self.current_period < (historial_size - 1):
                # Si el periodo actual es menor que el tamaño del historial, significa que la matriz existe
                self.simulate_existing_period(patient_historial)

            # Restamos el número de períodos restantes
            self.patient.set_periods(self.patient.get_periods() - 1)

            # Mostramos la matriz actual
            self.current_period += 1
            self.display_information()

        else:
            messagebox.showerror("Error", "No hay períodos para simular")

    def simulate_prev_period(self):
        # Si el periodo actual es diferente de 0, significa que no es el estado inicial
        if self.current_period > -1:
            patient_historial = self.patient.get_historial()
            # Obtememos la matriz dependiendo del periodo anterior
            prev_matrix = patient_historial.get_node_by_index(
                self.current_period-1).get_matrix()

            # Actualizamos el periodo actual
            self.current_period -= 1
            self.patient.set_matrix(prev_matrix)
            self.display_information()

            # Mostramos la matriz
            self.display_matrix(self.patient.get_matrix())

        else:
            messagebox.showerror("Error", "No hay períodos para simular")

    def display_information(self):
        self.display_matrix(self.patient.get_matrix())
        self.label_rest_periods.configure(
            text=f'Periodos restantes: {self.patient.get_periods()}')
        self.label_infected_cells.configure(
            text=f'Celdas infectadas: {self.patient.get_infected_cells()}')
        self.healthy_cells.configure(
            text=f'Celdas sanas: {self.patient.get_healthy_cells()}')

        self.label_current_period.configure(
            text=f'Periodo actual: {self.current_period}')

    def simulate_new_period(self, patient_historial: ListPatientHistorial):
        compare_matrix = VerifyMatrix()
        # Creamos una nueva lista para el siguiente periodo y la llenamos
        new_matrix = DoubleLinkedList_Y()
        for pos_x in range(self.patient.get_size()):
            new_matrix.insert_new_column(pos_x, self.patient.get_size())
        # Después comparamos la matriz que está a la cabeza del historial con la matriz que acabamos de crear
        compare_matrix.verify_matrix(
            self.patient.get_matrix(), new_matrix)
        # Actualizamos la matriz del paciente con la matriz que acabamos de crear
        self.patient.set_matrix(new_matrix)
        patient_historial.insert_node_at_end(new_matrix)

    def simulate_existing_period(self, patient_historial: ListPatientHistorial):
        next_matrix = patient_historial.get_node_by_index(
            self.current_period+1).get_matrix()
        self.patient.set_matrix(next_matrix)

