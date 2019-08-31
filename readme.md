selenium环境准备
安装selenium
pip install selenium
查找是否安装好selenium
pip show selenium

下载好chrome和对应版本chromedriver

mac
chromedriver放置目录
/user/local/bin

from selenium import webdriver
driver = webdriver.Chrome()
driver.get(‘http://www.baidu.com’)

drvier.quit()



frame框架定位
切换frame
from selenium import webdriver
driver =webdriver.Ie()
driver.switch_to.frame(“frame1”)
driver.switch_to.frame(“leftframe”)
#索引定位
driver.switch_to.frame(0)



嵌套frame
当某个frame中潜逃了其他的frame时，切换frame则需要潜逃结构逐层切换
<html>
<head>
	<title>嵌套切换</title>
</head>
<body>
	<iframe id = “frame1”>
		<iframe id = “frame2”/>
</iframe>
</body>
</html>

html中潜逃了frame2，如果需要定位frame2中的元素，则切换frame应当逐层切换
通过id切换到frame1
driver.swtich_to.frame(“frame1”)
通过id切换到frame2
driver.switch_to frame(“frame2”)
通过frame2切换到frame1
driver.switch_to.parent_frame()
返回上一层frame中，类似于回退效果，当上一层时住文档时，该方法无效
回退主frame
定位到主文档的元素
driver.switch_to.default_contect()