# GameFiles.threadManager.pyw
# This file manages all threads.

import sys
mod = module = sys.modules[__name__]  # i.e the "file" where your code is written
#setattr(current_module, 'variable_name', 15)  # 15 is the value you assign to the var
#print(variable_name)  # >>> 15, created from a string
import threading

CurrentThreads = []

def thisDoesSomething():
    print('hi')
    import time
    time.sleep(15)
    print('blerb')

def newThread(group=None, target=None, name=None, args=(), kwargs=None):
    global CurrentThreads
    if name is None:
        name = 'thread-' + str(len(CurrentThreads))
    CurrentThreads.append(name)
    if target is None:
        if args == () or kwargs is None or kwargs is {}:
            raise TypeError("Cannot add arguments to NoneType")
        else:
            print("Thread does nothing")
    else:
        try:
            #tName = name + 'T'
            setattr(mod, name + 'T', threading.Thread(group=group, target=target, name=name, args=args, kwargs=kwargs))
            aRandomThreadT.start()
        except Exception as err:
            print("Unable to create thread:")
            raise err
        finally:
            CurrentThreads.remove(name)
            
            
newThread(target=thisDoesSomething, name='aRandomThread')