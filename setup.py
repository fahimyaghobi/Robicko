from setuptools import setup, find_packages

setup(
    name="robicko",  # اسم کتابخونه روی PyPI
    version="0.1.0",  # ورژن اولیه
    author="fahim yaghobi",
    author_email="09035499040f@gmail.com",
    description="A simple Rubika bot library",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/robicko",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # یا هر لایسنس دیگه
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests",  # وابستگی‌ها
        "aiohttp"
    ],
) 