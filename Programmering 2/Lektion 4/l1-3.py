def bokstavsByte(mening):
    v = ""
    for bokstav in mening:
        if bokstav == "Ö":
            v = v + "O"
        elif bokstav == "ö":
            v = v + "o"
        else:
            v = v + bokstav
    return v

print(bokstavsByte("Den sköna ön över övre Östermalms-ön"))
