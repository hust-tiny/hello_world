from wordcloud import WordCloud,ImageColorGenerator
import jieba.analyse
from scipy.misc import imread
import matplotlib.pyplot as plt


txt = open("wordcloud.txt",encoding='utf-8').read()
alpha = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
tags = jieba.analyse.extract_tags(txt, topK=250, withWeight=True)
new_tags = {}
for k in range(len(tags)):
    uchar = tags[k][0][0]
    if uchar not in alpha:
        new_tags[tags[k][0]] = int(tags[k][1]*10000)
with open("xiuzheng.txt",'w',encoding='utf-8') as f:
    for i,j in tags:
        if i[0] not in alpha:
            f.write('{:15}\t{:15}'.format(i,int(j*10000))+'\n')
    f.close()

wdcloud = open("xiuzheng.txt",encoding='utf-8').read()
font = "C:\\Windows\\Fonts\\simhei.TTF"
target_coloring = imread(r'sucai.jpg')
word_cloud = WordCloud(font_path=font,background_color="white",max_words=40,max_font_size=60,mask=target_coloring).generate(wdcloud)
image_color = ImageColorGenerator(target_coloring)

plt.figure()
plt.imshow(word_cloud.recolor(color_func=image_color))
plt.axis("off")
plt.show()


word_cloud.to_file("jieguo.png")

