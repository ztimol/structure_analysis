import os
import numpy as np


def is_whole_string_comment(s):
    """ function to check if a line
         starts with some character.
         Here # for comment
    """
    # return true if a line starts with #
    return s.lstrip().startswith("#")


def is_empty_string(string):
    if string.strip() in ["\n", "\r\n", ""]:
        return True
    return False


def clean_string(string):
    string = remove_string_comments(string)
    # return string.lstrip().rstrip().replace("\r", "").replace("\n", "")
    return string.strip()


def remove_string_comments(string):
    if string.find("#") != -1:
        return string[: string.find("#")]
    return string


def calc_exp_polynomial(x, a, b):
    return a * np.exp(b * x)


def calc_first_degree_polynomial(x, a, b):
    return a * x + b


def calc_second_degree_polynomial(x, a, b, c):
    return a * x ** 2 + b * x + c


def calc_third_order_polynomial(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


# Define a class that forces representation of float to look a certain way
# This remove trailing zero so '1.0' becomes '1'
class nf(float):
    def __repr__(self):
        str = "%.1f" % (self.__float__(),)
        if str[-1] == "0":
            return "%.0f" % self.__float__()
        else:
            return "%.1f" % self.__float__()


def confirm_critical_file_exists(file_path):

    if os.path.isfile(file_path):
        return True
    else:
        raise Exception("file missing: " + file_path)


def convert_frames_to_ns(num_frames, frames_per_ns):
    return num_frames / frames_per_ns


def get_output_dir_name_from_config_file_args(config_file_args):
    file_name = config_file_args.split("/")[-1]
    return file_name.split(".")[0]


def split_list_into_segments(list_to_split, number_of_segments):
    k, m = divmod(len(list_to_split), number_of_segments)
    return [
        list_to_split[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)]
        for i in range(number_of_segments)
    ]
