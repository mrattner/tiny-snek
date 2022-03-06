from setuptools import setup, find_packages

setup(name="{{ cookiecutter.module_name }}",
    version="0.1.0",
    description="",
    long_description="",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Other/Nonlisted Topic",
    ],
    keywords="",
    url="",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author_email }}",
    license="MIT",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    install_requires=[
        {%- if cookiecutter.use_database == "y" %}
        "sqlalchemy",
        {%- endif %}
        {%- if cookiecutter.include_cli == "y" or cookiecutter.use_database == "y" %}
        "click",
        {%- endif %}
    ],
    entry_points={
        "console_scripts": [
            {%- if cookiecutter.include_cli|lower == "y" %}
            "{{ cookiecutter.module_name|replace('_','-') }} = {{ cookiecutter.module_name }}.cli:cli",
            {%- endif %}
            {%- if cookiecutter.use_database|lower == "y" %}
            "initdb = {{ cookiecutter.module_name }}.create_db:__main__",
            {%- endif %}
        ],
        "gui_scripts": [
        ]
    },
    include_package_data=True,
    zip_safe=False)

