由于最近在学scrapy框架，所以经常会看到各种数据写入的问题，所以在此总结一下常用的一些文件写入以及在scrapy框架里如何加入这些元素。

*仅介绍最近接触的写入方式，还有一些其他的写入方式可以在网上查阅。
*因为是在写爬虫的时候整合的这几个方法，所以都是在框架里面的，核心代码都在pipelines.py和scrapy_xm.py里面。
*scrapy_xm.py负责产生数据item，并传到pipelines.py里面，如果只是想知道数据写入部分可以不用管scrapy_xm.py部分。
*item只是表示你要传入的数据而已，建议自己弄一个test.py文件一个一个去测试这些方法。


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
第一段代码就不作说明了，跟上面txt是一样的。
第二段代码是去python官方文档查询的使用方法，作用是声明spamwriter是写入csv文件的对象。
其中要说一下的是quotechar是表明分隔符，可以在生成好的csv文件中看到同一行的数据都是用|分隔开的。
第三段代码是按行写入，一般在循环里面写入。

excle：
需要导入xlwt包和xlrd包，不过这里只用到了xlwt包，有其他需求可能会用到xlrd包。
核心语句：
f = xlwt.Workbook()
sheet = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
sheet.write(row,column,str)
f.save("scrapy.xlsx")
第一段代码是实例化Workbook对象。
第二段代码是声明xlsx文件中的表名，以及说明单元格是否可重写。
第三段代码即是写入数据，row和column负责定位，row表示行数，column表示列数，第三个参数就表示要写入的数据。
最后一段代码很直观，即保存的文件名。

接下来说到数据库的存储了。
Mysql和Mongo，数据库的存储其实都差不多，第一步连接数据库，第二步数据写入，第三步关闭数据库。
有过其他语言相关经验的人做过类似的数据库连接应该懂。
具体操作可在代码中查阅，这里就不多作说明了。
Mongo数据库的操作语句可能跟你用过的数据库语句不相同，可以在网上查阅相关语句。
有兴趣的朋友可以去百度一下Mongo和Mysql数据库的异同。
虽然查了不一定懂，但是我相信在以后的使用中也许会有哪一天醍醐灌顶大喊：原来是这样啊。

就写到这里了，如果以后想到有什么要补充的再来说明好了。
















