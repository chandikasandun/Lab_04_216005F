class Subject:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_subject_info(self):
        return f"Subject: {self.name}, Code: {self.code}"
