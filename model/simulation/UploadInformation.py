from xml.dom import minidom as MD

from data.pacients.ListPacients import ListPacients


class UploadInformation:
    @staticmethod
    def xPath(ruta):
        file = MD.parse(ruta)
        create_pacient = ListPacients()
        pacients = file.getElementsByTagName("paciente")
        for pacient in pacients:
            datos_personales = pacient.getElementsByTagName("datospersonales")
            periods = pacient.getElementsByTagName("periodos")
            size_matrix = pacient.getElementsByTagName("m")
            info_matrix = pacient.getElementsByTagName("rejilla")
            if len(datos_personales) == 0 or len(periods) == 0 or len(info_matrix) == 0 or len(size_matrix) == 0:
                return False
            else:
                name = pacient.getElementsByTagName("nombre")
                age = pacient.getElementsByTagName("edad")

                verifyPersonalData = UploadInformation().verifyNameAge(name, age)
                verifyMatrixData = UploadInformation().verifyMatrix(
                    info_matrix[0])

                if verifyPersonalData and verifyMatrixData:
                    create_pacient.inserPacientAtEnd(
                        name[0].firstChild.data, age[0].firstChild.data)
                else:
                    return False

        create_pacient.show_pacients()
        return True

    @staticmethod
    def verifyNameAge(name, age):
        if len(name) == 0 or len(age) == 0:
            return False
        else:
            return True

    @staticmethod
    def verifyMatrix(matrix):
        cells = matrix.getElementsByTagName("celda")
        for cell in cells:
            row_cell = cell.getAttribute("f")
            column_cell = cell.getAttribute("c")

            if len(row_cell) == 0 or len(column_cell) == 0:
                return False
            else:
                return True
