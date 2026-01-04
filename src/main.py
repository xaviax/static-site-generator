import os
import shutil


def reset_public_dir(dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    os.mkdir(dest_dir)



def copy_tree(src,dest):
    pass





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




