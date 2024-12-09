import xmltodict


def read_xml(path: str):
    dict_xml = None
    with open(path) as f:
        xml_str = f.read()
        dict_xml = xmltodict.parse(xml_str)
    return dict_xml
