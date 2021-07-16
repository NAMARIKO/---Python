import importModule as im
from importModule import module_2 as m2
# %%
# Sample_6
print("\n[Sample_6]")

imM = im.module_2(
    "namari", 27, "email@gmail.com", "000-0000-0000")
imM.getData()

m2M = m2(
    "namari", 27, "email@gmail.com", "000-0000-0000")
print(m2M.getTel())
