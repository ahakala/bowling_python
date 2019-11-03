

def score_game():
    frame = 1
    score = []
    while frame <= 10:
        ball1 = int(input("Type score for ball 1\n"))
        ball2 = int(input("Type score for ball 2\n"))
        score.append([ball1,ball2])
        print("Frame {}".format(frame))
        print(score)
        frame +=1
    return score

def total_score(frames):
    game_score = 0
    frame_index = 0
    for frame in frames:
        while frame_index <= 9:
            if len(frame) == 1:
                strike = 10
                next_ball = frame_index + 1
                next_frame_score = frames[next_ball]
                if len(next_frame_score) == 1:
                    total = 30
                    game_score = game_score + total
                    frame_index +=1
                else:
                    total = strike + sum(next_frame_score)
                    game_score = game_score + total
                    frame_index +=1
            else:
                frame_score = sum(frame)
                game_score = game_score + frame_score
                frame_index +=1
    
    return game_score
        
    

if __name__ == '__main__':
    frames = score_game()
    score = total_score(frames)
    print(score)

