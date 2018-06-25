def index_time(Xtime, ti, tf):
    """

    :param Xtime: Time np.array
    :param ti: Time init
    :param tf: Time end
    :return: index init, index end
    """
    start = Xtime[0]
    end = Xtime[-1]
    if ti < start or tf > end or ti >= tf:
        raise ValueError("ti: {} | tf: {} | start: {} | end: {}".format(ti, tf, start, end))
    steps = len(Xtime)
    total = end - start
    return int(ti*steps/total), int(tf*steps/total)






