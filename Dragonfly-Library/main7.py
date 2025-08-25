import json
import os
import re
import requests

# ------------------------
# Dragonfly Library System
# ------------------------
dragonflylibrary = {}

# ------------------------
# Session 1 - Add instrument
# ------------------------
def add_instrument(library):
    try:
        name = input("Enter instrument name: ").strip()
        if not name:
            raise ValueError("Instrument name cannot be blank.")

        if name in library:
            print("Instrument already exists.")
        else:
            development = input("Enter development location: ").strip()
            job = input("Enter job at Titan: ").strip()

            if not development or not job:
                raise ValueError("Development location and Job cannot be blank.")

            library[name] = {
                "Development": development,
                "Job": job,
                "Acronyms": {}
            }
    except ValueError as ve:
        print(f"[!] Input error: {ve}")
    return library

# ------------------------
# Session 2 - Add acronym & IAID (with validation)
# ------------------------
def add_acronym(library):
    try:
        name = input("Enter instrument name: ").strip()
        if name not in library:
            raise KeyError("Instrument not found.")

        acronym = input("Enter acronym (e.g., DraMS): ").strip().upper()
        iaid = input("Enter instrument acronym ID (e.g., 01, 02, 03...): ").strip()

        if not re.fullmatch(r"[A-Z][a-zA-Z]{2,6}", acronym):
            raise ValueError("Invalid acronym format. Must start with uppercase and be 3–7 letters.")
        if not re.fullmatch(r"\d{2,3}", iaid):
            raise ValueError("Invalid IAID format. Must be 2 or 3 digits.")

        library[name]["Acronyms"][acronym] = iaid
        print("Acronym added.")
    except KeyError as ke:
        print(f"[!] {ke}")
    except ValueError as ve:
        print(f"[!] Input error: {ve}")
    return library

# ------------------------
# Search for an instrument
# ------------------------
def search_instrument(library):
    try:
        name = input("Enter instrument name to search: ").strip()
        if name in library:
            print(f"\n{name}:")
            for key, value in library[name].items():
                print(f"  {key}: {value}")
        else:
            raise KeyError("Instrument not found.")
    except KeyError as ke:
        print(f"[!] {ke}")

# ------------------------
# Update an instrument
# ------------------------
def update_instrument(library):
    try:
        name = input("Enter instrument name to update: ").strip()
        if name not in library:
            raise KeyError("Instrument not found.")

        current = library[name]
        print("Leave blank to keep current value.")
        development = input(f"Development [{current['Development']}]: ").strip() or current['Development']
        job = input(f"Job at Titan [{current['Job']}]: ").strip() or current['Job']

        library[name]["Development"] = development
        library[name]["Job"] = job
    except KeyError as ke:
        print(f"[!] {ke}")

# ------------------------
# Base Counter Class
# ------------------------
class DragonflyLibraryCounter:
    def __init__(self, library):
        self.library = library

    def count_items(self):
        return sum(len(instr["Acronyms"]) for instr in self.library.values())

    def count_instruments(self):
        return len(self.library)

    def count_multi_acronym(self):
        return sum(1 for instr in self.library.values() if len(instr["Acronyms"]) > 1)

    def count_by_development(self, location):
        return sum(1 for instr in self.library.values() if instr["Development"].lower() == location.lower())

    def count_by_job(self, keyword):
        return sum(1 for instr in self.library.values() if keyword.lower() in instr["Job"].lower())

# ------------------------
# Save the catalog
# ------------------------
def save_catalog(library):
    try:
        os.makedirs("Library", exist_ok=True)
        filepath = os.path.join("Library", "dragonfly_catalog.txt")
        with open(filepath, 'w', encoding='utf-8') as file:
            for name, details in library.items():
                file.write(f"{name}:\n")
                for key, value in details.items():
                    file.write(f"    {key}: {value}\n")
                file.write("\n")
        print(f"[✓] Catalog saved to {filepath}")
    except Exception as e:
        print(f"[!] Error saving catalog: {e}")

