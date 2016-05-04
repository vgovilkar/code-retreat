def get_cell(x,y):
    if (x,y) in knownCells:
        return knownCells[(x,y)]
    else:
        return False


def set_cell_alive(x,y):
    knownCells[(x,y)] = True


def set_cell_dead(x,y):
    knownCells[(x,y)] = False


knownCells = {}

