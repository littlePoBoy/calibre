# calibre-recipes
recipe来抓取网页生成kindle可用的mobi格式电子书

## 电脑安装Calibre

## 下载calibre源码，并根据自己的情况做修改，详情见calibre仓库,本仓库主要修改了src\calibre\web\fetch\simple.py:290  针对特定网站的失败重试

## 进入D:\pyprojects\calibre\src  代码路径下

执行以下命名
> set CALIBRE_DEVELOP_FROM=D:\pyprojects\calibre\src
>
> echo %CALIBRE_DEVELOP_FROM%
>
回显成功即可

## 编写recipe脚本

## 利用ebook-convert转化为电子书格式
> ebook-convert devops.recipe devops.mobi
>
> ebook-convert devops.recipe devops.epub

> devops.recipe是用来抓取某一章节生成对用的电子书
>
> jishu.recipe是用来抓取整个网站内容生成电子书


> ebook-convert D:\Software\calibre\recipes\RPC实战与核心原理.recipe D:\Software\calibre\书库\RPC实战与核心原理.epub
