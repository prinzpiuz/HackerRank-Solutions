"""A script to generate README for this repo
"""

import os
from table_maker import MakeTable

ALLOWED_FILE_TYPES = [".py", ".go"]


def get_language(val: str) -> str:
    """Get progarmming language used.

    Args:
        val (str): Extention to find language used.

    Returns:
        str: Extention
    """
    if val == ".py":
        return "Python"
    if val == ".go":
        return "Go"
    return ""


def get_markdown_link(val: str) -> str:
    """Get markdown link for path

    Args:
        val (str): Path for link

    Returns:
        str: Markdown link
    """
    return f"[{val}]({val})"


if __name__ == "__main__":
    dir_list = os.listdir(".")
    data = []
    for file in dir_list:
        if os.path.isfile(file) and (os.path.splitext(file)[1] in ALLOWED_FILE_TYPES):
            file_name = os.path.splitext(file)[0]
            file_name = file_name.split("_")
            file_name = " ".join(file_name).title()
            file_type = get_language(os.path.splitext(file)[1])
            file_path = get_markdown_link(os.path.normpath(file))
            data.append([file_name, file_type, file_path])
    with open("README.MD", "w", encoding="UTF-8") as readme_file:
        readme_file.write("# My Solutions To HackerRank \n")
        readme_file.write("#### Contents \n")
        readme_file.writelines(
            MakeTable(headings=["problem", "language", "file"], sl_no=True).build(
                table_data=data
            )
        )
        readme_file.write("\n***\n")
        readme_file.write(
            "This is an auto generated file using [this](repo_utils/readme_builder.py)\n"
        )
