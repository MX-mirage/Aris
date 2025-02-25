import os
import requests
from bs4 import BeautifulSoup

class ArisAI:
    def __init__(self):
        self.version = "1.0"
        self.update_url = "https://raw.githubusercontent.com/YourRepo/Aris/main/Aris.py"  # Replace with your actual repo

    def learn_online(self, topic):
        """Scrapes Wikipedia for new knowledge."""
        url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        paragraphs = soup.find_all("p")
        learned_data = "\n".join([p.text for p in paragraphs[:3]])  # Get first 3 paragraphs
        return learned_data

    def update_self(self):
        """Downloads the latest version of Aris and replaces itself."""
        try:
            response = requests.get(self.update_url)
            new_code = response.text
            
            with open(__file__, "w") as f:
                f.write(new_code)
            
            print("Aris has updated successfully! Restart to apply changes.")
        except Exception as e:
            print(f"Update failed: {e}")

    def evolve(self):
        """Modifies its own code (Example: Appends a new function)."""
        new_function = "\n    def new_feature(self):\n        return 'This is a self-added feature!'\n"
        
        with open(__file__, "r") as f:
            lines = f.readlines()
        
        lines.insert(-1, new_function)  # Insert before the last line
        with open(__file__, "w") as f:
            f.writelines(lines)
        
        print("Aris has evolved by adding a new feature!")

# Example usage
aris = ArisAI()
print("Learning about AI:", aris.learn_online("Artificial Intelligence"))

update_choice = input("Do you want Aris to update? (yes/no): ")
if update_choice.lower() == "yes":
    aris.update_self()

evolve_choice = input("Do you want Aris to evolve? (yes/no): ")
if evolve_choice.lower() == "yes":
    aris.evolve()