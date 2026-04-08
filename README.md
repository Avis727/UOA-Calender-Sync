# UOA-Calender-Sync
我想做一个日历，可以是网页版或者直接在Apple日历里修改，它可以从Canvas和SSO爬取我的课程日历和作业DDL，自动标注到日历里，然后是实时动态的，自己会更新状态（做了 没做）你也可以编辑它的状态（增删改）

从学校网站（SSO CANVAS）抓数据 - 转换 - 同步到日历 - 可编辑 - 自动更新状态

一. 数据获取
目标：从sso拿到课表，从canvas拿到assginment_name, due_date
技能：Canvas LMS API进行http请求和json解析
过程：
1.API拿数据失败：学校不让自己生成TOKEN
1）找canvas界面域名
2）访问官方API文档 https://你的域名/doc/api/
3）创建Access Token Canvas → Account → Settings → New Access Token
怎么拿Token: 手动

2.直接在CANVAS抓包数据（爬虫登录，动态，代理）：

3.Mock 数据（自己写一份json先用着）

二. 数据处理
目标：把原始数据变成日历事件
数据类型：title(course_name, group), due(start_time_day, start_time_clock), group
技能：Python/js数据处理，时间处理

三. 日历
方案A：手搓网页日历
技能：前端日历库full calender，HTML + CSS + JS做网页日历，React

优化版本：接入APPLE calender（手机端）
技能：用ics文件（icalender）生成ics文件，用户订阅=自动更新

四. 状态管理（可增删改events）
技能：数据库存储（SQLite/MongoDB）增删查改，后端基础（Flask, Node.js）

五. 自动更新（自动同步SSO CANVAS更新）
技能：定时任务cron job + 后端定时运行（任务调度，API调用）

版本1：手动输入数据 + 网页
功能：手动输入events，显示在日历，用不同的颜色标记状态和类型（done灰色/not done其他颜色）（Assignment Quiz test红色）（LECTURE绿色）（tutorial,lab黄色）

版本2：接入API自动拉events (OAuth2自动拿token)

版本3：自动更新 + 同步

版本4：手机端 + UI优化

