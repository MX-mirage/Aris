import os
import requests
from bs4 import BeautifulSoup

class ArisAI:
    def __init__(self):
        self.version = "1.0"
        self.update_url = "https://raw.githubusercontent.com/MX-mirage/Aris/main/Aris.py"
        self.script_path = os.path.abspath(__file__)  # Get script's actual location

    def learn_online(self, topic):
        """Scrapes Wikipedia for new knowledge."""
        url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        paragraphs = soup.find_all("p")
        learned_data = "\n".join([p.text for p in paragraphs[:3]])  # Get first 3 paragraphs
        return learned_data

    def update_self(self):
        """Downloads the latest version of Aris and replaces itself safely."""
        try:
            response = requests.get(self.update_url)
            new_code = response.text
            
            temp_path = self.script_path + ".new"  # Write to a temporary file first
            with open(temp_path, "w") as f:
                f.write(new_code)

            os.replace(temp_path, self.script_path)  # Replace the old script safely
            print("Aris has updated successfully! Restart to apply changes.")
        except Exception as e:
            print(f"Update failed: {e}")

    def evolve(self):
        """Modifies its own code (Example: Appends a new function)."""
        try:
            new_function = "\n    def new_feature(self):\n        return 'This is a self-added feature!'\n"

            temp_path = self.script_path + ".new"
            with open(self.script_path, "r") as f:
                lines = f.readlines()

            lines.insert(-1, new_function)  # Insert before the last line
            with open(temp_path, "w") as f:
                f.writelines(lines)

            os.replace(temp_path, self.script_path)  # Replace the old script safely
            print("Aris has evolved by adding a new feature!")
        except Exception as e:
            print(f"Evolution failed: {e}")

# Example usage
aris = ArisAI()
print("Learning about AI:", aris.learn_online("Artificial Intelligence"))

update_choice = input("Do you want Aris to update? (yes/no): ")
if update_choice.lower() == "yes":
    aris.update_self()

evolve_choice = input("Do you want Aris to evolve? (yes/no): ")
if evolve_choice.lower() == "yes":
    aris.evolve()
