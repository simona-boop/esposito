s=str(input("Inserisci una stringa: "))
ripetizioni=0
for i in range(0, len(s)):
    r=l
    x=s[i]
    for j in range(i+l, len(s)):
        if s[i] == s[j]:
           r = r + l
    if r > ripetizioni:
        carattere = x
        ripetizioni = r
print(carattere)
print(ripetizioni)
