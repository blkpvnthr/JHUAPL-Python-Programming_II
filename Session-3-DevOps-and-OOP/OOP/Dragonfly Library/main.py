""" Counting Mixed Data & Key-Value Pairs """


# -------------------------------------
# Dragonfly Mission - Instrument Library (Session 3)
# -------------------------------------

# Step 1: Create the empty dictionary
dragonflylibrary = {}

# Step 2: Function to add instruments
def add_instrument(library):
    name = input("Enter the instrument's name: ").strip()
    if name in library:
        print(f"Instrument '{name}' already exists in the library!")
    else:
        library[name] = {}  # Prepare nested dictionary
        print(f"Instrument '{name}' has been added to the library.")
    return library

# Step 3: Function to add acronym and IAID
def add_acronym(library):
    name = input("Enter the instrument's name: ").strip()
    if name in library:
        acronym = input("Enter the acronym for this instrument: ").strip().upper()
        iaid = input("Enter the instrument acronym ID (e.g., 01, 02, 03...): ").strip()
        library[name][acronym] = iaid
        print(f"Acronym '{acronym}' with IAID '{iaid}' has been added to '{name}'.")
    else:
        print(f"Instrument '{name}' not found in the library. Please add it first.")
    return library

# -------------------------------------
# NEW: Step 4 - Class to count total IAIDs
# -------------------------------------
class DragonflyLibraryCounter:
    def __init__(self, library):
        self.library = library

    def count_iaids(self):
        total = 0
        # Loop through all instruments and count IAIDs
        for instrument in self.library.values():
            total += len(instrument)  # Count acronyms for each instrument
        return total

# -------------------------------------
# Step 5: Main interaction loop
# -------------------------------------
while True:
    choice = input("\nWhat would you like to do? (1. add_instrument / 2. add_acronym / 3. count / 4. quit): ").strip().lower()
    
    if choice == "1":
        dragonflylibrary = add_instrument(dragonflylibrary)
    elif choice == "2":
        dragonflylibrary = add_acronym(dragonflylibrary)
    elif choice == "3":
        counter = DragonflyLibraryCounter(dragonflylibrary)
        print(f"🔢 Total IAIDs (Acronyms) entered: {counter.count_iaids()}")
    elif choice == "4":
        break
    else:
        print("⚠️ Invalid option, please try again.")

# -------------------------------------
# Step 6: Display final library
# -------------------------------------
print("\n📜 Final Dragonfly Instrument Library:")
for instrument, data in dragonflylibrary.items():
    print(f"- {instrument}: {data}")
