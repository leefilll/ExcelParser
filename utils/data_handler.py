from pandas import read_excel
from pandas import isna
from numpy import nan
from utils.broadcaster_manager import Broadcaster
from utils.util import *


class DataHandler:
    def __init__(self, file_name):

        # TODO: Error handling
        self.data = read_excel(file_name, sheet_name=0, header=None)
        self.broadcasters = []
        self.find_separator()
        self.date_str = self.set_date()[6:]
        print(self.date_str)

        matrices = self.cut_by_broadcaster()
        for matrix in matrices:
            self.init_broadcasters(matrix)

        # Sorting according to the name of broadcasters
        self.broadcasters = sort_by_broadcasters(self.broadcasters)
        self.d_matrix = transpose_matrix(get_matrix_daily(self.broadcasters))
        self.p_matrix = transpose_matrix(get_matrix_prime(self.broadcasters))
    #
    # def read_file(self, file_name):
    #     self.data = read_excel(file_name, sheet_name=0, header=None)

    def set_date(self):
        """ Find today's date """
        return self.data.loc[1][self.middle_col].replace("  ", " ")
        # print(self.date_str)

    def find_separator(self):
        """ Find separate empty space in columns and rows """
        for (idx, val) in enumerate(self.data.loc[0]):
            if not isna(val):
                self.middle_col = idx
        # print(self.data.loc[0][self.title_idx])

        for (idx, val) in enumerate(self.data[0]):

            if "일일평균" in str(val):
                self.middle_row = idx + 1
                break
        # print(self.data[0][self.middle_row])

    def cut_by_broadcaster(self):
        """ Slice the raw excel data to matrices by broadcasters """
        mid_row = self.middle_row
        mid_col = self.middle_col
        matrices = []
        # table in upper left
        matrices.append(self.data.loc[3:mid_row - 1, 0:mid_col - 1].values)
        # table in upper right
        matrices.append(self.data.loc[3:mid_row - 1, mid_col + 1:].values)
        # table in lower left
        matrices.append(self.data.loc[mid_row + 1:, :mid_col - 1].values)
        # table in lower right
        matrices.append(self.data.loc[mid_row + 1:, mid_col + 1:].values)
        return matrices

    def init_broadcasters(self, matrix):
        """ Make object of Broadcaster and append """
        broadcaster_name = matrix[0][1]
        broadcaster = Broadcaster(broadcaster_name)
        programs_matrix = matrix[2:-4, :]   # matrix about programs
        # matrix about ratings for broadcaster
        ratings_matrix = matrix[-4:, :]

        for program_info in programs_matrix:
            # make object of Program and push to broadcaster's program array
            if program_info[0] is nan:
                continue
            broadcaster.add_programs(
                program_info[0], program_info[1], program_info[2:])

        # Set broadcaster's total ratings
        prime_ratings = ratings_matrix[2][-4:]
        daily_ratings = ratings_matrix[3][-4:]
        broadcaster.set_ratings(prime_ratings, daily_ratings)
        # print(broadcaster.rating_prime.get_ratings_as_array())

        self.broadcasters.append(broadcaster)
