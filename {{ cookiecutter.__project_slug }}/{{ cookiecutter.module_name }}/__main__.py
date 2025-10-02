{%- if cookiecutter.interface == "cli" -%}
import typer


def main():
    typer.echo("Hello World")


if __name__ == "__main__":
    typer.run(main)
{%- elif cookiecutter.interface == "gui" -%}
import tkinter as tk
from tkinter import ttk

FONT = ("Helvetica", 12)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "{{ cookiecutter.project_name }}")
        self.__set_window_geometry(400, 600)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.__frames = {}

        for cls in (StartPage, PageOne, PageTwo):
            frame = cls(container, self)
            self.__frames[cls] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def __set_window_geometry(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry(f"{width}x{height}+{x:.0f}+{y:.0f}")

    def show_frame(self, cont):
        frame = self.__frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Start Page", font=FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(
            self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne)
        )
        button.pack()

        button2 = ttk.Button(
            self, text="Visit Page 2", command=lambda: controller.show_frame(PageTwo)
        )
        button2.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One", font=FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Back to Home", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()

        button2 = ttk.Button(
            self, text="Page Two", command=lambda: controller.show_frame(PageTwo)
        )
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two", font=FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Back to Home", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()

        button2 = ttk.Button(
            self, text="Page One", command=lambda: controller.show_frame(PageOne)
        )
        button2.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
{%- endif %}
