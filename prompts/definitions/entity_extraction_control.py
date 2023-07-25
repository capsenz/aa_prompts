"""
Prompt to run entity extraction(English). Replace the text in the input and maybe the output format and play around!
"""

prompt = """### Instruction:
Extract all stars from the text. Use the json format:
{
    "stars": [...]
}

### Input:
At the center of our solar system lies the Sun, a dazzling G-type main-sequence star that provides light, heat, and energy to all the planets in its gravitational embrace. The Sun's radiant presence is the reason life flourishes on Earth and serves as a navigational guide for space missions venturing beyond our home planet. Around the Sun, there are several dwarf planets, asteroids, and comets that make up the vast expanse of our solar system. While these objects are not stars themselves, they interact with the Sun's gravity and illuminate our skies as they reflect sunlight. One of the most famous examples is Halley's Comet, which visits the inner solar system approximately every 76 years, creating a spectacular celestial display.

Beyond the boundaries of our solar system lies a myriad of stars, some of which are relatively close to us in cosmic terms. Among these, the three stellar systems that stand out are Alpha Centauri, Proxima Centauri, and Barnard's Star. Alpha Centauri is a triple-star system, with Alpha Centauri A and B forming a binary pair, and Proxima Centauri being the closest known neighboring star to the Sun. Proxima Centauri is a red dwarf, cooler and dimmer than the Sun, but its proximity has led scientists to speculate about the potential for exoplanets in its habitable zone. Barnard's Star, another red dwarf, ranks as the fourth-nearest known individual star to us. While these stars are too distant for human space missions with current technology, they serve as intriguing subjects for astronomers and exoplanet researchers seeking to unravel the mysteries of the universe beyond our solar system.

### Response: {"""

settings = {
    "maximum_tokens": 128
}

model = "luminous-supreme-control"