# supermetroid

Create a folder in the data/stable directory (if you try to run one of the sample files I have included, it should error out with the missing rom and you'll have the general path).

I create
SuperMetroid-Snes and that is the "game" in the files.

The .state files are the save states I've made.

data.json is the location of variables, however there are things to note here, score and lives seem to be required, so I just left it what it was (the addresses are from Super Mario World). I think that the HP is correct,and *assume* that room, missiles, supers, and pbs are right but havent confirmed.

Basically install python3, then pip3 install gym-retro.

If you want to play with NN's (specifically the ones here) you'll install torch.

Finally once you run it'll complain the game is missing, so you'll basically just copy/paste the Super Mario World folder, and rename it, and replace the relevant files with what I have in this repo. You'll need to go include your rom, I have to convert mine to sfc which there is an online one that works fine. Copy that into the folder and the game should start working.

If you want to start from Zebes you can set the default to zebes, or ceres or whatever, *or* you can specifically tell it which level. (this is noted in openai's docs, so I'd have to go look it up at some point).

Just confirmed that the offsets for the missiles are wrong, so, so far HP might be the only correct item.
