import os
import csv
import requests
from tqdm import tqdm


# 函数：用于获取指定URL的请求和响应数据
def fetch_data(url):
    try:
        response = requests.get(url)
        return response.request.method, response.status_code, response.text
    except requests.RequestException as e:
        return None, 'Error', str(e)


# 从文本文件中读取URL
input_file = 'G:\\Bp\\Wsq\\ResponseText\\mi_subdomain.txt'

# 调试：在读取文件之前打印提示信息
print(f"正在读取文件中的URL: {input_file}")

with open(input_file, 'r', encoding='latin-1') as file:
    urls = [line.strip() for line in file if line.strip()]  # 读取非空行作为URL

# 调试：打印找到的URL数量
print(f"找到的URL总数: {len(urls)}")

# 定义总的CSV文件路径
output_file = "ResponseText/all_responses.csv"
os.makedirs("ResponseText", exist_ok=True)

# 打开CSV文件，准备写入数据
with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # 写入CSV的标题行
    csv_writer.writerow(['URL', '请求方法', '状态码', '响应内容'])

    # 遍历URL，获取数据并写入总的CSV文件中
    for url in tqdm(urls, desc='处理URL中'):
        # 调试：打印当前正在处理的URL
        print(f"正在处理URL: {url}")

        request_method, status_code, response_body = fetch_data(url)

        # 调试：打印获取到的请求方法和状态码
        print(f"获取数据 - 请求方法: {request_method}, 状态码: {status_code}")

        # 将数据写入CSV文件中
        csv_writer.writerow([url, request_method, status_code, response_body])

        # 调试：确认数据已写入
        print(f"URL {url} 的响应数据已保存到总的CSV文件中。\n")

print(f"所有响应数据已保存到 {output_file}")
