                    for i in range(-1, 2):
                        for p in range(-1, 2):
                            if i == p and i == 0:
                                pass
                            else:
                                if 0 <= this_pos.x + i <= 7 and 0 <= this_pos.y + p <= 7:
                                    save.append([this_pos.x + i, this_pos.y + p])

                    for i in range(-2, 3):
                        if i == 0:
                            pass
                        else:
                            for p in range(-2, 3):
                                if p == 0 or abs(p) == abs(i):
                                    pass
                                else:
                                    if 0 <= this_pos.x + i <= 7 and 0 <= this_pos.y + p <= 7:
                                        save.append([this_pos.x + i, this_pos.y + p])