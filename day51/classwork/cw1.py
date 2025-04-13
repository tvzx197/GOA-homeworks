def printer_error(s):
    
    errors = sum(1 for char in s if char < 'a' or char > 'm')
    total_length = len(s)
    return f"{errors}/{total_length}"
print(printer_error("aaabbbbhaijjjm")) 
print(printer_error("aaaxbbbbyyhwawiwjjjwwm")) 