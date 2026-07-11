import random
import string

# 1. GENERATE COOL USERNAME
def generate_username():
    adjectives = ["Cool", "Epic", "Shadow", "Cyber", "Swift", "Neon", "Alpha", "Hyper"]
    nouns = ["Gamer", "Coder", "Hacker", "Ninja", "User", "Bot", "Ghost", "Knight", "Alpha", "Dragon" , "Phoenix", "Wizard", "Samurai", "Rogue", "Viper", "Titan", "Falcon", "Wolf", "Tiger", "Lion"]
    number = random.randint(100, 99999)
    return f"{random.choice(adjectives)}{random.choice(nouns)}{number}"

# 2. GENERATE SECURE PASSWORD
def generate_password(length=14):
    # Uses letters, digits, and safe special characters
    characters = string.ascii_letters + string.digits + "!?@#$"
    return ''.join(random.choice(characters) for _ in range(length))

# --- MAIN RUNNER ---
if __name__ == "__main__":
    print("\n====================================")
    print("===  OFFLINE CREDENTIAL GENERATOR ===")
    print("====================================\n")
    
    # Generate 3 options at once so the user has a choice
    print("🤖 Here are 3 randomly generated accounts for you:\n")
    
    for i in range(1, 4):
        uname = generate_username()
        pword = generate_password()
        print(f"[{i}] 👤 Username: {uname}")
        print(f"    🔑 Password: {pword}\n")
        
    print("====================================")
    print("👉 Copy any credentials and use them anywhere!")
    print("====================================")
    print("👉 Remember to keep your credentials safe and secure.")
    print("====================================")
    print("👉 This tool is for offline use only. No data is sent anywhere.")
    print("====================================")
    print("👉 If you like this tool, consider supporting the developer!\n")
    print("====================================")
    print("made with ❤️ by @Benni_main\n")
    print("====================================\n")
    print("We are Working on a New Gen With Email Generator and more features, Stay Tuned!\n")
    print("=== Offline Credential Generator ===")

