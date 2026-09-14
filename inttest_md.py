import md
import os
md.run_md()

if os.path.exists("cu.traj") and os.path.getsize("cu.traj") > 0:
    print("Integration test passed")
else:
    raise Exception("Integration test failed: cu.traj was not created or is empty")