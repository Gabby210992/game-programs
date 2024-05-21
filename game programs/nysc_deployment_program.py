import random
states = ["Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti",
            "Enugu", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Oyo", "Taraba", "yobe", 
            "Zamfara", "FCT"]
deployed_state = random.choice(states)
print(f"your allocated state is {deployed_state}. you are expected to report to camp in three days.")
