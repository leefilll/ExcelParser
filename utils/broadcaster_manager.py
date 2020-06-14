
class Broadcaster:
    def __init__(self, name):
        name = name.replace(" ", "").upper()
        self.name = name
        self.programs = []
        self.rating_prime = Rating("프라임")
        self.rating_daily = Rating("일일")

    def add_programs(self, time, program_name, ratings):
        program = Program(program_name)
        program.init_timeline(time)
        program.rating.set_ratings(ratings)
        program.broadcaster = self
        self.programs.append(program)

    def set_main_program(self, program_title):
        self.main_program = program_title

    # TODO: ratings about each broadcaster
    def set_ratings(self, ratings_prime, ratings_daily):
        self.rating_prime.set_ratings(ratings_prime)
        self.rating_daily.set_ratings(ratings_daily)

    def print_programs(self):
        print("방송사: {}".format(self.name))
        for program in self.programs:
            program.print_program()
        print("\n\n")


class Program:
    def __init__(self, name):
        self.name = name
        self.timeline = None
        self.broadcaster = None
        self.rating = Rating()

    def init_timeline(self, time_str):
        self.timeline = time_str

    def print_program(self):
        self.format = "시간대: {}, 프로그램: {}, 2549전국: {}, 2549수도권: {}, 가구전국: {}, 가구수도권: {}".format(self.timeline,
                                                                                               self.name,
                                                                                               self.rating.ratings_2549["전국"],
                                                                                               self.rating.ratings_2549["수도권"],
                                                                                               self.rating.ratings_house["전국"],
                                                                                               self.rating.ratings_house["수도권"])
        print(self.format)


class Rating:
    '''
    Note that if rating_type is None,
    it means broadcasters' ratings
    '''

    def __init__(self, rating_type=None):
        self.type = rating_type
        self.ratings_2549 = {}
        self.ratings_house = {}

    def set_ratings(self, ratings):
        self.ratings_2549["전국"] = float(ratings[0])
        self.ratings_2549["수도권"] = float(ratings[1])
        self.ratings_house["전국"] = float(ratings[2])
        self.ratings_house["수도권"] = float(ratings[3])

    def get_ratings_as_array(self):
        """ Order: 2549(capital -> nation) -> house(capital -> nation) """
        temp_arr = []
        temp_arr.append(self.ratings_2549["수도권"])
        temp_arr.append(self.ratings_2549["전국"])
        temp_arr.append(self.ratings_house["수도권"])
        temp_arr.append(self.ratings_house["전국"])
        return temp_arr

    def print_ratings(self):
        if self.type is not None:
            print(self.type, end=" ")
        print("2549전국: {}, 2549수도권: {}, 가구전국: {}, 가구수도권: {}".format(
            self.ratings_2549["전국"],
            self.ratings_2549["수도권"],
            self.ratings_house["전국"],
            self.ratings_house["수도권"]
        ))
