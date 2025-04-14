import xml.etree.ElementTree as ET
import json
from typing import Dict, List


class AWSMetrics:
    def get_metrics(self) -> str:
        return '{"cpu_usage": 75, "memory_usage": 60}'


class AzureMetrics:
    def get_metrics(self) -> str:
        return "<metrics><cpu_usage>80</cpu_usage><memory_usage>50</memory_usage></metrics>"


class GoogleCloudMetrics:
    def get_metrics(self) -> List[str]:
        return ["cpu_usage", "90", "memory_usage", "40"]


class StandardizedMetrics:
    def get_json(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")


class AWSAdapter(StandardizedMetrics):
    def __init__(self, aws_metrics: AWSMetrics):
        self.aws_metrics = aws_metrics

    def get_json(self) -> str:

        return self.aws_metrics.get_metrics()


class AzureAdapter(StandardizedMetrics):
    def __init__(self, azure_metrics: AzureMetrics):
        self.azure_metrics = azure_metrics

    def get_json(self) -> str:

        xml_string: str = self.azure_metrics.get_metrics()
        root = ET.fromstring(xml_string)
        data: Dict[str, str] = {child.tag: child.text for child in root}
        return json.dumps(data)


class GoogleCloudAdapter(StandardizedMetrics):
    def __init__(self, google_cloud_metrics: GoogleCloudMetrics):
        self.google_cloud_metrics = google_cloud_metrics

    def get_json(self) -> str:

        raw_data: List[str] = self.google_cloud_metrics.get_metrics()
        data: Dict[str, str] = {
            raw_data[i]: raw_data[i + 1] for i in range(0, len(raw_data), 2)
        }
        return json.dumps(data)


if __name__ == "__main__":

    aws: AWSMetrics = AWSMetrics()
    azure: AzureMetrics = AzureMetrics()
    google_cloud: GoogleCloudMetrics = GoogleCloudMetrics()

    aws_adapter: AWSAdapter = AWSAdapter(aws)
    azure_adapter: AzureAdapter = AzureAdapter(azure)
    google_cloud_adapter: GoogleCloudAdapter = GoogleCloudAdapter(google_cloud)

    print("AWS Metrics:", aws_adapter.get_json())
    print("Azure Metrics:", azure_adapter.get_json())
    print("Google Cloud Metrics:", google_cloud_adapter.get_json())
