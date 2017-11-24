import webbrowser

global a
global b
a = 2
b = 4


def link():
    global a
    global b
    x = input("Enter your link\n");
    webbrowser.open(x)
    while a != b:
        link()

link()
