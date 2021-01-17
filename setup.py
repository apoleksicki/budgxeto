import setuptools


setuptools.setup(
    name='Budgxeto',
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': 'budgxeto=budgxeto.cli:add_expense'},
)
