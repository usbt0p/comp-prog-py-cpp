morse = {
"A" : ".-"	,
"B" : "-...",
"C" : "-.-.",
"D" : "-.."	,	
"E" : "."	,	
"F" : "..-.",		
"G" : "--."	,	
"H" : "....",		
"I" : ".."	,	
"J" : ".---",		
"K" : "-.-"	,	
"L" : ".-..",		
"M" : "--"	,	
"N" : "-.",
"O" : "---",
"P" : ".--.",
"Q" : "--.-",
"R" : ".-.",
"S" : "...",
"T" : "-",
"U" : "..-",
"V" : "...-",
"W" : ".--",
"X" : "-..-",
"Y" : "-.--",
"Z" : "--..",
"!" : "-.-.--",		
"?" : "..--.."
}

def duration(morse):
    dur = 0
    for i in range(len(morse)):
        if morse[i] == "-":
            dur += 3
        else:
            dur += 1
        dur += 1
    dur -= 1 # quitar la ultima suma
    return dur


n_casos = int(input())
casos = [input() for _ in range(n_casos)]

for msg in casos:

    dur = 0
    for letra in msg:
        if letra != " ":
            dur += duration(morse[letra])
            dur += 3
        else:
            dur -= 3 
            # hack para eliminar la suma de la letra anterior (siempre habra una antes)
            dur += 5
    dur -= 3
    print(dur)


    