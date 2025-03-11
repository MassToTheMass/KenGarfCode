import tkinter as tk

class Page():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def show_window(self):
        window = tk.Toplevel(root)
        window.title(self.key)
        window.geometry("800x500")

        if skillsList.index(self) == len(skillsList) -1:
            tk.Label(window,text = self.key).grid(row=0, column=0, pady= 10)
            tk.Button(window, text= "Yes", command=lambda: (self.score(True),show_final_window(),window.destroy())).grid(row=1, column=0,pady=10)
            tk.Button(window, text= "Maybe", command=lambda: (show_final_window(),window.destroy())).grid(row=2, column=0,pady=10)
            tk.Button(window, text= "No", command=lambda: (self.score(False),show_final_window(),window.destroy())).grid(row=3, column=0,pady=10)
        else:
            tk.Label(window,text = self.key).grid(row=0, column=0, pady= 10)
            tk.Button(window, text= "Yes", command=lambda: (self.score(True),skillsList[skillsList.index(self) + 1].show_window(),window.destroy())).grid(row=1, column=0,pady=10)
            tk.Button(window, text= "Maybe", command=lambda: (skillsList[skillsList.index(self) + 1].show_window(),window.destroy())).grid(row=2, column=0,pady=10)
            tk.Button(window, text= "No", command=lambda: (self.score(False),skillsList[skillsList.index(self) + 1].show_window(),window.destroy())).grid(row=3, column=0,pady=10)

    def score(self,boolean):
        global weightScoring
        if boolean == True:
            weightScoring = [a+b for a,b in zip(weightScoring,self.value)]
        elif boolean == False:
            weightScoring = [a-b for a,b in zip(weightScoring,self.value)]


def show_final_window():
    root.destroy()
    window = tk.Tk()
    window.title("Your score")
    window.geometry("800x500")
    tk.Label(window, text=weightScoring).grid(row=0, column=0, pady= 10)
    tk.Button(window, text="Exit", command=window.destroy).grid(row=1, column=0, pady= 10)

    
    

skills = {"Are you good at COMMUNICATING" : (2,3,5,5,1), "Do you work well in a TEAM?" : (3,2,5,5,1), "Are you good at PROBLEM-SOLVING?" : (5,4,0,0,1)}
for key,value in skills.items():
    skillsButtonate = {}
skillsLocation = list(skills.keys())
skillsList = []

for key,value in skills.items():
    skill = Page(key,value)
    skillsList.append(skill)



weightScoring = [0,0,0,0,0]


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Find Your Dream Job")
    root.geometry("800x500")
    root.resizable(False, False)

    tk.Button(root, text="Take Test", command=skillsList[0].show_window).pack(pady=10)

    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

    root.mainloop()