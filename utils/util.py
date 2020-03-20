
from numpy import array
from numpy import transpose
from numpy import empty_like
from numpy import arange

# TODO: Remove repeated codes

def sort_by_broadcasters(broadcasters, order=None):
    """ Sort the broadcasters by name """
    ordered_list = [None for _ in range(len(broadcasters))]

    if not order:
        # TVCHOSUN -> JTBC -> MBN -> CHANNEL A
        order = ["TVCHOSUN", "JTBC", "MBN", "채널A"]

    for idx, val in enumerate(order):
        for bc in broadcasters:
            if bc.name == val:
                ordered_list[idx] = bc

    # print([bc.name for bc in ordered_list])
    return ordered_list


def get_matrix_daily(broadcasters):
    """
    Get summary among broadcasters
    All matrices order: 2549 capital, 2549 nation, house capital, house nation
    """
    temp_daily = []
    for bc in broadcasters:
        temp_daily.append(bc.rating_daily.get_ratings_as_array())

    # matrix of ratings for broadcasters
    daily_matrix = array(temp_daily)
    # print(daily_matrix)
    return daily_matrix


def get_matrix_prime(broadcasters):
    """
    Get summary among broadcasters
    All matrices order: 2549 capital, 2549 nation, house capital, house nation
    """
    temp_primes = []
    for bc in broadcasters:
        temp_primes.append(bc.rating_prime.get_ratings_as_array())

    prime_matrix = array(temp_primes)
    return prime_matrix


def get_matrix_programs(broadcasters, pg_name_list):
    main_pgs = []
    for pg in pg_name_list:
        for bc in broadcasters:
            for pgs in bc.programs:
                if pgs.name == pg:
                    main_pgs.append(pgs)
                    break

    temp_pg_ratings = []
    for pg in main_pgs:
        temp_pg_ratings.append(pg.rating.get_ratings_as_array())

    pg_matrix = transpose_matrix(array(temp_pg_ratings))
    print(pg_matrix)
    return pg_matrix


def transpose_matrix(matrix):
    """
    Do transpose for printing and optimizing the matrix
    """
    return transpose(matrix)


def get_rank(ordered_ratings):
    """
    Return rank of bc[0] in the ratings(np.array)
    """
    temp = ordered_ratings.argsort()[::-1]
    ranks = empty_like(temp)
    ranks[temp] = arange(len(ordered_ratings))
    return ranks[0] + 1


