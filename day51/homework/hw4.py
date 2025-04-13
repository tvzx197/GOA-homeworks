def nb_year(p0, percent, aug, p):
    years = 0
    current_population = p0
    percent_decimal = percent / 100
    
    while current_population < p:
        current_population += int(current_population * percent_decimal) + aug
        years += 1
    
    return years