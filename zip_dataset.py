# 将一个目录下的所有文件和文件夹按照原来的文件结构打包，每个包不超过10g

import zipfile
import os
from tqdm import tqdm

dataset_dir = "/home/lin/Desktop/github/mini/jinzhangpeng_shop_mini/"
zip_dir = "/home/lin/Desktop/zip"
dataset_name = "siim"

zip_num = 1
curr_name = "{}-{}.zip".format(dataset_name, zip_num)
curr_zip_path = os.path.join(zip_dir, curr_name)
f = zipfile.ZipFile(curr_zip_path, "a", zipfile.ZIP_DEFLATED)

files_list = []
list_size = 0
zip_tot_size = 9.7 * 1024 * 128
zip_left_size = zip_tot_size
# 9.7 * 1024 * 1024 * 1024


for dirpath, dirnames, filenames in tqdm(os.walk(os.path.join(dataset_dir))):
    print(dirpath, filenames)
    for filename in filenames:
        files_list.append(
            [
                os.path.join(dirpath, filename),
                os.path.join(dirpath[len(dataset_dir) :], filename),
            ]
        )
        list_size += os.path.getsize(os.path.join(dirpath, filename))
        if list_size >= zip_left_size * 1.1:  # 如果当前列表中未压缩文件的大小大于 1.1 倍zip包能装的大小
            # 将列表里所有的文件写入zip
            for pair in files_list:
                f.write(pair[0], pair[1])
            curr_size = os.path.getsize(curr_zip_path)
            files_list = []
            if curr_size >= zip_tot_size:
                f.close()
                zip_num += 1
                curr_name = "{}-{}.zip".format(dataset_name, zip_num)
                curr_zip_path = os.path.join(zip_dir, curr_name)
                f = zipfile.ZipFile(curr_zip_path, "a", zipfile.ZIP_DEFLATED)
            else:
                zip_left_space = zip_tot_size - curr_size

if len(files_list) != 0:
    for pair in files_list:
        f.write(pair[0], pair[1])
    curr_size = os.path.getsize(curr_zip_path)
    files_list = []
    f.close()


# f.write(
#     os.path.join(dirpath, filename),
#     os.path.join(dirpath[len(dataset_dir) :], filename),
# )