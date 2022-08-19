import xml.etree.ElementTree as ET
from xml.dom import minidom as MD


class UploadInformation:
    @staticmethod
    def xPath(ruta):
        file = MD.parse(ruta)
        pacients = file.getElementsByTagName("paciente")
        for pacient in pacients:
            print(pacient.getElementByTagName())
            print(pacient.getElementsByTagName)
