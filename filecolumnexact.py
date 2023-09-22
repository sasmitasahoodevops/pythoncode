with open("sample.log") as logfile:
    for line in logfile:
        # covers also 'installed', 'half-installed', …
        # for deeper processing you can use re module, but it's very likely not necessary
        if "install" in line.split()[3]:  # or [4]
            # your code here
            print(line)