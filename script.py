import base64

# 假设图片内容已经读取为字节数据
with open("1.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

print(encoded_string)