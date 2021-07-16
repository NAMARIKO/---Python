import os

# %%
# Sample_6
print("\n[Sample_6]")

dir = os.listdir()
for val in dir:
    print(val)

# Pythonの path
print(os.path)


# %%
# Sample_7
print("\n[Sample_7]")

dir = os.listdir()
for fileName in dir:
    print(os.path.abspath(fileName), end="\t\t")
    if os.path.isfile(fileName):
        print("ファイルです")
    elif os.path.isdir(fileName):
        print("ディレクトリです")
    else:
        print("その他")
