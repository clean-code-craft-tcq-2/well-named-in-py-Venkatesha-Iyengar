from Conversion_ColorPairs import *

def test_number_to_pair(pair_number, expected_major_color, expected_minor_color):
    major_color, minor_color = get_color_from_pair_number(pair_number)
    assert(major_color == expected_major_color)
    assert(minor_color == expected_minor_color)


def test_pair_to_number(major_color, minor_color, expected_pair_number):
    pair_number = get_pair_number_from_color(major_color, minor_color)
    assert(pair_number == expected_pair_number)

def test_Reference_Manual():
    #Since an object to initialize the color set is defined in Coversion_ColorPairs
    #We shall use the same object to assert the reference manual
    pair_number_counter=1
    for major_Color in obj_Definition_ColorSets.MajorColors:
        for minor_Color in obj_Definition_ColorSets.MinorColors:
            pair_number_received = get_pair_number_from_color(major_Color, minor_Color)
            assert(pair_number_received == pair_number_counter)
            pair_number_counter+=1
            
    
