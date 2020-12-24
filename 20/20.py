import time
from collections import defaultdict, Counter
from copy import deepcopy
import numpy as np
from itertools import permutations
import numpy as np
# complex*i to rotate left/ccw, complex*-i to rotate right/cw
x = 0+0j
direction = 1+0j
# if command == 'L':
#     direction *= 1j**(move // 90)
# if command == 'R':
#     direction /= 1j**(move // 90)


content = open("input.txt").read()


def part1(input):
    jigsaw_pieces_raw = input.split("\n\n")
    
    border_fingerprints = defaultdict(set)
    
    neighbors = defaultdict(set)
    for id_and_piece_raw in jigsaw_pieces_raw:
        id_raw, piece_raw = id_and_piece_raw.split(":\n")
        id = int(id_raw[4:])
        piece = piece_raw.split("\n")
        
        fp_top = piece[0]
        fp_top_r = piece[0][::-1]
        fp_bot = piece[-1]
        fp_bot_r = piece[-1][::-1]
        
        fp_l = "".join([line[0] for line in piece])
        fp_l_r = fp_l[::-1]
        fp_r = "".join([line[-1] for line in piece])
        fp_r_r = fp_r[::-1]
        
        fps = set([fp_top, fp_top_r, fp_bot, fp_bot_r, fp_l, fp_l_r, fp_r, fp_r_r])
        for fp in fps:
            FRIENDS = border_fingerprints[fp]
            for other_id in FRIENDS:
                if id != other_id:
                    neighbors[id].add(other_id)
                    neighbors[other_id].add(id)
            FRIENDS.add(id)
        
    #print(border_fingerprints)
    #print(neighbors)
    ids = ([id for id in neighbors if len(neighbors[id]) == 2])
    print(ids)
    
    return np.prod(ids)

def build_image(cur_img_id, neighbors, puzzle_pieces, total_img):
    cur_img = puzzle_pieces[cur_img_id]
    for neigbor in neighbors[cur_img_id]
    
def part2(input):
    jigsaw_pieces_raw = input.split("\n\n")

    border_fingerprints = defaultdict(set)

    neighbors = defaultdict(set)
    puzzle_pieces = dict()
    for id_and_piece_raw in jigsaw_pieces_raw:
        id_raw, piece_raw = id_and_piece_raw.split(":\n")
        id = int(id_raw[4:])
        piece = piece_raw.split("\n")
        puzzle_pieces[id] = piece
        fp_top = piece[0]
        fp_top_r = piece[0][::-1]
        fp_bot = piece[-1]
        fp_bot_r = piece[-1][::-1]

        fp_l = "".join([line[0] for line in piece])
        fp_l_r = fp_l[::-1]
        fp_r = "".join([line[-1] for line in piece])
        fp_r_r = fp_r[::-1]

        fps = set([fp_top, fp_top_r, fp_bot, fp_bot_r, fp_l, fp_l_r, fp_r, fp_r_r])
        for fp,  in fps:
            FRIENDS = border_fingerprints[fp]
            for other_id in FRIENDS:
                if id != other_id:
                    neighbors[id].add(other_id)
                    neighbors[other_id].add(id)
            FRIENDS.add(id)
    ids = ([id for id in neighbors if len(neighbors[id]) == 2])
    print(ids)
    snek="""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
    
    
    
print(part1(content))
print(part2(content))