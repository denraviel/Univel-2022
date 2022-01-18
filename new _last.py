with open("database.csv","a") as our_log_file:
    name = "atha"
    tries = 6
    our_log_file.write(f"{name},{tries}")