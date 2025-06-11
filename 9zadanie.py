import re


def main(s):
    pattern = r'equ\s*[\'](\w+?)[\']\s*to\s*@[\"](\w+?)[\"]'
    matches = re.findall(pattern, s, re.DOTALL)

    result = {}
    for value, key in matches:
        result[key] = value

    return result

s = "do equ'isus'to @\"tiin_887\"od. do equ 'esce' to @\"vela_310\"od. do equ 'biqube_860' to @\"ledi_610\" od."
print(main(s))

import re


def main(s):
    pattern = r'option\s*\[\s*([\s\S]*?)\s*\]\s*=:?\s*[\'"](\w+)[\'"]'
    matches = re.findall(pattern, s, re.DOTALL)

    result = []
    for vars_str, key in matches:
        vars_list = [v.strip() for v in vars_str.split(';') if v.strip()]
        result.append((key, vars_list))

    return result

from itertools import product

def variant_15(L):
    # Z = {λ² | λ ∈ L, λ ≥ -40}
    Z = [l**2 for l in L if l >= -40]

    # P = {5λ | λ ∈ L, -56 < λ < 53}
    P = [5 * l for l in L if -56 < l < 53]

    # K = {floor(ζ / 5) + ζ | ζ ∈ Z, ζ < 96 or ζ > -23}
    K = [z // 5 + z for z in Z if z < 96 or z > -23]

    # First sum: ∑ 8ρ for ρ ∈ P
    sum1 = sum(8 * p for p in P)

    # Second sum: ∑ ρκ for all (ρ, κ) ∈ P × K
    sum2 = sum(p * k for p, k in product(P, K))

    return sum1 + sum2


def main(hex_string):
    value = int(hex_string, 16)

    b1 = value & 0b111111                          # 6 бит (0–5)
    b2 = (value >> 6) & 0b111                      # 3 бита (6–8)
    b3 = (value >> 9) & 0b111                      # 3 бита (9–11)
    b4 = (value >> 12) & 0b11                      # 2 бита (12–13)
    b5 = (value >> 14) & 0b11                      # 2 бита (14–15)
    b6 = (value >> 16) & 0b111111                  # 6 бит (16–21)

    return tuple(hex(b) for b in (b1, b2, b3, b4, b5, b6))