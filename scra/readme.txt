由于最近在学scrapy框架，所以经常会看到各种数据写入的问题，所以在此总结一下常用的一些文件写入以及在scrapy框架里如何加入这些元素。

*仅介绍最近接触的写入方式，还有一些其他的写入方式可以在网上查阅。

首先说一下涉及的文件类型以及数据库：

txt
csv
excle
Mysql
Mongo

其中txt，csv,excle是一类，Mysql和Mongo是一类。

txt:
最简单的写入，无需导入其他包即可实现。
核心语句：
with open('scrapy.txt','w',encoding='utf-8') as f:
	f.write(str)
不需要写关闭语句，数据写完后自动关闭。
第一个参数：scrapy.txt即文件名。
第二个参数：

	w：以写方式打开，

	a：以追加模式打开 (从 EOF 开始, 必要时创建新文件)

	r+：以读写模式打开

	w+：以读写模式打开 (参见 w )

	a+：以读写模式打开 (参见 a )

	rb：以二进制读模式打开

	wb：以二进制写模式打开 (参见 w )

	ab：以二进制追加模式打开 (参见 a )

	rb+：以二进制读写模式打开 (参见 r+ )

	wb+：以二进制读写模式打开 (参见 w+ )

	ab+：以二进制读写模式打开 (参见 a+ )
*有时候错误提示写入数据是byte格式的时候需要使用二进制模式打开
第三个参数：很明显是编码格式，看需要进行更改。

csv:
需要导入csv包。
核心语句：
with open('scrapy.csv','a',encoding='utf-8') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(str1,str2,str3)

















