from setuptools import setup, find_packages

setup(
    name='tictactoe',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'tictactoe_agent = tictactoe.run:main'
        ]
    }
)