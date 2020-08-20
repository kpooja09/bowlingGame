'''
__author__: "Pooja Kamble"

Given a string of score for each frame the program calculated the total score for the player
'''


def get_score(scr_str):

    if not scr_str:
        return 0

    # get the frames and bonus frame
    scores = scr_str.split("||")
    bonus_frame = scores[1]
    frames = scores[0].split("|")

    # if len(frames) < 10:
    #     return 0
    
    # variables to keep track of previous first and second ball's score
    first, second = 0,0
    # get the bonus score
    if len(bonus_frame) > 0:
        first, second, flg = parse_score(bonus_frame)

    frame_score = []

    for i, f in enumerate(frames[::-1]):
        score = 0
        cur_first,cur_second, flg = parse_score(f)
        
        # score is sum of first ball and second ball
        cur_score = cur_first + cur_second

        if flg == 'strike':
            next_two = 0
            if second == 10 and first < 10:
                next_two = second
            else:
                next_two = first + second
            frame_score.append(cur_score+next_two)
        
        elif flg == 'spare':
            high = max(cur_first, cur_second)
            frame_score.append(high+first)
            first ,second = cur_first, high
            continue  
        else:
            frame_score.append(cur_score)

        if cur_second == 0:
            first, second = cur_first, first
        else:
            first, second = cur_first, cur_second

    total_Score = sum(x for x in frame_score)
    return total_Score


def parse_score(f):
    # print(f)
    flg = None

    first = 0
    second = 0
    ref =  { 'X' : {'scr':10, 'flg':'strike'}, 
            '/': {'scr':10, 'flg':'spare'},
            '-': {'scr':0, 'flg':None}} 
    
    if len(f) == 1:
        if f == 'X':
            first = ref[f]['scr']
            flg = ref[f]['flg']
        else:
            first = int(f)

    if len(f) == 2:
        b1 = f[0]
        b2 = f[1]

        if 48 <= ord(b1) <=57:
            first = int(b1)
        else:
            first = ref[b1]['scr']
            if flg == None:
                flg = ref[b1]['flg']

        if 48 <= ord(b2) <=57:
            second = int(b2)
        else:
            second = ref[b2]['scr']
            if flg == None:
                flg = ref[b2]['flg']

    return first, second, flg

        
        
if __name__ == '__main__':
    scr_str = ["X|X|X|X|X|X|X|X|X|X||XX","X|X|X|X|X|X|X|X|X||XX",
              "9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||",
              "5/|5/|5/|5/|5/|5/|5/|5/|5/|5/||5",
              "X|7/|9-|X|-8|8/|-6|X|X|X||81", "11|22|33|44|5/|6/|7/|8/|9/||X",
              ]
    scores = [300,90,150,167]
    score = 300


    for scr in scr_str:
        print(get_score(scr))


