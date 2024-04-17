data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = []
codes = []

for item in data:
    if item.isdigit():
       codes.append(item)
    else:
        designations.append(item)

operators = dict(zip(designations, codes))

not_funtional = ['Katel', 'Fonex']

for operator in not_funtional:
    if operator in operators:
        del operators[operator]

addictional_codes = {
    "O!": {"0700", "0500", "705"},
    "Megacom": {"0999", "0555", "0550"},
    "Beeline": {"0222", "0777", "0770"}
}

for operator, codes in addictional_codes.items():
    if operator in operators:
        operators[operator] = codes

for key, value in operators.items():
    print(f'{key} - {value}')

