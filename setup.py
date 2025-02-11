from setuptools import setup, find_packages

setup(
    name="creditoruralBC",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Bruno Campos",
    description="Um pacote para acessar dados de crédito rural do Banco Central do Brasil, ainda em construção",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/BrunoTCampos/credito_ruralBC.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)