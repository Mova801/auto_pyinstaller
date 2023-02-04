"""
Simple module which implement a Color class supporting RGB and HEX formats.
"""
import re
import textwrap

tuple3int = tuple[int, int, int]
_BLACK: tuple3int = (0, 0, 0)


class InvalidRGBColorError(ValueError):
    def __init__(self, *args) -> None:
        self.error = f"{args[0]} is not a valid rgb color." \
                     "You can either enter a hexadecimal number (i.e. '#FF00FF')" \
                     " or 3 integers between 0 and 255."
        super().__init__(self.error)


def _merge_list_elements(list_to_merge: list, index1: int, index2: int) -> list:
    """
    Merges index1 and index2 of a list.
    :param list_to_merge: list to merge
    :param index1: starting index to merge
    :param index2: ending index to merge
    :return: list with merged item

    # id          0   1   2   3   4   5
    # list      [ 9 , 3 , 4 , 7 , 3 , 5 ]
    # merge       0-><-1
    # merged    [ 93 , 4 , 7 , 3 , 5 ]
    # id_merged   0    1   2   3   4

    """
    list_copy = list_to_merge.copy()
    list_copy[index1:index2 + 1] = [''.join(list_copy[index1: index2 + 1])]
    return list_copy


class Color:
    """
    Represents a color.
    The value is stored as a hexadecimal string, but is possible to get the rgb value.
        - hex: returns the hex value (as str)
        - rgb: returns the rgb value (as tuple[int, int, int])
    """
    __min_rgb_value: int = 0
    __max_rgb_value: int = 255

    __rgb_colors_num: int = 3

    def __init__(self, *args) -> None:
        if len(args) == 1 and isinstance(args[0], str | int):
            # hex must be a str (but accept int also)
            self.__init_hex__(*args)
        elif len(args) == 3 and isinstance(args[0], int) and isinstance(args[1], int) and isinstance(args[2], int):
            self.__init_rgb__(*args)
        else:
            raise InvalidRGBColorError(args)

    def __init_hex__(self, hex_color: str) -> None:
        """Initializes the color from a hex value."""
        valid_hexadecimal_digits: str = "[0-9A-Fa-f]"
        valid_hex_color_digits: list[str] = re.findall(valid_hexadecimal_digits, str(hex_color))
        valid_color: str = ''.join(valid_hex_color_digits)[:6]
        self.__value = valid_color

    def __init_rgb__(self, red: int, green: int, blue: int) -> None:
        """Initializes the color from a rgb value."""
        # checks if the values are valid
        colors: tuple3int = red, green, blue
        valid_rgb_values: tuple3int = tuple(  # type: ignore
            color for i, color in enumerate(colors) if self.__min_rgb_value <= color <= self.__max_rgb_value
        )

        # sets a default value (if invalid values are found)
        if len(valid_rgb_values) < self.__rgb_colors_num:
            rgb_color = _BLACK
        else:
            rgb_color = valid_rgb_values

        # converts the rgb value to hex
        hex_value: list[str] = [f"{hex(color)[2:]:0>2}" for color in rgb_color]
        self.__value = ''.join(hex_value).upper()

    @property
    def rbg(self) -> tuple3int:
        """RGB color value."""
        # red, green, blue values in hexadecimal
        segmentation_len: int = max(1, len(self.__value) // 3)
        hex_rgb_values: list[str] = textwrap.TextWrapper(width=segmentation_len).wrap(text=self.__value)

        # if the length of the generated list is 4 or 5, merges the first 4 list values into 2 values
        # to get a 2/3 elements list.
        if len(hex_rgb_values) in [4, 5]:
            hex_rgb_values = _merge_list_elements(hex_rgb_values, 0, 1)
            hex_rgb_values = _merge_list_elements(hex_rgb_values, 1, 2)

        # if the length of the list if below 3 then 0s are added to the end of the list till length 3 is reached.
        missing_colors_num: int = self.__rgb_colors_num - len(hex_rgb_values)
        [hex_rgb_values.append("0") for _ in range(missing_colors_num)]

        return tuple(int(value, 16) for value in hex_rgb_values)  # type: ignore

    @property
    def hex(self) -> str:
        """HEXADECIMAL color value."""
        return "#" + self.__value
