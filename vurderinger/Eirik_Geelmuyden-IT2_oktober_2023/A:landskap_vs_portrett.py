def format(b:int, h:int) -> str:
    if b > h:
        return "Landscape"
    elif b < h:
        return "Portrait"
    elif b==h:
        return "Square"

print(format(200,300))