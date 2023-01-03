import function 
import view
import Phonebook_input



command = 0
exitflag = 0
while exitflag == 0:
    view.printmenu()
    try:
        command = int(input())
        if command == 1:
            Phonebook_input.input_data()
        elif command == 0:
            exitflag = 1
        elif command == 2:
            function.Convert_file()
            view.conv1()
            exitflag = 1 
        elif command == 3:
            function.search()
            exitflag = 1     
        else:
            view.printerror()
    except:
        view.printerror()
      