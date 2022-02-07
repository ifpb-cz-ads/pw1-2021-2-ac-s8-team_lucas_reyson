def validate(string, min, max):
    if len(string) <= max and len(string) >=min:
        return True
    else:
        return False

verifica = validate('constitucional', 1, 14)
print(verifica)