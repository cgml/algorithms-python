class Profiler:
    call_counter = 0

    @staticmethod
    def reset():
        Profiler.call_counter = 0

    @staticmethod
    def increment():
        Profiler.call_counter += 1

    @staticmethod
    def popcounter():
        c = Profiler.call_counter
        Profiler.reset()
        return c