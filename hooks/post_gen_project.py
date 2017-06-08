if __name__ == "__main__":
    import os

    PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
    MODULE = "{{ cookiecutter.module_name }}"
    
    def remove_file(*path_segments):
        os.remove(os.path.join(PROJECT_DIRECTORY, *path_segments))

    if "{{ cookiecutter.include_cli|lower }}" != "y":
        remove_file(MODULE, "cli.py")

    if "{{ cookiecutter.use_database|lower }}" != "y":
        remove_file("settings.ini")
        remove_file("tests", "test_session.py")
        remove_file(MODULE, "models.py")
        remove_file(MODULE, "database.py")
        remove_file(MODULE, "create_db.py")