# ------------------------
# Export JSON and simulate POST
# ------------------------
def export_to_json(library):
    try:
        return json.dumps(library, indent=4)
    except TypeError as e:
        print(f"[!] Error converting to JSON: {e}")
        return '{}'

def post_to_api(library_json):
    print("\n[POST] Sending data to https://api.missioncontrol.space/dragonfly")
    try:
        response = requests.post("https://api.missioncontrol.space/dragonfly", json=json.loads(library_json))
        print("[✓] API responded:", response.status_code)
        print(response.text)
    except Exception as e:
        print(f"[!] Failed to send API request: {e}")

# ------------------------
# Simulate GET API
# ------------------------
def get_from_api():
    print("\n[Simulating GET request to /api/dragonfly]")
    try:
        response_json = '''
        {
            "NewInstrument": {
                "Development": "ESA",
                "Job": "Analyze Titan surface composition",
                "Acronyms": {"NIT": "006"}
            }
        }
        '''
        return json.loads(response_json)
    except Exception as e:
        print(f"[!] Failed to simulate API GET: {e}")
        return {}

# ------------------------
# Sample data
# ------------------------
dragonflylibrary["Mass Spectrometer"] = {
    "Development": "NASA Goddard, CNES",
    "Job": "Analyze chemical components for life.",
    "Acronyms": {"DraMS": "001"}
}
dragonflylibrary["Drill for Acquisition of Complex Organics"] = {
    "Development": "Honeybee Robotics",
    "Job": "Drill and transfer samples.",
    "Acronyms": {"DrACO": "002"}
}
dragonflylibrary["Gamma-ray and Neutron Spectrometer"] = {
    "Development": "JHU APL, LLNL",
    "Job": "Measure elemental composition.",
    "Acronyms": {"DraGNS": "003"}
}
dragonflylibrary["Geophysics and Meteorology Package"] = {
    "Development": "JHU APL, JAXA",
    "Job": "Monitor atmosphere and seismic activity.",
    "Acronyms": {"DraGMet": "004"}
}
dragonflylibrary["Camera Suite"] = {
    "Development": "Malin Space Science Systems",
    "Job": "Surface and aerial imaging.",
    "Acronyms": {"DragonCam": "005"}
}

# ------------------------
# Main Interaction Loop
# ------------------------
def main():
    while True:
        print("\n--- MENU ---")
        print("1) Add instrument")
        print("2) Add acronym")
        print("3) Search instrument")
        print("4) Update instrument")
        print("5) Counts")
        print("6) Save catalog")
        print("7) Export & POST to API")
        print("8) Import from API")
        print("9) Quit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_instrument(dragonflylibrary)
        elif choice == "2":
            add_acronym(dragonflylibrary)
        elif choice == "3":
            search_instrument(dragonflylibrary)
        elif choice == "4":
            update_instrument(dragonflylibrary)
        elif choice == "5":
            counter = DragonflyLibraryCounter(dragonflylibrary)
            print(f"Total IAIDs: {counter.count_items()}")
            print(f"Total Instruments: {counter.count_instruments()}")
            print(f"Instruments with multiple acronyms: {counter.count_multi_acronym()}")
            dev = input("Development location to count (or blank): ").strip()
            if dev:
                print(f"  Instruments developed at '{dev}': {counter.count_by_development(dev)}")
            job = input("Job keyword to count (or blank): ").strip()
            if job:
                print(f"  Instruments with job containing '{job}': {counter.count_by_job(job)}")
        elif choice == "6":
            save_catalog(dragonflylibrary)
        elif choice == "7":
            json_data = export_to_json(dragonflylibrary)
            post_to_api(json_data)
        elif choice == "8":
            new_data = get_from_api()
            if new_data:
                dragonflylibrary.update(new_data)
                print("[✓] Data imported from API simulation.")
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("[!] Invalid option.")

    # ------------------------
    # Final Report
    # ------------------------
    print("\nDragonfly Library:")
    for name, data in dragonflylibrary.items():
        print(f"- {name}: {data}")

# Run the app
if __name__ == "__main__":
    main()
