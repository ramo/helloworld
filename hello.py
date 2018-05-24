class Ramo:

    def __init__(self, language):
        self.language = language

    def __str__(self):
        return "ramo"

    def set_language(self, language):
        self.language = language

    def do_program(self):
        print(f"I am doing programming on {self.language}")


if __name__ == '__main__':
    r = Ramo('Python')
    r.do_program()
    r.set_language('Java')
    r.do_program()
