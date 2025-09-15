# Colour here:        G G        B G        R G        B R
# Becomes colour:      G          R          B          G

# RRGBRGBB

# récupérer les deux premières lettres
# stocker la valeur dans une variable finale
# faire une fonction qui retourne soit G / R ou B en fonction des combinaisons

def combinaisons(letter1: str, letter2: str):
    if (letter1 == letter2):
        return letter1
    elif(letter1 == "B" and letter2 == "G" or letter2 == "B" and letter1 == "G"):
        return "R"
    elif(letter1 =="R" and letter2 == "G" or letter2 == "R" and letter1 == "G"):
        return "B"
    elif(letter1 == "B" and letter2 == "R" or letter2 == "B" and letter1 == "R"):
        return "G"


# RRGBRGBB
def triangles(code: str):
    if(len(code) == 1):
        return code
    
    nextCode = ""
    for i in range(0, len(code) - 1):
        nextCode += combinaisons(code[i], code[i + 1])
    print(nextCode)
    return triangles(nextCode)

triangles("RRGBRGBB")
