# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "https://yltang.cn/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Kepler",
    "type": "local",
    "path": "../Kepler"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "iyltang/site-Blog@gh-pages"
}
category_by_folder = True

# 站点设置
site_name = "原谅糖"
site_logo = "${static_prefix}mylogo.png"
site_build_date = "2019-09-03T17:44+08:00"
author = "原谅糖"
email = "952716224@qq.com"
author_homepage = "https://yltang.cn/"
description = "清醒的人最荒唐"
key_words = ['Maverick', '原谅糖', 'Kepler', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Travelling",
        "url": "https://travellings.now.sh/",
        "brief": "随机的友链总是好的"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "音乐",
        "url": "${site_prefix}music/",
        "target": "_self"
    },
    {
        "name": "友链",
        "url": "${site_prefix}links/",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "#",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "#",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "#",
        "icon": "gi gi-weibo"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "qfulUMeeHaHSTNRWkv0NtufY-9Nh9j0Va",
    "appKey": "NpoJYNLR7JX05K9gJwbnccrS",
    "visitor": True,
    "placeholder": "来畅所欲言吧~"
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="dns-prefetch" href="//yltang.cn" />
<link rel="apple-touch-icon" sizes="180x180" href="${static_prefix}mylogo.png">
<link rel="shortcut icon" href="${static_prefix}favicon.ico">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aplayer/dist/APlayer.min.css">
<style>.yue a {color: #42b983;border-bottom: 0px solid #42b983;}</style>
<script src="https://cdn.jsdelivr.net/npm/aplayer/dist/APlayer.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/meting@2/dist/Meting.min.js"></script>
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?662d4f74107525a0ad20ea78dc27c62e";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>

'''

footer_addon = '<a no-style href="http://www.beian.miit.gov.cn/" target="_blank">苏ICP备20021763号</a> | <a no-style href="https://www.upyun.com/" target="_blank">又拍云</a>'

body_addon = ''
