import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="overloads",
    version="1.7",
    author="jian.zhang",
    author_email="zj19180525254@163.com",
    description="Implement the function overload in Python by the decorator named @overloads",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhangjian-ai/pypi/blob/master/packaging_tutorial/overload/overload/overload.py",
    packages=setuptools.find_packages(include=['overloads']),  # 找到需要打包的文件
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

# 在当前目录下打包并上传
# python3 setup.py sdist
# python3 setup.py sdist upload
