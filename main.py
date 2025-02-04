import py5
import math
from player import player
from obstacle import pipe

bird = player()
pipe_list = []

time = 0
last_spawn_time = 0
score = 0
is_playing = False


def show_score():
    global score
    py5.fill(255)
    py5.text_size(20)
    py5.text("Score: " + str(score), 10, 20)


def update_pipe():
    global score, is_playing
    for i in pipe_list:
            i.move_obstacle(-4)
            i.show()
            if i.collision_check(bird):
                is_playing = False
            if i.check_if_passed(bird):
                score = score + 1


def show_level():
    py5.fill(56,77,72)
    py5.rect(-30, py5.height + 30, py5.width + 60, -60)
    py5.rect(-30, -30, py5.width + 60, 60)


def game_over():
    global time, last_spawn_time, pipe_list, is_playing, bird, score
    time = 0
    last_spawn_time = 0
    pipe_list = []
    bird.pos_y = py5.height/2

    py5.background(30, 30, 220)
    py5.fill(255)
    py5.text_size(81)
    py5.text("press Z to play", py5.width / 10.1, py5.height / 2)
    py5.text_size(20)
    py5.text("Score: " + str(score), py5.width / 10.1, py5.height / 4)

    if py5.is_key_pressed:
        if py5.key in ['z', 'Z']:
            score = 0
            is_playing = True


def spawn_pipe():
    global time, last_spawn_time, pipe_list    

    time = time + 1

    if time - last_spawn_time > py5.random(100, 200):
        new_pipe = pipe()
        last_spawn_time = time
        new_pipe.pos_y = math.sin(time/10) * 100 + py5.height/2
        pipe_list.append(new_pipe)


def border_collision_check(body):
    global is_playing
    if body.pos_y > py5.height - 30:
        is_playing = False
    if body.pos_y < 30:
        is_playing = False


def setup():
    py5.size(720, 480)

def draw():
    global bird, pipe_list, is_playing, score
    if is_playing == True:
        py5.background(10, 10, 25)

        bird.show()
        bird.move()
        bird.jump()
        border_collision_check(bird)

        spawn_pipe()
        update_pipe()
        
        show_level()
        show_score()


    elif is_playing == False:
        game_over() 

py5.run_sketch()  