import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for
                                                                                                             i in
                                                                                                             input().split()]

elevators = {}
for _ in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevators[elevator_floor] = elevator_pos

# game loop
while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    print(clone_floor, clone_pos, direction, clone_floor, clone_pos, file=sys.stderr)
    print(exit_floor, exit_pos, nb_elevators, width, file=sys.stderr)
    print(elevators, file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    if exit_floor == clone_floor:
        if clone_pos < exit_pos:
            if direction == 'LEFT':
                print('BLOCK')
            else:
                print('WAIT')
        elif exit_pos < clone_pos:
            if direction == 'RIGHT':
                print('BLOCK')
            else:
                print('WAIT')
        else:
            print('WAIT')
    else:
        if clone_pos < elevators.get(clone_floor, 0):
            if direction == 'LEFT':
                print('BLOCK')
            else:
                print('WAIT')
        elif clone_pos > elevators.get(clone_floor, width - 1):
            if direction == 'RIGHT':
                print('BLOCK')
            else:
                print('WAIT')
        else:
            print('WAIT')
