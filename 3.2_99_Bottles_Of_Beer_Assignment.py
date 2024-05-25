# 3.2 Bottles Of Beer Song - Jon Tokarz - May 25, 2024

# First verses of the "99 Bottles Of Beer" song.

beer_count = int(99)

while beer_count >= 3:
    print(beer_count, "bottles of beer on the wall")
    print(beer_count, "bottles of beer.")
    print("Take one down, pass it around")
    beer_count -= 1     #Taking one bottle down to pass around
    print(beer_count, "bottles of beer on the wall!\n")

# Song for the stanza with 1 bottle of beer remaining.

while beer_count >= 2:
    print(beer_count, "bottles of beer on the wall")
    print(beer_count, "bottles of beer.")
    print("Take one down, pass it around")
    beer_count -= 1     #Taking one bottle down to pass around
    print(beer_count, "bottle of beer on the wall!\n")

# Song for the stanza with no bottles of beer remaining.

while beer_count >= 1:
    print(beer_count, "bottle of beer on the wall")
    print(beer_count, "bottle of beer.")
    print("Take it down, pass it around")
    beer_count -= 1     #Taking one bottle down to pass around
    print("No bottles of beer on the wall!\n")

    

