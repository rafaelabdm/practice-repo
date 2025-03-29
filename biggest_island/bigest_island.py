# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water),
# find the biggest island in it. Write a function to return the area of the biggest island.
# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water).
# Each cell is considered connected to other cells horizontally or vertically (not diagonally).


# SOLUTION:
def check_discovered_islands(position: tuple, islands: list[list]) -> bool:
    """
        Checks for slot in already discovered islands.
    """
    for island in islands:
        if position in island:
            return True
    return False


def check_next_slots(matrix: list[list], temp_island: set[tuple], current_row: int, current_slot: int, slots_per_row: int) -> None:
    """
        Checks if slots on the right of a land spot belongs to the current island,
        therefore linking the current slot to the island as well.
        If it does, add the current slot to temp_island (current island).
    """
    temp_slot = 0
    while temp_slot < slots_per_row:
        if temp_slot - current_slot <= 0:
            temp_slot += 1
            continue
        slot_up = None if current_row - 1 < 0 else current_row - 1
        if matrix[current_row][temp_slot] == 1:
            if (slot_up, temp_slot) in temp_island:
                temp_island.add((current_row, current_slot))
                break
            temp_slot += 1
        else:
            break


def get_biggest_island(islands: list[list]) -> int:
    bigest_island = 0
    for island in islands:
        if len(island) > bigest_island:
            bigest_island = len(island)
    return bigest_island


def search_islands(matrix: list[list]) -> list[list]:
    islands = list()
    temp_island = set()

    row = 0
    slot = 0
    end_search = False

    rows_count = len(matrix)
    slots_per_row = len(matrix[0])

    while row < rows_count and not end_search:
        while slot < slots_per_row:
            if not temp_island and matrix[row][slot] == 1 \
                and (row, slot) and not check_discovered_islands((row, slot), islands):
                temp_island.add((row, slot))
                slot += 1
                continue
            if matrix[row][slot] == 1:
                if check_discovered_islands((row, slot), islands) or (row, slot) in temp_island:
                    slot += 1
                    continue
                slot_up = None if row - 1 < 0 else row - 1
                slot_left =  None if slot - 1 < 0 else slot - 1
                if set([(row, slot_left), (slot_up, slot)]).intersection(temp_island):
                    temp_island.add((row, slot))
                else:
                    check_next_slots(matrix, temp_island, row, slot, slots_per_row)
                    slot += 1
            else:
                slot += 1
                continue

        if temp_island and row + 1 == rows_count:
            islands.append(temp_island.copy())
            temp_island.clear()
            row=0
            slot=0
        elif not temp_island and row == rows_count and slot == slots_per_row:
            end_search = True
        else:
            row += 1
            slot = 0 
    
    return islands


def main(selected_matrix: list[list]):
    islands = search_islands(selected_matrix)
    print(f"This matrix have {len(islands)} islands.")
    print(f"The biggest one has {get_biggest_island(islands)} slots of land!")


# There are more Example Matrices in the file examples.py, test it out!
from examples import *

main(matrix_1)
main(matrix_2)
main(matrix_3)
main(matrix_4)
main(matrix_5)
main(matrix_6)
