import main

def testWorld():
    assert (main.get_cell(1000, 1000) == True or main.getCell(1000, 1000) == False)

    main.set_cell_alive(-1000, -1000)
    assert main.get_cell(-1000, -1000)

    main.set_cell_dead(-500, 500)
    assert main.get_cell(-500, 500) == False

    main.get_list_neighbors(-500,500)
    assert len(main.get_list_neighbors()) == 8

    main.get_list_neighbors(2, 2)
    assert main.get_list_neighbors() == [(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)]
