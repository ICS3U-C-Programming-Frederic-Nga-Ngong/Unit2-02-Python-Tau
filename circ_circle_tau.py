#!/usr/bin/env python3
# Created By: Frederic
# Date: Feb 18 2008
# Calculate circumference of circle
def main():
    # assign a value to tau
    tau = 6.28
    radius = int(input("enter a variable :"))
    # calculate circumference
    circumference = tau * radius
    print(
        "the circumference of a circle of radius {} is {}".format(radius, circumference)
    )


if __name__ == "__main__":

    main()
