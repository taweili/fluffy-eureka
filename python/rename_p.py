import os
import shutil
import pandas as pd
from pypinyin import pinyin, lazy_pinyin
from pprint import pprint


# Read the Excel file
df = pd.read_excel("list.xlsx")

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    wx_name = row["A"]
    name = row["C"]
    student_id = row["D"]
    pyname = list(map(lambda x: x.capitalize(), lazy_pinyin(name)))
    pyname = ''.join(pyname)
    filename = row["E"]

    if pd.isna(filename):
        print(f"filename is NaN for {wx_name}")
        continue

    dirname = f"作业文档\{wx_name}"
    files = os.listdir(dirname)
    # filepath = f"作业文档\{wx_name}\{filename}"
    filepath = os.path.join(dirname, files[0])

    if (not os.path.isdir(dirname)):
        print(f"dirname: {dirname} not exists")
        continue

    if (not os.path.exists(filepath)):
        print(f"filepath: {filepath} not exists")
        continue
    base_name, file_suffix = os.path.splitext(filename)
    new_filepath = os.path.join("files", f"{student_id}{pyname}{file_suffix}")
    shutil.copy(filepath, new_filepath)
