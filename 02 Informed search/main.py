from puzzle import Puzzle
import ida_star
import math

def read_input():
    k = input()
    if not k.isdigit():
        raise ValueError('k must be digit')
    k = int(k)
    if not math.sqrt(k + 1).is_integer():
        raise ValueError('K + 1  must be perfect square.')
    
    l = input()
    l = int(l)
    if l > k or l < -1: 
        raise ValueError('l must be less than or equal to k and greater than -2')
    if l == -1:
        l = k
        
    matrix = []
    for _ in range(int(math.sqrt(k + 1))):
        m = input()
        m = m.split(' ')
        if len(m) != k + 1:
            ValueError('Row length is incorrect')
        m = [int(x) for x in m]
        matrix.append(m)
        
    k = int(math.sqrt(k + 1))
    return k, l, matrix

def translate_transitions(transitions):
    res = []
    for t in transitions:
        if t == (-1, 0):
            res.append('up')
        elif t == (1, 0):
            res.append('down')
        elif t == (0, -1):
            res.append('right')
        elif t == (0, 1):
            res.append('left')
    return res

def main() -> None:
    k, l, m = read_input()
    p = Puzzle(k, l, m)
    path, transitions = ida_star.start_ida_star(p)
    print(translate_transitions(transitions))
    print(len(transitions))
    
if __name__ == '__main__':
    main()

# 8
# -1
# 8 7 6
# 5 4 3
# 2 1 0