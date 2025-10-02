import random

# --- Clasificación simplificada ---
def classify_sequence(seq: str) -> str:
    """
    Simulación simple: clasifica la secuencia según contenido
    En el futuro lo conectaremos a un modelo real de ML.
    """
    seq = seq.upper()
    if "U" in seq:
        return "ARN (posible Virus)"
    elif seq.count("C") > seq.count("G"):
        return "Bacteria"
    elif len(seq) > 50:
        return "Humano"
    else:
        return "Planta"

# --- Mutaciones probables ---
def predict_mutations(seq: str):
    """
    Genera mutaciones simples de la secuencia dada.
    """
    seq = seq.upper()
    bases = ["A", "T", "C", "G"]
    mutations = []

    for _ in range(5):  # generar 5 mutaciones
        pos = random.randint(0, len(seq)-1)
        original = seq[pos]
        new_base = random.choice([b for b in bases if b != original])
        mutations.append(f"Pos {pos+1}: {original} → {new_base}")

    return mutations
