from Initialize_ColorPairs import Definition_ColorSets

obj_Definition_ColorSets = Definition_ColorSets()

def ReferenceManual():
    print('\n############### Reference Manual ################\n')
    pair_number = 1
    for major_Color in obj_Definition_ColorSets.MajorColors:
        for minor_Color in obj_Definition_ColorSets.MinorColors:
            print(f'Pair Number: {pair_number} --> {major_Color}, {minor_Color}')
            pair_number += 1


if __name__ == '__main__':
    ReferenceManual()
