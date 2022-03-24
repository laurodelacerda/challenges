def replace_substr(texto: str, inicial: str, final: str, i_inicial: int, i_final: int) :

    print(inicial, final, i_inicial, i_final)

    if i_inicial == 0:
        text = final + texto[i_final :]
    else:
        if i_final < len(texto) :
            text = texto[0 :i_inicial] + texto[i_inicial :i_final].replace(inicial, final) + texto[i_final :]
        else :
            text = texto[0 :i_inicial] + texto[i_inicial :i_final].replace(inicial, final)

    print(text)

    return text


def replace(texto: str, palavras_a_substituir: list) :
    for i in palavras_a_substituir :
        if i["before"] in texto:
            # texto = replace_substr(texto, i["before"], i["after"], i["start"], i["start"] + len(i["before"]))
            texto = texto.replace(i["before"], i["after"], 1)
    return texto