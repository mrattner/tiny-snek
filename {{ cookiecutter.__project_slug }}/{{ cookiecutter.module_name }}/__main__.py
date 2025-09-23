{% if cookiecutter.interface == "cli" -%}
import typer


def main():
    typer.echo("Hello World")


if __name__ == "__main__":
    typer.run(main)
{%- elif cookiecutter.interface == "gui" %}
import PySimpleGUI as sg


def main():
    layout = [[sg.Text("Your typed chars appear here:"), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key="-IN-")],
          [sg.Button("Show"), sg.Button("Exit")]]

    window = sg.Window("{{ cookiecutter.project_name }}", layout)

    # Event Loop
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Show':
            # Update the "output" text element to be the value of "input" element
            window['-OUTPUT-'].update(values['-IN-'])

    window.close()


if __name__ == "__main__":
    main()
{%- endif %}
