import os
import shutil
from gencontent import generate_page,generate_pages_recursive

def reset_public_dir(dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    os.mkdir(dest_dir)





def copy_tree(src,dest):
    print("SRC: ", src)
    print("DEST: ", dest)

    src_contents = os.listdir(src)
    for item in src_contents:
        item_src_path = os.path.join(src, item)
        item_dest_path = os.path.join(dest, item)

        print("src: ", item_src_path)
        print("dest: ", item_dest_path)

        if os.path.isfile(item_src_path):
            shutil.copyfile(item_src_path, item_dest_path)

        elif os.path.isdir(item_src_path):
            if not os.path.exists(item_dest_path):
                os.mkdir(item_dest_path)
                copy_tree(item_src_path, item_dest_path)









if __name__  == '__main__':
    this_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(this_dir)
    # the above two lines help get the directory for public
    folder_path = os.path.join(root_dir, "public")
    src_static = os.path.join(root_dir, "static")
    # now need to do the same for static directory



    print("root_dir is",root_dir)
    print("src_public_static is",src_static)
    print("public_dir is",folder_path)

    reset_public_dir(folder_path)
    copy_tree(src_static,folder_path)


    content_md = os.path.join(root_dir, "content","index.md")
    template_html = os.path.join(root_dir, "template.html")
    dest_html = os.path.join(root_dir,"public","index.html")

    """generate_page(
        content_md,
        template_html,
        dest_html,
    )"""

    content_dir = os.path.join(root_dir, "content")
    public_dir = os.path.join(root_dir, "public")


    generate_pages_recursive(content_dir,template_html,public_dir,content_dir)








