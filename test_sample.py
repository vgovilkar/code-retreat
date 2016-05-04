import main

def testWorld():
    assert (main.getCell(1000,1000) == True or main.getCell(1000,1000) == False)

    main.setCellAlive(-1000,-1000)
    assert main.getCell(-1000,-1000)

    main.killCell(-500,500)
    assert main.getCell(-500,500) == False



