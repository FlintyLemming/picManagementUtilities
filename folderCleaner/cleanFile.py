import os


# 删除所有以 txt 和 html 后缀的文件
def traverse_dir_files(root_dir, ext=None):
    paths_list = []
    for parent, _, fileNames in os.walk(root_dir):
        for name in fileNames:
            if name.startswith('.'):
                continue
            if ext:
                if name.endswith(tuple(ext)):
                    paths_list.append(os.path.join(parent, name))
                    print(os.path.join(parent, name))
                    os.remove(os.path.join(parent, name))
            else:
                paths_list.append(os.path.join(parent, name))

    return paths_list


traverse_dir_files("Z:\\写真\\个人", ext=["txt", "html"])
