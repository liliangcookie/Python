from goose3 import Goose
from goose3.text import StopWordsChinese

url = 'https://mp.weixin.qq.com/s/HHN2_MC3L73r_iXf4zkzfQ'
g = Goose({'stopwords_class': StopWordsChinese})
text = g.extract(url=url)
print(text.cleaned_text)