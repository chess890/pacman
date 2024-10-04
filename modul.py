# Datei: modul.py

def erstelleBitmaske(tilemap, row, col):
    if tilemap[row][col] == 1:
        if tilemap[row][col + 1] == 1:
            if tilemap[row][col - 1] == 1:
                if tilemap[row + 1][col] == 1:
                    if tilemap[row - 1][col] == 1:
                        bitmaske = 11111
                    else:
                        bitmaske = 11110
                else:
                    if tilemap[row - 1][col] == 1:
                        bitmaske = 11101
                    else:
                        bitmaske = 11100
            else:
                if tilemap[row + 1][col] == 1:
                    if tilemap[row - 1][col] == 1:
                        bitmaske = 11011
                    else:
                        bitmaske = 11010
                else:
                    if tilemap[row - 1][col] == 1:
                        bitmaske = 11001
                    else:
                        bitmaske = 11000
        else:
            if tilemap[row][col - 1] == 1:
                if tilemap[row + 1][col] == 1:
                    if tilemap[row - 1][col] == 1:
                        bitmaske = 10111
                    else:
                        bitmaske = 10110
                else:
                    if tilemap[row - 1][col] == 1:
                        bitmaske = 10101
                    else:
                        bitmaske = 10100
            else:
                if tilemap[row + 1][col] == 1:
                    if tilemap[row - 1][col] == 1:
                        bitmaske = 10011
                    else:
                        bitmaske = 10010
                else:
                    if tilemap[row - 1][col] == 1:
                        bitmaske = 10001
                    else:
                        bitmaske = 10000
    else:
        bitmaske = 0

    tile_type = bitmaske
    return tile_type
