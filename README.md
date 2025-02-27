# 豆瓣电影导出工具

这是一个用于导出和展示豆瓣电影数据的工具和个人观影记录。

## 项目结构

- `csv_to_markdown.py`: CSV转Markdown的Python脚本
- `movie_export.csv`: 从豆瓣导出的原始电影数据
- `豆瓣电影.md`: 转换后的Markdown格式电影列表

## 使用方法

1. 从豆瓣导出电影数据为CSV格式
2. 使用转换脚本将CSV转为Markdown：

```bash
python csv_to_markdown.py movie_export.csv 豆瓣电影.md
```

## 功能特点

- 支持UTF-8编码
- 自动处理CSV格式转换为Markdown表格
- 保留原始数据的同时提供更好的展示格式

## 注意事项

- 确保Python环境中有相关依赖
- 输入文件需要是UTF-8编码的CSV格式
- 建议使用相对路径运行脚本