class myclass:
    @staticmethod
    def charCount(string):
        return len(string)
    @staticmethod
    def capitalize(string):
        return string.capitalize()
    @staticmethod
    def letter(char):
        if(char.isdigit()): return "number"
        if(char.isalpha()): return "letter"
    @staticmethod
    def toUpper(string):
        return str.upper(string)