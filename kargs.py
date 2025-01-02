def famous_name(first,last,title, **addition):
    name = f'{title} {first} {last}'
    return name
name = famous_name(first = 'baby',last='adiba',title = 'cutie',addition='kuchu')
print(name)
