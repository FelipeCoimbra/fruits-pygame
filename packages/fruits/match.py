

class Match:

    class MatchConf:
        def __init__(self):
            self.team_count = 0

    def __init__(self):
        self.__conf = None
        self.__teams = []

    def __set_conf(self, conf):
        self.__conf = conf.team_count
