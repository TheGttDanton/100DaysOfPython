from prettytable import PrettyTable

table = PrettyTable()

table.add_column(fieldname="Name", column=["Pokemon1", "Pokemon2", "Pokemon3", "Pokemon4", "Pokemon5"])
table.add_column(fieldname="Type", column=["Water", "Electric", "Land", "Fire", "Speed"])
table.align = "r"
print(table)
