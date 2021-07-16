from functools import partial
import re


def check(ptr, str):
    for pVal in ptr:
        print("---------")
        pattern = re.compile(pVal)
        for sVal in str:
            res = pattern.search(sVal)
            if res is not None:
                m = "〇"
            else:
                m = "×"
            print(f"{pVal} = {sVal} \t{m:>10}")


# %%
# Sample_6
print("\n[Sample_6]")
ptr = ["Aplee", "Good", "tk"]
str = ["Hello", "good", "tk"]
check(ptr, str)

# %%
# Sample_7
print("\n[Sample_7]")
ptr = ["TXT", "^TXT", "TXT$", "^TXT$"]
str = ["TXT", "TXTT", "TTXT"]
check(ptr, str)  # %%

# %%
# Sample_8
print("\n[Sample_8]")
ptr = ["TXT.", "TXT..", ".TXT", "..TXT"]
str = ["TXT", "TXTT", "TXTTT", "TTXT", "TTTXT"]
check(ptr, str)

# %%
# Sample_9
print("\n[Sample_9]")
ptr = ["[012]", "[0-3]", "[^0-2]"]
str = ["0", "1", "2", "3"]
check(ptr, str)

# %%
# Sample_10
print("\n[Sample_10]")
ptr = ["T*", "T+", "T?", "T{3}"]
str = ["x", "TX", "TT", "TTT", "TTTT"]
check(ptr, str)

# %%
# Sample_11
print("\n[Sample_11]")
ptr = ["(TXT)+", "XTX|TXT"]
str = ["TX", "TXT", "XTX", "TXTXT"]
check(ptr, str)


# %%
# Sample_12
print("\n[Sample_12]")

ptr = r".(csv|html|py)$"
str = ["Sample.csv", "Sample.html", "Sample.py", "Sample.exe"]
partial = re.compile(ptr)
for val in str:
    res = partial.sub(".txt", val)
    print("置換前:", val, "置換後:", res, sep="\t")
