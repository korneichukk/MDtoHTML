import re


def markdown_to_blocks(markdown: str):
    markdown = re.sub(r"\n{3,}", "\n\n", markdown.strip())
    cleaned_blocks = []
    for block in markdown.split("\n\n"):
        lines = block.split("\n")
        stripped_lines = [line.strip() for line in lines]
        cleaned_blocks.append("\n".join(stripped_lines))

    return cleaned_blocks
