"""Solution for CamelCase4 Problem.
"""


class StringManipulation:
    """String manipulation class"""

    def __init__(self, input_string):
        self.string = input_string
        self.string_components = input_string.split(";")
        self.type_of_operation = self.string_components[0]
        self.type_to_generate = self.string_components[1]
        self.output_string = self.string_components[2]

    def manipulate(self):
        """Manipulate input strings

        Returns:
            str: output string
        """
        if self.type_of_operation == "S":
            self.split_string()
        else:
            self.combine()
        return self.output_string

    def combine(self):
        """Combine string"""
        cobine_list = self.output_string.split(" ")
        for count, word in enumerate(cobine_list):
            if self.type_to_generate == "V":
                if count == 0:
                    cobine_list[count] = word.lower()
                else:
                    cobine_list[count] = word.title()
            elif self.type_to_generate == "M":
                if "()" not in cobine_list:
                    cobine_list.append("()")
                if count == 0:
                    cobine_list[count] = word.lower()
                else:
                    cobine_list[count] = word.title()
            elif self.type_to_generate == "C":
                cobine_list[count] = word.title()
        self.output_string = "".join(cobine_list)
        cobine_list.clear()

    def split_string(self):
        """Split string"""
        string_to_list = list(self.output_string.split("()")[0])
        copy_string_to_list = string_to_list.copy()
        for char in string_to_list:
            if char.isupper():
                char_index = copy_string_to_list.index(char)
                if char_index != 0:
                    copy_string_to_list.insert(char_index, " ")
        self.output_string = "".join(copy_string_to_list).lower()


string_list = [
    "S;V;iPad",
    "S;M;plasticCup()",
    "C;V;mobile phone",
    "C;C;coffee machine",
    "S;C;LargeSoftwareBook",
    "C;M;white sheet of paper",
    "S;V;pictureFrame",
]

for string in string_list:
    print(StringManipulation(string).manipulate())
