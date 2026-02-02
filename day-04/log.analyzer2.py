import json
class LogAnalyzer:
     """
        class has 2 things
        data members (variables) & member functions (functions)
    """
     def __init__(self,file_name,output_file):
            self.file_name = file_name
            self.output_file = output_file

     def read_log(self):
        try:
            with open(self.file_name, "r") as file:
                return file.readlines()
        except FileNotFoundError:
                return []

     def analyze(self):
        log_count = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        lines = self.read_log()

        for line in lines:
            if "INFO" in line:
                log_count["INFO"] += 1
            elif "WARNING" in line:
                log_count["WARNING"] += 1
            elif "ERROR" in line:
                log_count["ERROR"] += 1

        self.write_json(log_count)
        return log_count
     def write_json(self, counts):
        with open(self.output_file, "w") as json_file:
            json.dump(counts, json_file, indent=4)
# modular
log_1 = LogAnalyzer("app.log","output1.json") # creating object
log_count = log_1.analyze()

# reusable clear # extensible
log_1 = LogAnalyzer("app2.log","output2.json") # creating object
log_count = log_1.analyze()
