def markdown_to_blocks(markdown):
    split_markdown = markdown.split('\n\n')
    blocks = []
    for i in range(len(split_markdown)):
        split_markdown[i] = split_markdown[i].strip()
        if split_markdown[i] != '':
            blocks.append(split_markdown[i])

    return blocks





