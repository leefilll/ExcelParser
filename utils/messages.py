from utils.util import get_rank


def make_sentence(broadcasters, rating_list, program_list=None):
    bc_names = [bc.name for bc in broadcasters]
    pg_names = [pg for pg in program_list] if program_list else None

    first = "{}{} {}로 종편 {}위 ".format(
        bc_names[0],
        (" <" + pg_names[0] + ">") if program_list else "",
        rating_list[0],
        get_rank(rating_list)
    )
    second = "("

    if not program_list:
        for idx, bc in enumerate(bc_names):
            if idx == 0:
                continue
            second += (bc + " ")
            second += (str(rating_list[idx]))
            if idx == len(bc_names) - 1:
                second += ")"
                break
            second += ", "
    else:
        for idx, pg in enumerate(pg_names):
            if idx == 0:
                continue
            second += ("<" + pg + "> ")
            second += (str(rating_list[idx]))
            if idx == len(bc_names) - 1:
                second += ")"
                break
            second += ", "

    return first + second


def print_name(team, name, date):
    return "안녕하세요. {} {}입니다.".format(team, name) + '\n' + "{} 일일 시청률 보고 드립니다.".format(date)


def print_summary(broadcasters, matrix):
    return "- 2549타깃(수도권) : {}\n".format(make_sentence(broadcasters, matrix[0])) \
        + "- 2549타깃(전국) : {}\n".format(make_sentence(broadcasters, matrix[1])) \
        + "\n- 유료가구(수도권) : {}\n".format(make_sentence(broadcasters, matrix[2])) \
        + "- 유료가구(전국) : {}\n".format(make_sentence(broadcasters, matrix[3]))


def print_capital_summary(broadcasters, rating_list):
    return "{}%, 종편 {}위".format(rating_list[0], get_rank(rating_list))


def print_main_programs(broadcasters, matrix, program_list):
    return "- 2549타깃 : {}".format(make_sentence(broadcasters, matrix[0], program_list)) \
        + "\n- 유료가구 : {}".format(make_sentence(broadcasters,
                                               matrix[2], program_list))
