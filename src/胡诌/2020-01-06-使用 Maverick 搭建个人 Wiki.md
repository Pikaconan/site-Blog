---
layout: post
title: 使用 Maverick 搭建个人 Wiki
slug: wiki-by-maverick
date: 2020/01/06 14:08:00
status: publish
author: 原谅糖
tags: 
  - Maverick
  - Wiki
excerpt: 一个新的静态博客工具。
---


Maverick 是 VOID 主题作者 [熊猫小 A](https://blog.imalan.cn/) 的新项目，是一个类似 Hexo 的静态博客生成器，具体可以查看这两篇文章 [Maverick - Go My Own Way.](https://blog.imalan.cn/archives/blog-now-powered-by-maverick/) 和 [完全使用 GitHub 写博客](https://blog.imalan.cn/archives/blog-with-github/)。

作者说得很明白了，我也不必大篇转载，主要想谈谈用 Maverick 搭建个人 Wiki 站的感受。

### 为什么要用 Maverick

作者发第一篇 Maverick 文章时，我是懵逼的，一是完全看不懂 Python，二是 VOID 已经足够好用了，为何还要造这样一个东西呢？

静态博客像一座围城，相信很多人和我一样，刚开始接触的是静态博客，比如 GitHub Pages。然后向往动态博客强大的功能扩展，尝试各种主题和插件，最后玩够了就又想回到静态博客的怀抱。

~~本站还没有切换到静态，因为我还在评估，我到底能不能放弃那些插件带来的便利，能不能放弃 VOID 的各种特性。~~真香~

正好 Maverick 更新了一款新主题 Kepler，用于搭建 Wiki 站，我便开始了尝试。

### 第一步是打开 GitHub Actions

作者教程的第一步是打开 GitHub Pages，这也没错，但是我在这里卡了很久，因为始终显示 404 无法打开站点，但是其实不要紧，继续走教程，按教程打开 GitHub Actions，或者第一步就打开 GitHub Actions 也是可以的。

### 什么是 GitHub Actions

我一开始以为这是一个类似 Webhook 的东西，但其实不是，GitHub Actions 是一个免费的测试环境，相当于一台虚拟机，直接使用仓库中的代码构建项目，将生成的文件更新到仓库的 master 或者 gh-pagse 分支。并且它是能监控仓库的每一次 push 的，这样就能做到每一次更新文章，都能自动构建站点。

### 几乎完美的写作体验

将仓库克隆到本地之后，直接在资源管理器中查看博客的源文件并用 Typora 修改，再使用作者准备好的 bat or sh 脚本将改动 push 到线上仓库中，GitHub Actions 检测到 push 会自动开始构建站点，稍等即可。

再也不用使用 Typecho 那个非常简陋的编辑器了，再也不用费劲往图床里上传再复制链接了，再也不用...

这应该是我使用过的最爽的写作方式了，没有之一。

### 后记

- favicon.ico 默认放在 staic 文件里，还必须在 head 标签里加上`<link rel="shortcut icon" href="${static_prefix}favicon.ico">`才能让 favicon.ico 读取正常。

- jsDelivr 只能加速静态文件和图片，所以如果你访问站点，首先就得忍受访问 GitHub 的响应速度，然后才能愉快地访问其他资源，并且文章也没办法获得加速。最后我只好套一个国内的 CDN 服务，站点才变得非常顺畅。
