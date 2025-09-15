def seventate(code):
    # vérifier si le nombre précédent est un 7 et idem pour celui d'après
    result = []
    for i in range(0, len(code) - 1):
        if(code[i] != 0):
            if(code[i - 1] and code[i + 1] == "7"):
                continue
            result.append(code[i])
    print("".join(result))
            
seventate("79712312")