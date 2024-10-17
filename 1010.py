p1 = input().split()
p2 = input().split()

peca1 = float(p1[1])
valorp1 = float(p1[2])
peca2 = float(p2[1])
valorp2 = float(p2[2])

def valor_pagar (peca1, valorp1, peca2, valorp2):
    pagar = (peca1 * valorp1) + (peca2 * valorp2)
    return pagar

pagar = valor_pagar(peca1, valorp1, peca2, valorp2)
print(f"VALOR A PAGAR: R$ {pagar:.2f}")