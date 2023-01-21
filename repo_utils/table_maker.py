"""Functions and classes for generating markdown formatted tables
"""
from typing import Optional


class ColumnCountNotMatching(Exception):
    """Exception for invalid data."""

    def __init__(self, data):
        super().__init__(f"Data {data} count not matching column count")


class InvalidData(Exception):
    """Exception for when data is empty"""

    def __init__(self, reason):
        super().__init__(f"Data is {reason}")


class MakeTable:
    """Fundementals for building markdown table."""

    def __init__(
        self,
        headings: list,
        width: Optional[int] = None,
        table_name: Optional[str] = None,
        sl_no: bool = False,
    ) -> None:
        self.table_name = table_name
        self.heading = headings
        self.width = width
        self.data = []
        self.out_lines = []
        self.sl_no = sl_no

    def __repr__(self) -> str:
        pass

    def __get_width(self):
        self.width = 0
        for data_list in self.data:
            for data in data_list:
                if len(data) > self.width:
                    self.width = len(data)

    def __validate_data(self):
        if not self.data:
            raise InvalidData("Empty")
        if not isinstance(self.data, list):
            raise InvalidData("Not a list")
        for data_list in self.data:
            if not isinstance(data_list, list):
                raise InvalidData("Not a list(Inner)")
            if not len(data_list) == len(self.heading):
                raise ColumnCountNotMatching(data=data_list)

    def __add_space(self, head: list) -> str:
        split_head = list(head)
        for _ in range(self.width - len(head)):
            split_head.append(" ")
        return "".join(split_head)

    def __prepend_append(self, input_string: str) -> str:
        return f"|{input_string}|"

    def __add_new_line(self, input_string: str) -> str:
        return f"{input_string}\n"

    def __build_structure(self, input_list: list):
        self.out_lines.append(
            self.__add_new_line(self.__prepend_append("|".join(input_list)))
        )

    def __build_base(self):
        first_line = []
        second_line = []
        for head in self.heading:
            first_line.append("".join(self.__add_space(head=head.upper())))
            second_line.append("-" * self.width)
        self.__build_structure(first_line)
        self.__build_structure(second_line)

    def build(self, table_data: list) -> str:
        """Build and returns a markdown table.

        Args:
            data (list): Data for the table.

        Returns:
            str: Markdown formated table

        """
        self.data = table_data
        self.__validate_data()
        if self.sl_no:
            self.heading.insert(0, "Sl No")
        if not self.width:
            self.__get_width()
        self.__build_base()
        for count, data_lists in enumerate(self.data, start=1):
            if self.sl_no:
                data_lists.insert(0, str(count))
            out_list = []
            for data in data_lists:
                out_list.append("".join(self.__add_space(head=data)))
            self.__build_structure(out_list)
        return "".join(self.out_lines)
