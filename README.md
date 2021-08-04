# 一个Flask框架的应用
### 项目目的
对豆瓣数据进行可视化，并在前端展示出来
### 项目技术
* Flask
* Echarts
* jieba+Wordcloud
### 项目细节
* 下载网站模板找到需要的组件
* 电影页使用sqlite读取之前爬取的数据，进行表格展示
* 数据页使用Echarts制作表格
* 词云页使用jieba对长字符串进行分割，然后交给wordcloud进行词云图的绘制，最后用matplotlib进行图像绘制
### 项目改进
* 更多的数据分析项目
* 更好看的Echarts