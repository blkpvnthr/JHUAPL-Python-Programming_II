"""
In this session, you will start building a simple Python application to manage the scientific instruments aboard NASA's Dragonfly mission to Titan.
"""
import os

# Dragonfly instrument catalog
dragonflylibrary = {}

# Add an instrument
def add_instrument(name, acronym, acronym_id, developers, job):
    if acronym in dragonflylibrary:
        print(f"[!] Instrument '{acronym}' already exists.")
    else:
        dragonflylibrary[acronym] = {
            "Name": name,
            "Acronym ID": acronym_id,
            "Developers": developers,
            "Job at Titan": job
        }
        print(f"[+] Instrument '{acronym}' added.")

# Search for an instrument
def search_instrument(acronym):
    instrument = dragonflylibrary.get(acronym)
    if instrument:
        print(f"\nFound '{acronym}':")
        for key, value in instrument.items():
            print(f"  {key}: {value}")
    else:
        print(f"[!] No instrument found with acronym '{acronym}'.")

# Update an instrument
def update_instrument(acronym):
    if acronym not in dragonflylibrary:
        print(f"[!] No instrument found with acronym '{acronym}'.")
        return

    print(f"Updating '{acronym}': Leave blank to keep current value.")
    current = dragonflylibrary[acronym]
    name = input(f"Name [{current['Name']}]: ") or current['Name']
    acronym_id = input(f"Acronym ID [{current['Acronym ID']}]: ") or current['Acronym ID']
    developers = input(f"Developers [{current['Developers']}]: ") or current['Developers']
    job = input(f"Job at Titan [{current['Job at Titan']}]: ") or current['Job at Titan']

    dragonflylibrary[acronym] = {
        "Name": name,
        "Acronym ID": acronym_id,
        "Developers": developers,
        "Job at Titan": job
    }
    print(f"[~] Instrument '{acronym}' updated.")

# Save the Dragonfly library to a file
def save_catalog(filename=None):
    try:
        if filename is None:
            filename = "dragonfly_catalog.txt"
        os.makedirs("Dragonfly-Library", exist_ok=True)
        filepath = os.path.join("Dragonfly-Library", filename)

        with open(filepath, 'w', encoding='utf-8') as file:
            for acronym, details in dragonflylibrary.items():
                file.write(f"{acronym}:\n")
                for key, value in details.items():
                    file.write(f"    {key}: {value}\n")
                file.write("\n")

        print(f"[✓] Catalog successfully saved to '{filepath}'")
    except Exception as e:
        print(f"[!] Failed to save catalog: {e}")

# Sample data
add_instrument("Mass Spectrometer", "DraMS", "001", "NASA Goddard, CNES", "Analyze chemical components for life.")
add_instrument("Drill for Acquisition of Complex Organics", "DrACO", "002", "Honeybee Robotics", "Drill and transfer samples.")
add_instrument("Gamma-ray and Neutron Spectrometer", "DraGNS", "003", "JHU APL, LLNL", "Measure elemental composition.")
add_instrument("Geophysics and Meteorology Package", "DraGMet", "004", "JHU APL, JAXA", "Monitor atmosphere and seismic activity.")
add_instrument("Camera Suite", "DragonCam", "005", "Malin Space Science Systems", "Surface and aerial imaging.")

# Simple menu
def main_menu():
    while True:
        print("\n--- Dragonfly Library ---")
        print("1. View All Instruments")
        print("2. Search Instrument")
        print("3. Update Instrument")
        print("4. Add Instrument")
        print("5. Save Catalog to File")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            for acronym in dragonflylibrary:
                search_instrument(acronym)

        elif choice == '2':
            acronym = input("Enter acronym to search: ")
            search_instrument(acronym)

        elif choice == '3':
            acronym = input("Enter acronym to update: ")
            update_instrument(acronym)

        elif choice == '4':
            name = input("Enter full name: ")
            acronym = input("Enter acronym (e.g., DraMS): ")
            acronym_id = input("Enter acronym ID (e.g., 001): ")
            developers = input("Enter developers: ")
            job = input("Enter job at Titan: ")
            add_instrument(name, acronym, acronym_id, developers, job)

        elif choice == '5':
            save_catalog()  # <-- fixed this line

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("[!] Invalid choice. Try again.")

# Run the menu
main_menu()
