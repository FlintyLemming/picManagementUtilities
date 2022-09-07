import os
import yaml


# 删除所有视频
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


with open('config.yml', 'rb') as file:
    conf = yaml.safe_load(file)
traverse_dir_files(conf['targetPath'], ext=["mp4", "avi", "flv", "mkv"])
