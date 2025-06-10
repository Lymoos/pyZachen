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
