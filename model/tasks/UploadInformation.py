from lxml import etree

import xml.etree.ElementTree as ET
from xml.dom import minidom as MD


class UploadInformation:
    @staticmethod
    def xPath(ruta):
        tree = etree.parse(ruta)
        elements = tree.xpath('//*')
        for element in elements:
            print(element.tag)
            print(element.attrib)
            print(element.text)
            print('\n')
