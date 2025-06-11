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
