from setuptools import setup, find_packages

setup(
    name="clever_prompt_detector",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "multiprocess>=0.70.15",
        "pandas>=2.2.0"
    ],
    author="foggystar",
    description="A tool to detect prompt injection attacks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/clever_prompt_detector",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)