from abc import ABC, abstractmethod
import json


class Report(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def generate(self):
        pass


class JSONReport(Report):
    def generate(self):
        return json.dumps(self.data, indent=2)


class CSVReport(Report):
    def generate(self):
        if not self.data:
            return ""
        headers = ','.join(self.data[0].keys())
        rows = [','.join(str(v) for v in row.values()) for row in self.data]
        return '\n'.join([headers] + rows)


class HTMLReport(Report):
    def generate(self):
        html = "<html><body><table>\n"
        if self.data:
            html += "<tr>" + \
                "".join(
                    f"<th>{k}</th>" for k in self.data[0].keys()) + "</tr>\n"
            for row in self.data:
                html += "<tr>" + \
                    "".join(f"<td>{v}</td>" for v in row.values()) + "</tr>\n"
        html += "</table></body></html>"
        return html


class XMLReport(Report):
    def generate(self):
        xml = "<?xml version='1.0'?>\n<records>\n"
        for item in self.data:
            xml += " <record>\n"
            for key, value in item.items():
                xml += f"  <{key}>{value}</{key}>\n"
            xml += "  </record>\n"
        xml += "</records>"
        return xml


class ReportFactory:
    @staticmethod
    def create_report(report_type, data):
        report_types = {
                'json': JSONReport,
                'csv': CSVReport,
                'html': HTMLReport,
                'xml': XMLReport
        }
        report_class = report_types.get(report_type.lower())
        if report_class:
            return report_class(data)
        raise ValueError(f"Unkown report type: {report_type}")


# Usage
data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}
]

json_report = ReportFactory.create_report('json', data)
print(json_report.generate())

xml_report = ReportFactory.create_report('xml', data)
print(xml_report.generate())
