from markdown_blocks import markdown_to_html_node
import os

def extract_title(markdown):
    split_markdown = markdown.split('\n')
    for line in split_markdown:
        if line.startswith('# '):
            return line[2:].strip()

    raise Exception('No title found')


def generate_page(from_path, template_path, dest_path, basepath):
    print(f'from_path:{from_path}\ntemplate_path:{template_path}\ndest_path:{dest_path}')

    with open(from_path,'r') as file:
        file_contents = file.read()

    with open(template_path,'r') as file:
        template_contents = file.read()


    html_node = markdown_to_html_node(file_contents)
    html=html_node.to_html()
    title = extract_title(file_contents)

    template_contents = template_contents.replace("{{ Title }}", title)
    template_contents = template_contents.replace("{{ Content }}", html)

    template_contents = template_contents.replace('href="/', 'href="' + basepath)
    template_contents = template_contents.replace('src="/', 'src="' + basepath)



    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path,'w') as file:
        file.write(template_contents)



def generate_pages_recursive(dir_path_content,template_path,dest_dir_path, content_root,base_path):
    entries = os.listdir(dir_path_content)
    for entry in entries:
        entry_path = os.path.join(dir_path_content,entry)

        if os.path.isdir(entry_path):
            generate_pages_recursive(entry_path,template_path,dest_dir_path,content_root,base_path)

        elif os.path.isfile(entry_path) and entry_path.endswith('.md'):
            rel_path = os.path.relpath(entry_path, content_root)

            rel_html_path = rel_path.replace(".md",".html")
            dest_path = os.path.join(dest_dir_path,rel_html_path)
            generate_page(entry_path, template_path, dest_path,base_path)

