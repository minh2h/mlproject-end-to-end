requirements = []
with open(requirements.txt) as f:
    for line in f:
        requirements.append(line.strip())
        
print(requirements)