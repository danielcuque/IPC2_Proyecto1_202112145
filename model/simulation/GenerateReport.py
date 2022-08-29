import xml.etree.ElementTree as ET

from datetime import datetime
from tkinter import filedialog
from model.simulation.GenerateGraphvizDoc import GenerateGraphvizDoc
from model.simulation.UploadInformation import UploadInformation
from data.base.classes.Patient import Patient


class GenerateReport:

    def generate_report(self):
        self.upload_information = UploadInformation()
        self.list_of_patients = self.upload_information.patients_list

        # Create a document with date and time as name
        get_day = datetime.now().strftime("%Y-%m-%d")
        get_hour_minute_second = datetime.now().strftime("%H:%M:%S")
        self.report_name = f'reporte-de-pacientes-{get_day}-at-{get_hour_minute_second}.xml'

        self.path_to_write = filedialog.askdirectory() + "/" + self.report_name

        self.root_patients = ET.Element('pacientes')
        tmp = self.list_of_patients.head
        while tmp is not None:
            self.root_patients.append(
                self.create_patient_xml(tmp.get_body()))
            tmp = tmp.get_next()
        self.tree = ET.ElementTree(self.root_patients)
        self.tree.write(self.path_to_write, encoding='utf-8',
                        xml_declaration=True)
        GenerateGraphvizDoc().generate_graphviz_doc(self.path_to_write)
        return True

    def create_patient_xml(self, patient: Patient):
        patient_xml = ET.Element('paciente')
        patient_xml.append(self.create_personal_data_xml(patient))
        patient_xml.append(self.create_periods_xml(patient))
        patient_xml.append(self.create_matrix_size_xml(patient))
        patient_xml.append(self.create_diagnosis_xml(patient))
        if patient.get_period_number() > 0:
            patient_xml.append(self.create_period_number_xml(patient))
            if patient.get_period_number() > 1:
                patient_xml.append(self.create_period_span_xml(patient))

        return patient_xml

    def create_personal_data_xml(self, patient: Patient):
        personal_data_xml = ET.Element('datospersonales')
        name_xml = ET.Element('nombre')
        name_xml.text = patient.get_name()
        age_xml = ET.Element('edad')
        age_xml.text = str(patient.get_age())
        personal_data_xml.append(name_xml)
        personal_data_xml.append(age_xml)
        return personal_data_xml

    def create_periods_xml(self, patient: Patient):
        periods_xml = ET.Element('periodos')
        periods_xml.text = str(patient.get_total_periods())
        return periods_xml

    def create_matrix_size_xml(self, patient: Patient):
        matrix_size_xml = ET.Element('m')
        matrix_size_xml.text = str(patient.get_size())
        return matrix_size_xml

    def create_diagnosis_xml(self, patient: Patient):
        diagnosis_xml = ET.Element('resultado')
        diagnosis_xml.text = patient.get_disease_severity()
        return diagnosis_xml

    def create_period_number_xml(self, patient: Patient):
        period_number_xml = ET.Element('n')
        period_number_xml.text = str(patient.get_period_number())
        return period_number_xml

    def create_period_span_xml(self, patient: Patient):
        period_span_xml = ET.Element('n1')
        period_span_xml.text = str(patient.get_period_span())
        return period_span_xml
