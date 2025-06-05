######### Virtual Environment in python ###########
'''An environment which is same as the system  interpreter but,
         is isolated from the other python environment on the system. '''

''' So, as we install any version of any module ex: (pip install pandas==1.5.3) for some use case ,it installs it,but
the version of pandas 2.2.2 is already intalled on system was deleted automatically, VScode shows notifition that conflict b/w version 
want to create the virtual environment(venv) to isloate you dependencies    '''
# venv.py file 

''' is the (virtual-env) file that has all packages, which has no realtion fom the global interpreter, means 
makes the copy of python installation and with in that copy we install dif-diff versions of packages of modules, 
we can make an isolated environment '''
# python -m virtualenv env ->       this command adds the virtual enverionment in 
# .\env\Scripts\Activate.ps1 ->     this command will activate the virtual environment 

'''if this shows error like  ->      cannot be loaded because running scripts is disabled on this system,  means PowerShell is blocking script execution due to the Execution Policy.
                                   then open PS as admin and  run the command ,
        "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned" 
        What this does:
        RemoteSigned: Allows local scripts (like Activate.ps1) to run, but blocks unsigned scripts from the internet.
        Safe for development and the recommended option.

'''


