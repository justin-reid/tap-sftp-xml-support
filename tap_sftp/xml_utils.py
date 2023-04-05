from xml.etree import ElementTree
import csv
import io


def convert_xml_to_csv(file_handle, xml_fields):
    root = ElementTree.fromstring(file_handle.read())

    stringOutput = io.StringIO()
    csv_writer = csv.writer(stringOutput)

    csv_header = xml_fields
    csv_writer.writerow(csv_header)

    for action in root.findall('Action'):
        action_data = []

        for field in xml_fields:
            action_data.append(action.find(field).text)

        csv_writer.writerow(action_data)

    return io.BytesIO(stringOutput.getvalue().encode('utf8'))
