from programming_language import ProgrammingLanguage
"""Demo test code to show how to use programming language class."""
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
languages = [python, ruby, visual_basic]
print("The dynamically typed languages are: ")
for language in languages:
    if language.is_dynamic():
        print(language.field)