import time

songly="""This night is cold in the kingdom
I can feel you fade away
From the kitchen to the bathroom sink and
Your steps keep me awake
Don't cut me down, throw me out, leave me here to waste
I once was a man with dignity and grace
Now I'm slippin' through the cracks of your cold embrace
So please, please
Could you find a way to let me down slowly?
A little sympathy, I hope you can show me
If you wanna go then I'll be so lonely
If you're leavin', baby, let me down slowly
Let me down, down, let me down, down, let me down
Let me down, down, let me down, down, let me down
If you wanna go then I'll be so lonely
If you're leavin', baby, let me down slowly"""

def lyoutput(str):
    for oneLine in str.splitlines():
        print(oneLine)
        time.sleep(1)

lyoutput(songly)
