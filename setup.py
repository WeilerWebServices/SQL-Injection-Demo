import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="injectiondemo"
    version="0.1.0",
    url="https://github.com/WeilerWebServices/SQL-Injection-Demo",
    description="An insecure application to demo SQL injection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)

