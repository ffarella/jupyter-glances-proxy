import setuptools
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="jupyter-glances-proxy",
    version='0.1.0',
    url="https://github.com/ffarella/jupyter-glances-proxy",
    author="ffarella",
    description="",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
	keywords=['jupyter', 'glances', 'jupyterhub'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy>=1.5.0'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'glances = jupyter_glances_proxy:setup_glances',
        ]
    },
    package_data={
        'jupyter_glances_proxy': ['icons/glances.png'],
    },
)
