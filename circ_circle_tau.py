#!/usr/bin/env python3
# Created By: Frederic
# Date: Feb 18 2008
# Calculate circumference of circle
def main():
    from constants import TAU
    radius = int(input("enter a variable :"))
    # calculate circumference
    circumference = TAU * radius
    print(
        "the circumference of a circle of radius {} is {}".format(radius, circumference)
    )


if __name__ == "__main__":

    main()
