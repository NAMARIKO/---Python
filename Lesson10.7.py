# %%
# Q1
import os
import datetime
print("\n[Q1]")

list = os.listdir(".")
print(list)
print(f"名前\t\t\t\tサイズ")
for dir in list:
    siz = os.path.getsize(dir)
    time = os.path.getatime(dir)
    time = datetime.datetime.fromtimestamp(time)

    print(f"{dir:<32}{siz:<10}{time}")
