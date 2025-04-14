from abc import ABC, abstractmethod


class DataPipeline(ABC):
    def process_pipeline(self):
        self.load_data()
        self.process_data()
        self.save_data()

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass


class CSVDataPipeline(DataPipeline):
    def load_data(self):
        print("Loading data from CSV file")

    def process_data(self):
        print("Processing data from CSV")

    def save_data(self):
        print("Saving processed data to CSV file")


class JSONDataPipeline(DataPipeline):
    def load_data(self):
        print("Loading data from JSON file")

    def process_data(self):
        print("Processing data from JSON")

    def save_data(self):
        print("Saving processed data to JSON file")

csv = CSVDataPipeline()
csv.process_pipeline()