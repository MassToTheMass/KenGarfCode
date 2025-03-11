import tkinter as tk

openPerson = False

def show_test_window():
    global test_window
    test_window = tk.Toplevel(root)
    test_window.title("Personality Test")
    test_window.geometry("800x500")

    tk.Label(test_window, text="Personality Test").grid(row=0, column=0, pady= 10)
    tk.Checkbutton(test_window, text="Are you an open person", variable=openPerson).grid(row=1, column=0, pady=10)
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Find Your Dream Job")
    root.geometry("800x500")
    root.resizable(False, False)

    tk.Button(root, text="Take Test", command=show_test_window).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

    root.mainloop()