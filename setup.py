from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="sushil sani",
    author_email="sush.sani39@gmail.com",
    installl_requires=["openai", "langchain", "langchain_community", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)