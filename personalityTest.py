import ollama  # Use ollama for loading and inference
import tkinter as tk  #used for the UI
from accelerate import Accelerator  #used to manage GPU and CPU usage


class Ai:
    def __init__(self):
        # Model Configuration
        self.model_name = "phi"  # phi is the ai we are using
        self.model = ollama.chat(model=self.model_name)  # Use ollama to load the model
        self.accelerator = Accelerator()  # Initialize Accelerator, helps with GPU usage on my computer

    def generate_career_recommendation(self, test_results):
        prompt = f"""
        You are an expert career advisor. Based on the following personality traits and interests, recommend the best career paths.
        
        Personality and Interests: {test_results}

        Provide a numbered list of 5 career suggestions. Each suggestion should include:
        - The job title
        - A short explanation (1-2 sentences) on why it fits the person, mean salary for the career, and required degree.
        - Do not include any puzzles, extra content, or logic games. Just the career suggestions.
        """
        #format the response correctly and actually call upon locally run ai. 
        response = ollama.chat(model=self.model_name, messages=[{"role": "user", "content": prompt}])

        
        
        # Extract only the career suggestions part (before the puzzle)
        if 'message' in response and hasattr(response['message'], 'content'):
            career_suggestions = response['message'].content.split("\n\n\n")[0]  # Split at extra content and get the career suggestions part
            return career_suggestions
        else:
            return "Error: Could not find the content in the response."

# Example usage
career_ai = Ai()
print(career_ai.generate_career_recommendation("I love computers and i am fairly introverted"))

class Page():
    def __init__(self, key, value):
        #Lets the object know that key and value will be referenced in other methods
        self.key = key
        self.value = value
    def show_window(self):
        #Sets up the page window
        window = tk.Toplevel(root)
        window.title(self.key)
        window.geometry("800x500")

        #Checks to see if the page is the final page in the list, if so, moves to the show_final_window instead of the next.
        if skillsList.index(self) == len(skillsList) -1:
            #Asks the question and gives 3 answers, Yes, I dont know, or No. Runs the score function if its yes or no, moves onto the final page if any button is pressed.
            tk.Label(window,text = self.key).grid(row=0, column=0, pady= 10)
            tk.Button(window, text= "Yes", command=lambda: (self.score(True),show_final_window())).grid(row=1, column=0,pady=10)
            tk.Button(window, text= "Maybe", command=lambda: (show_final_window())).grid(row=2, column=0,pady=10)
            tk.Button(window, text= "No", command=lambda: (self.score(False),show_final_window())).grid(row=3, column=0,pady=10)
        #Runs if the page is not the final page in the list
        else:
            #Asks the question and gives 3 answers, Yes, I dont know, or No. Runs the score function if its yes or no, moves onto the next page if any button is pressed, and destroys this page.
            tk.Label(window,text = self.key).grid(row=0, column=0, pady= 10)
            tk.Button(window, text= "Yes", command=lambda: (self.score(True),skillsList[skillsList.index(self) + 1].show_window(),window.destroy())).grid(row=1, column=0,pady=10)
            tk.Button(window, text= "Maybe", command=lambda: (skillsList[skillsList.index(self) + 1].show_window(),window.destroy())).grid(row=2, column=0,pady=10)
            tk.Button(window, text= "No", command=lambda: (self.score(False),skillsList[skillsList.index(self) + 1].show_window(),window.destroy())).grid(row=3, column=0,pady=10)

    def score(self,boolean):
        global weightScoring
        #If boolean is True (Yes) then add the self.value to weightScoring
        if boolean == True:
            weightScoring = [a+b for a,b in zip(weightScoring,self.value)]
        #If boolean is False (No) then subtract the self.value to weightScoring
        elif boolean == False:
            weightScoring = [a-b for a,b in zip(weightScoring,self.value)]

#Displays the final window
def show_final_window():
    #Destroys the root window (The one asking if you want to take the test) and all children
    root.destroy()
    #Sets up the page window
    window1 = tk.Tk()
    window1.title("Your score")
    window1.geometry("800x500")

    #Displays your scores
    tk.Label(window1, text=weightScoring).grid(row=0, column=0, pady= 10)
    #Destroys the window
    tk.Button(window1, text="Exit", command=window1.destroy).grid(row=1, column=0, pady= 10)

#Defines a dictionary that contains the question and respective points earned in the 5 OCEAN catagories, in order they are Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism.        
skills = {"Are you good at COMMUNICATING" : (5,4,5,4,2), "Do you work well in a TEAM?" : (4,5,4,5,2), "Are you good at PROBLEM-SOLVING?" : (5,5,3,3,2), "Are you good at TIME MANAGEMENT": (3,5,2,3,2)}
#Sets up a list that will contain all the Pages for each question
skillsList = []

#iterates through the skills dictionary, grabbing both key and value from it.
for key,value in skills.items():
    #Creates a new object that has a questions key and value
    skill = Page(key,value)
    #Adds the object to the skillsList list
    skillsList.append(skill)

#Weight Scores stand for Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism 
weightScoring = [0,0,0,0,0]

#Prevents accidentally invoking an unintended script.
if __name__ == "__main__":
    #root is the beginning page
    root = tk.Tk()
    root.title("Find Your Dream Job")
    root.geometry("800x500")
    root.resizable(False, False)

    #Button asking the user if they wish to take the test, clicking advances to next page
    tk.Button(root, text="Take Test", command=skillsList[0].show_window).pack(pady=10)
    #Button that closes everything.
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

    #Keeps the GUI window open
    root.mainloop()