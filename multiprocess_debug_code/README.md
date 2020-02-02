### Description

This is an example to use the multiprocess debug feature
of vscode.

### Instructions


* First of all, you can open the code workspace file contained in the directory in order to
put yourself in the right environment.

* Open an integrated terminal into the active workspace by going to
View>Command Palette> then type "Terminal: Create New Integrated Terminal (In Active Workspace)"
and run the main.py file with command: 
```console
$ python main.py
```
This will spawn a new process executing the execute.process_identifier() function.

This function contains a breakpoint.

Thus, upon giving the command, the execution will stop at the predefined breakpoint
with the message "Waiting for debugger attach".

* Make sure you have a proper debug configuration for the project.
it should look like this:

```json
    {
        "name": "Python: Attach",
        "type": "python",
        "request": "attach",
        "port" : 5678
    }
```
5678 is the port at which the debugger should attach.
After starting the main.py, go in the debug section of vscode, then in the upper dropdown list
select the configuration "Python: Attach" you just set up.
3) Click play: the debugger should detect the waiting process, and you will see the breakpoint set.
Note that any print output which is after the breakpoint will be shown in terminal window.
