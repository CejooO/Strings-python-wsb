def check_string(string):
    not_met_req = []

    if not any (i.isupper() for i in string):
        not_met_req.append("String musi zawierac conajmniej jedna wielka litere")

    if not any (i.islower() for i in string):
        not_met_req.append("String musi zawierac conajmniej jedna mala litere")

    if not any (i.isdigit() for i in string):
        not_met_req.append("String musi zawierac conajmniej jedna cyfre")

    if len(string) < 5:
        not_met_req.append("String musi zawierac conajmniej 5 znakow")

    if not not_met_req:
        not_met_req.append(string)

    return not_met_req

string = input("Enter a string: ")
print(check_string(string))
