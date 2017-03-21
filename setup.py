from setuptools import setup

setup(
    name='grassy',
    version='1.0',

    py_modules=[
        'grassy'
    ],
    install_requires=[
        'Click',
        'Jinja2',
        'Markdown',
    ],
    entry_points="""
        [console_scripts]
        grassy=grassy:cli
    """
)
