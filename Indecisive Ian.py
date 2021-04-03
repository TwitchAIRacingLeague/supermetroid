import retro
from datetime import datetime
import time
import random
import itertools
import time
import gzip


def get_all_pairwise_actions(possible_actions):
    groupings = []
    for each in itertools.permutations(possible_actions.keys(),2):
        groupings.append(possible_actions[each[0]] + possible_actions[each[1]])
    return groupings
def spin_run(possible_actions, direction, run_distance_before_spin):
    set_of_actions = []
    for i in range(run_distance_before_spin):
        set_of_actions.append(possible_actions[direction])
    set_of_actions.append(possible_actions["DOWN"])
    return set_of_actions
def spin_dash(possible_actions, direction, taps):
    set_of_actions = []
    set_of_actions.append(possible_actions[direction])
    for i in range(taps):
        set_of_actions.append(possible_actions["DOWN"])
        set_of_actions.append(possible_actions["DOWN"] + possible_actions["B"])
    return set_of_actions
def run(possible_actions, direction, run_distance):
    set_of_actions = []
    for i in range(run_distance):
        set_of_actions.append(possible_actions[direction])
    return set_of_actions

def jump(possible_actions, direction, jump_duration):
    set_of_actions = []

    set_of_actions.append(possible_actions["A"])
    set_of_actions.append(possible_actions["A"])
    for i in range(jump_duration):
        set_of_actions.append(possible_actions[direction])

    return set_of_actions

def actions_available(possible_actions):
    #https://info.sonicretro.org/index.php?title=File:Sonic2_MD_US_manual.pdf&page=7

    x = {"run_left_spin_X_frames" : spin_run(possible_actions, "LEFT", 100), # This could be a variable amount of running
         "run_left_spin_Y_frames" : spin_run(possible_actions, "LEFT", 200), # This could be a variable amount of running
         "run_right_spin_X_frames" : spin_run(possible_actions, "RIGHT", 100), # This could be a variable amount of running
         "run_right_spin_Y_frames" : spin_run(possible_actions, "RIGHT", 200), # This could be a variable amount of running
         "run_left_X_frames" : run(possible_actions, "LEFT", 100), # This could be a variable amount of running
         "run_left_Y_frames" : run(possible_actions, "LEFT", 200), # This could be a variable amount of running
         "run_right_X_frames" : run(possible_actions, "RIGHT", 100), # This could be a variable amount of running
         "run_right_Y_frames" : run(possible_actions, "RIGHT", 200), # This could be a variable amount of running
         "spindash_right_X_times" : spin_dash(possible_actions, "RIGHT", 5),
         "spindash_left_X_times" : spin_dash(possible_actions, "LEFT", 5),
         "jump_right_X_frames" : jump(possible_actions, "RIGHT", 5),
         "jump_left_X_frames" : jump(possible_actions, "LEFT", 5),
         "jump_up_X_frames" : jump(possible_actions, "RIGHT", 5),
         
     }
    return x['run_right_X_frames'] #list(x.keys())[random.randint(0,len(x.keys())-1)]]

def save_state_to_file(env, name="test.state"):
    
    content = env.em.get_state()
    with gzip.open(name, 'wb') as f:
        f.write(content)

def main():

    actions_by_value = {"B" : 2**11, "A" : 2**10, "START" : 2**8, "UP" : 2**7, "DOWN" : 2**6, "LEFT" : 2**5, "RIGHT" : 2**4, "C" : 2**3, "Y" : 2**2, "X" : 2**1, "Z" : 2**0} # "MODE" : 2**9
    # Experiment with making an example like actions_by_value with snes
    env = retro.make(game='SuperMetroid-Snes')
    obs = env.reset()

    while True:
        action = env.action_space.sample()
        obs, rew, done, info = env.step(action)
        env.render()
        
        time.sleep(1.0/60.0)
        
        if done:
            print ("DONE?")
            if info["lives"] != 0:
                print ("bdone", done)
                print (info)
                print (rew)
                #print ("WHAT???")
                #input()
                #level_index += 1
                #env = retro.make(game='SonicTheHedgehog2-Genesis', state=levels[level_index])
            obs = env.reset()
            continue
    env.close()


if __name__ == "__main__":
    main()

'''
/home/hotdog/.local/lib/python3.6/site-packages/retro/data/stable/SonicTheHedgehog2-Genesis/

contest.json
data.json
metadata.json
scenario.json
script.lua
xpos.json
'''