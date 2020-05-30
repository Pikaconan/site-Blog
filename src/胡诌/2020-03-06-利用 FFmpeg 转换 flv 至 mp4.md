---
layout: post
title: 利用 FFmpeg 转换 flv 至 mp4
slug: ffmpeg-flv-mp4
date: 2020/03/06 23:48:00
status: publish
author: 原谅糖
tags: 
  - FFmpeg
excerpt: FFmpeg 是个好东西。
---

又拍云 CDN 实在太便宜了，几个月下来，通过又拍云联盟获得的代金券才用了七毛钱（其实是本站没啥人看）。看到 Maverick 集成了 Dplayer 插件，于是打算放一个视频上来。

从 B 站下了个视频准备上传引用，突然发现视频是 flv 格式的，Dplayer 调用需要额外加载`flv.min.js`，于是打算将 flv 转换成 mp4。

因为 flv 和 mp4 的编码都是 h.264，只是封装格式不一样，所以完全没必要使用格式工厂这种重工具，事实上我不是很喜欢格式工厂的远古设计，一般用完就卸载了。

可以使用 FFmpeg 来转换视频。

### 下载

到 [这里](https://ffmpeg.zeranoe.com/builds/) 下载 Windows 版 FFmpeg。

### 设置

将下载好的 FFmpeg 解压，复制里面的 bin 文件夹路径，然后在此电脑上右键-属性-高级系统设置-环境变量，找到系统变量里的 path，新建一条，粘贴 bin 的路径，确定。

### 开始

将需要转换的视频文件放入 bin 文件夹中，按住 shift 键+鼠标右键，选择在此处打开 Powershell 窗口，输入命令：

```
ffmpeg -i input.flv output.mp4
```

`input`是需要被转换的视频名称，`output`是最终输出的视频名称，然后耐心等待即可。

### 后记

等我做好这一切，push 上去才发现 Kepler 不支持 Dplayer，伤心。