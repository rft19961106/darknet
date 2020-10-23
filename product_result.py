import os

paths = r"D:\rft\2020doc\image\train\JPEGImages" # 测试图片的路径
f = open('test.txt', 'w')  # 最后得到的图片路径txt文件
filenames = os.listdir(paths)
filenames.sort()
for filename in filenames:
    out_path = "D:/rft/2020doc/image/train/JPEGImages/" + filename # 引号内为测试图片文件夹的绝对路径
    print(out_path)
    f.write(out_path + '\n')
f.close()