"""Create a function that takes an array of strings and return the number of
smiley faces contained within it.
These are the components that make up a valid smiley:

A smiley has eyes. Eyes can be : or ;

A smiley has a nose but it doesn't have to. A nose can be - or ~

A smiley has a mouth which can be ) or D
"""

eyes = (":", ";")
nose = ("", "-", "~")
mouth = (")", "D")


def is_smiley(face):
    if len(face) == 2:
        # No nose
        return face[0] in eyes and face[1] in mouth

    # Nose
    return face[0] in eyes and face[1] in nose and face[2] in mouth


def count_smileys(arr):
    if not arr:
        return 0

    smileys = 0

    for face in arr:
        if is_smiley(face):
            smileys += 1

    return smileys


print(count_smileys([";]", ":[", ";*", ":$", ";-D"]))  # expected: 1
print(count_smileys([";D", ":-(", ":-)", ";~)"]))  # expected: 3
print(count_smileys([":)", ";(", ";}", ":-D"]))  # expected: 2
