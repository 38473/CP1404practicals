class ProgrammingLanguage:
    def __init__(self, field, typing, reflection, year):
        """Initialise programming language instance."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """ returns True/False if the programming language is dynamically typed or not."""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """display the final result"""
        return f"{self.field}, {self.typing} Typing, Reflecting = {self.reflection}, First appeared in {self.year}"

