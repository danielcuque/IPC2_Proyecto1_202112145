from xml.dom import minidom as MD

from data.pacients.ListPatients import ListPatients


class UploadInformation:
    patients_list = ListPatients()

    def xPath(self, ruta):
        if ruta == "" or ruta == None:
            return False
        file = MD.parse(ruta)
        patients = file.getElementsByTagName("paciente")

        for patient in patients:

            datos_personales = patient.getElementsByTagName("datospersonales")
            periods = patient.getElementsByTagName("periodos")
            size_matrix = patient.getElementsByTagName("m")
            info_matrix = patient.getElementsByTagName("rejilla")

            if len(datos_personales) == 0 or len(periods) == 0 or len(info_matrix) == 0 or len(size_matrix) == 0:
                return False
            else:
                name = patient.getElementsByTagName("nombre")
                age = patient.getElementsByTagName("edad")

                verify_personal_data = UploadInformation().verify_name_age(name, age)

                if verify_personal_data:
                    self.patients_list.insert_patient_at_end(
                        name[0].firstChild.data, age[0].firstChild.data, int(size_matrix[0].firstChild.data), int(periods[0].firstChild.data))
                    # UploadInformation().insert_cells_at_matrix(
                    #     info_matrix[0], self.patients_list.get_patient(name[0].firstChild.data))
                else:
                    return False
        self.patients_list.show_patients()
        return True

    @staticmethod
    def verify_name_age(name, age):
        if len(name) == 0 or len(age) == 0:
            return False
        else:
            return True

    @staticmethod
    def insert_cells_at_matrix(info_matrix, patient):
        cells = info_matrix.getElementsByTagName("celda")
        for cell in cells:
            row_cell = cell.getAttribute("f")
            column_cell = cell.getAttribute("c")
            patient.get_matrix().change_cell_state(row_cell, column_cell, 1)
