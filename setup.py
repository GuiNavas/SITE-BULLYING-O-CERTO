from setuptools import setup, find_packages

setup(
    name="contra-o-bullying",
    version="1.0.0",
    description="Site de conscientização sobre bullying",
    author="Guilherme Navasconi e Daniel Martins",
    packages=find_packages(),
    install_requires=[
        "Flask==2.3.3",
        "matplotlib==3.7.2",
        "Werkzeug==2.3.7",
        "gunicorn==21.2.0",
        "Pillow==10.0.1",
        "numpy==1.24.3"
    ],
    python_requires=">=3.8",
)
