import csv
import sys

def csv_to_markdown(csv_file_path, md_file_path):
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            # 读取CSV文件
            csv_reader = csv.reader(csv_file)
            
            # 获取表头
            headers = next(csv_reader)
            
            # 准备markdown内容
            md_content = []
            
            # 添加表头
            md_content.append('| ' + ' | '.join(headers) + ' |')
            
            # 添加分隔行
            md_content.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')
            
            # 添加数据行
            for row in csv_reader:
                md_content.append('| ' + ' | '.join(row) + ' |')
            
            # 写入markdown文件
            with open(md_file_path, 'w', encoding='utf-8') as md_file:
                md_file.write('\n'.join(md_content))
                
        print(f"转换成功！Markdown文件已保存为: {md_file_path}")
        
    except FileNotFoundError:
        print(f"错误：找不到CSV文件 {csv_file_path}")
    except Exception as e:
        print(f"发生错误：{str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python csv_to_markdown.py 输入文件.csv 输出文件.md")
    else:
        csv_file_path = sys.argv[1]
        md_file_path = sys.argv[2]
        csv_to_markdown(csv_file_path, md_file_path)