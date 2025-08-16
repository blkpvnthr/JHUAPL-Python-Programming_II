### Dragonfly Library Review ###

"""
You are part of the Dragonfly mission's software team. 
Your job is to create a system to catalog the mission's scientific instruments. 
These instruments will be crucial in analyzing Titan’s environment and helping 
scientists answer big questions about habitability and life beyond Earth.


In Session 1, we entered the instrument’s name in the dragonflylibrary 
by defining the add_instrument definition. To better organize and track each 
instrument, your team now requires each entry to also include its acronym and a unique ID.
 Later, this will help scientists easily reference and process information about each 
instrument.

1. Add the function to add acronym and IAID.

2. Add the main interaction loop.

3. Combine the code from last session with this one."""

# -------------------------
# Dragonfly Instrument Library
# -------------------------

dragonflylibrary = {
    "Mass Spectrometer": {
        "acronym": "DraMS",
        "development": "Johns Hopkins APL",
        "job_at_titan": "Analyze surface material composition and organics."
    },
    "Drill for Acquisition of Complex Organics": {
        "acronym": "DrACO",
        "development": "Honeybee Robotics",
        "job_at_titan": "Rotary-percussive drill to sample and pneumatically transfer surface material to DraMS."
    },
    "Gamma-ray and Neutron Spectrometer": {
        "acronym": "DraGNS",
        "development": "Johns Hopkins APL, Lawrence Livermore National Laboratory",
        "job_at_titan": "Measure bulk elemental surface composition, including minor inorganics, to classify surface materials."
    },
    "Geophysics and Meteorology": {
        "acronym": "DraGMet",
        "development": "Johns Hopkins APL, Japan Aerospace Exploration Agency (JAXA)",
        "job_at_titan": "Monitor atmospheric conditions, constrain regolith properties, and detect and characterize the level of seismic activity."
    },
    "Camera Suite": {
        "acronym": "DragonCam",
        "development": "Malin Space Science Systems",
        "job_at_titan": "Characterize landforms and surface processes at multiple scales; surface and aerial imaging."
    }
}

# -------------------------
# Function to add a new instrument
# -------------------------
def add_instrument(library):
    name = input("Enter the instrument's name: ")
    acronym = input("Enter the instrument's acronym: ")
    development = input("Enter the developer/organization(s): ")
    job = input("Enter the instrument's job at Titan: ")

    library[name] = {
        "acronym": acronym,
        "development": development,
        "job_at_titan": job
    }
    print(f"\n✅ Instrument '{name}' (Acronym: {acronym}) has been added successfully!\n")
    return library

# -------------------------
# Function to display instruments
# -------------------------
def view_instruments(library):
    print("\nCurrent Dragonfly Instrument Library:")
    for instrument, details in library.items():
        print(f"""
🔹 Instrument: {instrument}
   Acronym: {details['acronym']}
   Development: {details['development']}
   Job at Titan: {details['job_at_titan']}
""")
    print("------------------------------------------------------------")

# -------------------------
# Main interaction loop
# -------------------------
def main():
    print("🚀 Welcome to the Dragonfly Mission Instrument Catalog System!\n")

    while True:
        print("Options:")
        print("1 - Add a new instrument")
        print("2 - View all instruments")
        print("3 - Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_instrument(dragonflylibrary)
        elif choice == "2":
            view_instruments(dragonflylibrary)
        elif choice == "3":
            print("🔚 Exiting the catalog system. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again.\n")

# -------------------------
# Run the program
# -------------------------
if __name__ == "__main__":
    main()
