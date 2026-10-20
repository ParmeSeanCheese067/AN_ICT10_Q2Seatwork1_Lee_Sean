from pyscript import document


club_members = ["Luisito Balajadia", "Denis Villenueve", "Steven Spielberg", "Cheese Burger"]

def verify_candidate(event=None):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    full_name = f"{first_name} {last_name}".title().strip()

    is_member = full_name in club_members

    messages = {
        True: f"Welcome, {full_name}! Enjoy your stay at the movies.",
        False: f"Sorry {full_name}, your name is not on the list."
    }
    document.getElementById("result").innerText = messages[is_member]