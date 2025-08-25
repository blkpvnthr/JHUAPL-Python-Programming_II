import os

# Dragonfly instrument catalog: {name: {Development, Job, Acronyms{acronym: IAID}}}
dragonflylibrary = {}

# ------------------------
# Add instrument with initial acronym
# ------------------------
def add_instrument_with_acronym(name, acronym, acronym_id, developers, job):
    if name in dragonflylibrary:
        print(f"[!] Instrument '{name}' already exists.")
    else:
        dragonflylibrary[name] = {
            "Development": developers,
            "Job": job,
            "Acronyms": {acronym.upper(): acronym_id}
        }
        print(f"[+] Sample instrument '{name}' added.")

# ------------------------
# Add instrument manually
# ------------------------
def add_instrument(library):
    name = input("Enter instrument name: ").strip()
    if name in library:
        print("[!] Instrument already exists.")
    else:
        development = input("Enter development location: ").strip()
        job = input("Enter job at Titan: ").strip()
        library[name] = {
            "Development": development,
            "Job": job,
            "Acronyms": {}
        }
        print(f"[+] Instrument '{name}' added.")
    return library

# ------------------------
# Add acronym to existing instrument
# ------------------------
def add_acronym(library):
    name = input("Enter instrument name: ").strip()
    if name in library:
        acronym = input("Enter acronym: ").strip().upper()
        iaid = input("Enter acronym ID (e.g., 001, 002): ").strip()
        library[name]["Acronyms"][acronym] = iaid
        print(f"[+] Acronym '{acronym}' added to '{name}'.")
    else:
        print("[!] Instrument not found.")
    return library

# ------------------------
# Search for instrument by name or acronym
# ------------------------
def search_instrument(library):
    term = input("Enter instrument name or acronym to search: ").strip()
    found = False
    for name, data in library.items():
        if name.lower() == term.lower() or term.upper() in data["Acronyms"]:
            print(f"\n🔍 Found '{name}':")
            print(f"  Development: {data['Development']}")
            print(f"  Job at Titan: {data['Job']}")
            print(f"  Acronyms: {data['Acronyms']}")
            found = True
    if not found:
        print("[!] No matching instrument found.")

# ------------------------
# Update instrument
# ------------------------
def update_instrument(library):
    name = input("Enter instrument name to update: ").strip()
    if name not in library:
        print("[!] Instrument not found.")
        return

    current = library[name]
    print(f"Updating '{name}' — leave blank to keep current value.")
    dev = input(f"Development [{current['Development']}]: ") or current['Development']
    job = input(f"Job at Titan [{current['Job']}]: ") or current['Job']
    library[name]["Development"] = dev
    library[name]["Job"] = job
    print(f"[~] Instrument '{name}' updated.")

# ------------------------
# Save to text file
# ------------------------
def save_catalog(library, filename="dragonfly_catalog.txt"):
    try:
        os.makedirs("Library", exist_ok=True)
        path = os.path.join("Library", filename)
        with open(path, 'w', encoding='utf-8') as file:
            for name, details in library.items():
                file.write(f"🔹 {name}\n")
                file.write(f"Development: {details['Development']}\n")
                file.write(f"Job at Titan: {details['Job']}\n")
                if details["Acronyms"]:
                    acro_str = ", ".join(f"{k}:{v}" for k, v in details["Acronyms"].items())
                    file.write(f"Acronyms: {acro_str}\n")
                else:
                    file.write("Acronyms: (none)\n")
                file.write("\n")
        print(f"[✓] Catalog saved to {path}")
    except Exception as e:
        print(f"[!] Save failed: {e}")

# ------------------------
# Counting features
# ------------------------
class DragonflyLibraryCounter:
    def __init__(self, library):
        self.library = library

    def count_items(self):
        return sum(len(d["Acronyms"]) for d in self.library.values())

    def count_instruments(self):
        return len(self.library)

    def count_multi_acronym(self):
        return sum(1 for d in self.library.values() if len(d["Acronyms"]) > 1)

    def count_by_development(self, location):
        return sum(1 for d in self.library.values() if d["Development"].lower() == location.lower())

    def count_by_job(self, keyword):
        return sum(1 for d in self.library.values() if keyword.lower() in d["Job"].lower())

# ------------------------
# Sample Data
# ------------------------
add_instrument_with_acronym("Mass Spectrometer", "DraMS", "001", "NASA Goddard, CNES", "Analyze chemical components for life.")
add_instrument_with_acronym("Drill for Acquisition of Complex Organics", "DrACO", "002", "Honeybee Robotics", "Drill and transfer samples.")
add_instrument_with_acronym("Gamma-ray and Neutron Spectrometer", "DraGNS", "003", "JHU APL, LLNL", "Measure elemental composition.")
add_instrument_with_acronym("Geophysics and Meteorology Package", "DraGMet", "004", "JHU APL, JAXA", "Monitor atmosphere and seismic activity.")
add_instrument_with_acronym("Camera Suite", "DragonCam", "005", "Malin Space Science Systems", "Surface and aerial imaging.")

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
        print("7) Quit")
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
            print("Exiting...")
            break
        else:
            print("[!] Invalid option.")

# Run the app
if __name__ == "__main__":
    main()
