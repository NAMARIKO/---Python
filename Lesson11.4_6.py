import urllib.request
from html.parser import HTMLParser

"""
URLでHTMLを取得する
"""
# %%
# Sample_6
print("\n[Sample_6]")


page = urllib.request.urlopen("https://www.python.org/")
html = page.read()
str = html.decode()
print(str)

"""
HTMLを解析する
"""
# %%
# Sample_7
print("\n[Sample_7]")


class SampleHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.title = False

    def handle_starttag(self, tag, attrs):

        if tag == "title":
            self.title = True

    def handle_data(self, data: str):
        if self.title is True:
            print(f"タイトル:{data}")
            self.title = False


p = SampleHTMLParser()
p.feed(str)
p.close()
