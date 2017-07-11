# JobSpiderDjango

该项目包含以下三部分：

* 爬虫: 负责拉钩和智联职位信息的数据抓取，解析，存库，详情请参见 JobSpiderScrapy 仓库
* 服务端：服务端，负责为客户端提供数据接口
* 移动端：负责在 Android 端展示爬取到的数据， 详情请参见 JobSpiderAndroid 仓库

本仓库是该项目的服务端源码，主要是基于 Django，为移动端数据提供接口。