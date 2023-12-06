personas={
    "sergio":5,
    "roberto":13,
    "julio":47,
    "martina":27,
    "andrea":19,
    "andres":17
}

mayores= [nombre for nombre, edad in personas.items() if edad > 18 ]

print(mayores)