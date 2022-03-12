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
    python_requires=">=3.8",
    install_requires=[
        {%- if cookiecutter.interface == "gui" %}
        "pysimplegui",
        {%- endif %}
        {%- if cookiecutter.use_database|lower == "y" %}
        "sqlalchemy",
        {%- endif %}
        {%- if cookiecutter.interface == "cli" or cookiecutter.use_database|lower == "y" %}
        "typer",
        {%- endif %}
    ],
    entry_points={
        "console_scripts": [
            {%- if cookiecutter.interface == "cli" %}
            "{{ cookiecutter.module_name|replace('_','-') }} = {{ cookiecutter.module_name }}:main",
            {%- endif %}
            {%- if cookiecutter.use_database|lower == "y" %}
            "initdb = {{ cookiecutter.module_name }}.create_db:main",
            {%- endif %}
        ],
        "gui_scripts": [
            {%- if cookiecutter.interface == "gui" %}
            "{{ cookiecutter.module_name|replace('_','-') }} = {{ cookiecutter.module_name }}:main"
            {%- endif %}
        ]
    },
    include_package_data=True,
    zip_safe=False)

