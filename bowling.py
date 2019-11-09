

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

def spare_score(next_ball):
    score = 10 + next_ball
    return score

def score_strike(frame_index, frames):
    pins = 10
    next_ball = frame_index + 1
    next_frame_score = frames[next_ball]
    if len(next_frame_score) == 1:
            pins = 20
            next_ball = frame_index + 2
            if len(frames[next_ball]) == 1:
                return 30
            else:
                total = pins + sum(next_frame_score)
                return total

def total_score(frames):
    game_score = 0
    frame_index = 0
    for frame in frames:
        while frame_index <= 9:
            if len(frame) == 1:
                total = score_strike(frame_index, frames)
                game_score = game_score + total
                frame_index +=1
            else:
                frame_score = sum(frame)
                if frame_score == 10:
                    next_frame = frame_index + 1
                    next_ball = frames[next_frame]
                    print("Next ball is ", next_ball[0])
                    total = spare_score(next_ball[0])
                    print(total, "Frame{}".format(frame))
                    game_score = game_score + total
                    print(game_score)
                    frame_index +=1
                else:
                    print(frame_score)
                    game_score = game_score + frame_score
                    print(game_score)
                    frame_index +=1
    
    return game_score
        
    

if __name__ == '__main__':
    frames = score_game()
    score = total_score(frames)
    print(score)

