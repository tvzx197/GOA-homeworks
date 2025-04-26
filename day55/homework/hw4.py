def get_size(w, h, d):
    surface_area = 2 * (w * h + h * d + w * d)
    volume = w * h * d
    return [surface_area, volume]