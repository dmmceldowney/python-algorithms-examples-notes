# move all disks to the third peg from the first peg
# can only move one peg at a time
# larger disks must be on the bottom at all times
# base case: tower of height 1
def moveTower(height, from_pole, to_pole, inner_pole):
    if height >= 1:
        moveTower(height - 1, from_pole, inner_pole, to_pole)
        moveDisk(from_pole, to_pole)
        moveTower(height - 1, inner_pole, to_pole, from_pole)


def moveDisk(from_pole, to_pole):
    print(f"moving disk from {from_pole} to {to_pole}")


if __name__ == "__main__":
    moveTower(3, "A", "B", "C")
