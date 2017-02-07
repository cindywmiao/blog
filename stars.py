from skyfield.api import load

planets = load('de421.bsp')

# for i in planets:
#     print(i)

solar_system_barycenter = {
    'MERCURY BARYCENTER'
    , 'VENUS BARYCENTER'
    , 'EARTH BARYCENTER'
    , 'MARS BARYCENTER'
    , 'JUPITER BARYCENTER'
    , 'SATURN BARYCENTER'
    , 'URANUS BARYCENTER'
    , 'NEPTUNE BARYCENTER'
    , 'PLUTO BARYCENTER'
    , 'SUN'}

ts = load.timescale()
t = ts.now()
earth = planets['earth']
for i in solar_system_barycenter:
    if i is not 'earth':
        planet = planets[i]
        position = earth.at(t).observe(planet)
        ra, dec, distance = position.radec()

        print(ra)
        print(dec)
        print(distance)

def display_solar_system():


