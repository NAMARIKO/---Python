# %%
# Sample_8
import datetime
print("\n[Sample_8]")

dt = datetime.datetime.now()
list = ["月", "火", "水", "木", "金", "土", "日"]

print(f"現在:\t{dt}")
print(f"年:\t{dt.year}")
print(f"月:\t{dt.month}")
print(f"日:\t{dt.day}")
print(f"時間:\t{dt.hour}")
print(f"分:\t{dt.minute}")
print(f"秒:\t{dt.second}")
print(f"曜日:\t{list[dt.weekday()]}")


dt = dt + datetime.timedelta(days=1)
print(dt)

dt = dt - datetime.timedelta(days=1)
print(dt)


# %%
# Sample_9
print("\n[Sample_9]")

str = dt.strftime("%c")
print("現在の日時は:", str, sep="\t")

str = dt - datetime.timedelta(days=1)
str = dt.strftime("%Y-%m-%d")
print("一日後は:", str, sep="\t")
