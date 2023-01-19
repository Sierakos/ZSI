def symulation(temp, ogrz, klim):
    if ogrz > 0 and klim < 0:
        return temp + ogrz
    elif klim > 0 and ogrz < 0:
        return temp - klim
