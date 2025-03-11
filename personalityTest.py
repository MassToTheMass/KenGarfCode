import tkinter as tk

class Page():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def show_window(self):
        window = tk.Toplevel(root)
        window.title(self.key)
        window.geometry("800x500")

        tk.Label(window,text = self.key).grid(row=0, column=0, pady= 10)
        tk.Button(window, text= "Yes", command=lambda: (self.score(True),skillsList[1].show_window(),window.destroy())).grid(row=1, column=0,pady=10)
        tk.Button(window, text= "No", command=lambda: (self.score(False),skillsList[1].show_window(),window.destroy())).grid(row=1, column=1,pady=10)
    def score(self,boolean):
        global weightScoring
        if boolean == True:
            weightScoring = [a+b for a,b in zip(weightScoring,self.value)]
            print(weightScoring)
        
        
"""
for key, value in skills.items():
        tk.Checkbutton(test_window,text=key, variable = openPerson).grid(row=skillsLocation.index(key), column=0, pady=10)
"""
skills = {"Are you an open person?" : [1,0,0,2,0], "Do you like people?" : [0,1,0,1,1], "Do you enjoy labor?" : [0,0,3,0,0]}
for key,value in skills.items():
    skillsButtonate = {}
skillsLocation = list(skills.keys())
skillsList = []

for key,value in skills.items():
    skill = Page(key,value)
    skillsList.append(skill)

print(skillsList)

weightScoring = [0,0,0,0,0]

"""def show_test_window():
    global test_window
    test_window = tk.Toplevel(root)
    test_window.title("Personality Test")
    test_window.geometry("800x500")

    tk.Label(test_window, text="Personality Test").grid(row=0, column=0, pady= 10)
    """


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Find Your Dream Job")
    root.geometry("800x500")
    root.resizable(False, False)

    tk.Button(root, text="Take Test", command=skillsList[0].show_window).pack(pady=10)
    #tk.Button(root, text="Take Test", command=show_test_window).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

    root.mainloop()