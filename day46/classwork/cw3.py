def cat_mouse(x):
    cat_index = x.index('C')
    mouse_index = x.index('m')
    distance = mouse_index - cat_index - 1 
    if distance <= 3:
        return "Caught!"
    else:
        return "Escaped!"