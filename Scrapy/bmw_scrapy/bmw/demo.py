import os

print(os.path.dirname(os.path.dirname(__file__)))
print(os.path.join(os.path.dirname(os.path.dirname(__file__)), "images"))
print(os.path.dirname(__file__))

images_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "images")
# os.path.exists判断路径是否存在
if not os.path.exists(images_path):
    os.mkdir(images_path)
    print("文件夹不存在")
else:
    print("文件夹存在")
