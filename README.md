# UOA-Calender-Sync
我想做一个日历，可以是网页版或者直接在Apple日历里修改，它可以从Canvas和SSO爬取我的课程日历和作业DDL，自动标注到日历里，然后是实时动态的，自己会更新状态（做了 没做）你也可以编辑它的状态（增删改）。这个项目的名字叫什么，要从哪里入手，分为哪几个模块，要用到什么技能（我需要有基础）

从学校网站（SSO CANVAS）抓数据 - 转换 - 同步到日历 - 可编辑 - 自动更新状态

1. 数据获取
目标：从sso拿到课表，从canvas拿到assginment_name, due_date
技能：Canvas LMS API进行http请求和json解析

2. 数据处理
目标：把原始数据变成日历事件
数据类型：title(course_name, group), due(start_time_day, start_time_clock), group
技能：Python/js数据处理，时间处理

3. 日历集成
方案A：手搓网页日历
技能：前端日历库full calender，HTML + CSS

优化版本：接入APPLE calender
