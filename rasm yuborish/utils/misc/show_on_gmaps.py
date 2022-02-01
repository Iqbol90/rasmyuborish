URL="https://www.google.com/maps?q={lat},{lon}"

def show(lat, lon):
    return URL.format(lat=lat, lon=lon)
