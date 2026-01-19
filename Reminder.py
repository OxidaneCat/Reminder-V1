#list to store data, not the list that will be print in th end
event_list = []

#colors
red_color = "\033[1;31m"
reset_color = "\033[0m"
green_color = "\033[0;32m"
#clear screen
import os
def clear_screen():
    #clear screen
    if os.name == 'nt': # For Windows
        os.system('cls')
    else: # For macOS and Linux
        os.system('clear')
    return
#Date Module
#https://www.w3schools.com/python/python_datetime.asp
import datetime

#3 : view current date 
#BONUS number 2 !!!!!
#allow the user to see time right now
#go check on the Select()
def date():
    date_now = datetime.datetime.now()
    print(date_now)
    return

#the final list that will be print
fixed_list = []
#update the list
def update_fixed_list():
    fixed_list.clear()
    today = datetime.date.today()
    for item in event_list:
        event_date_length = item[:10] #The first 10 letters of an item (Year-Month-day)
        #take them apart and compare it in to date now
        #replace "-" with nothing and skip if the date is somehow not digit
        if not event_date_length.replace("-", "").isdigit(): 
            continue
        year = int(event_date_length[0:4])
        month = int(event_date_length[5:7])
        day = int(event_date_length[8:10])
        event_date = datetime.date(year, month, day)
        #compare and remove events in the past
        if event_date >= today:
            fixed_list.append(item)
    #BONUS number 1!!!!!!!
    #Automatically sort the reminders by date
    fixed_list.sort()
    return

#2 : Add an new event
def add_event():
    clear_screen()
    print("Add an new event!")
    global set_Day,set_Year,set_event,set_Month,new_event
    #checks if the input is a number or not
    #https://www.w3schools.com/python/ref_string_isdigit.asp
    #year
    choice = input("Enter the Year in numbers: ")
    if not choice.isdigit():
        choice = "0"
    set_Year = int(choice)
    #month
    choice = input("Enter the Month in numbers: ")
    if not choice.isdigit():
        choice = "0"
    set_Month = int(choice)
    #date
    choice = input("Enter the date in numbers: ")
    if not choice.isdigit():
        choice = "0"
    set_Day = int(choice)
    #check if it is a real date
    #reference from
    #https://www.w3schools.com/python/python_try_except.asp
    #https://www.w3schools.com/python/python_datetime.asp
    try:
        datetime.date(set_Year, set_Month, set_Day) #check if the date is real
    except ValueError:
        print(red_color+"This date does not exist."+reset_color)
        Select()
        return
    #input an event
    new_event = input("Enter the event: ")
    
    #hyphen = "-"
    #punctuation_mark = ":"
    print(green_color+"added "+reset_color)
    #the length have to be 10 digits long for the dates so that update_fixed_list() can work
    set_event = f"{set_Year:04d}-{set_Month:02d}-{set_Day:02d}:{new_event}"
    event_list.append(set_event)
    update_fixed_list() #add it to the fixed list
    Select()
    return

#4 : Remove an event
def delete_event():
    if len(fixed_list) >= 1:
        for item in fixed_list:
            print(item)
        print("Remove options\n" \
        "        1 : Remove a specified event\n" \
        "        2 : Remove EVERYTHING\n")
        choice = input("Select an option: ")
        if not choice.isdigit():
            choice = "0"
        remove_option = int(choice)
        #option 1 (delete an event)
        if remove_option == 1:
            event_for_delete = input("Enter the event's date and name in the same format to delete the event: \n")
            #found the item and delete it
            if event_for_delete in fixed_list:
                fixed_list.remove(event_for_delete)
                event_list.remove(event_for_delete)
                update_fixed_list()
                clear_screen()
                print(green_color+"deleted"+reset_color)
                #print the list again
                if len(fixed_list) >= 1:
                    for item in fixed_list:
                        print(item)
                    Select()
                #no item in the list after the last item was deleted
                else:
                    print("no more events in the list")
                    Select()
            #could not find the item
            else:
                clear_screen()
                print(red_color+"Event not found."+reset_color)
                for item in fixed_list:
                    print(item)
                Select()

        #option 2 (delete all events)
        elif remove_option == 2:
            #comfirm
            print(red_color+"DELETE EVERYTHING")
            print("Enter 1 to confirm"+reset_color)
            choice = input("Enter here: ")
            if not choice.isdigit():
                choice = "0"
            confirem_delete = int(choice)
            if confirem_delete == 1:
                fixed_list.clear()
                event_list.clear()
                print(green_color+"ALL EVENTS DELETED, YEAHHHH!!!"+reset_color)
                print(r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠴⠶⠶⠒⠒⠒⠒⠒⠶⠶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢶⣄⠀⣠⠴⠚⠛⠳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠛⠉⠛⣶⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⣄⠀⠀⠀⠀⠀⠀⠈⠻⡅⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠁⠈⣹⠞⠁⠀⢀⣴⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀⠈⢶⣄⠀⠀⠀⠀⢷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠀⢀⠞⠁⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⣦⠀⠀⡀⠀⠀⠀⠀⠀⠀⡙⢄⠀⠀⠀⠀⠀⢢⢫⠳⡀⠀⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⢠⠏⠀⠀⠀⣴⠋⠀⠀⢀⠆⠀⠀⠀⣼⠋⠳⡄⠙⣦⡀⠀⠀⠀⠀⠈⠈⢣⠀⠀⠀⠀⠀⠀⢧⡱⡀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡾⠀⢀⠏⠀⠀⠀⢠⠇⠀⠀⢀⡞⠀⡴⢁⣼⠏⠀⠀⠈⠲⣌⠻⣦⣄⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠘⣷⢡⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠇⠀⡜⠀⠀⠀⠀⡼⠀⠀⣠⡟⣠⠎⣠⠞⠁⠀⠀⠀⠀⠀⠀⣙⡪⢵⡷⣤⣀⠀⠀⢘⡄⠀⠀⠀⠀⠀⠇⢇⡆⠀⠀⢹⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⠀⢀⠃⠀⠀⠀⠀⡇⢀⢴⣯⣞⠷⠛⢳⡄⠀⠀⠀⠀⠀⠀⠘⠤⠤⠤⠚⠋⠛⠻⠴⢆⡇⠀⠀⠀⠀⠀⢸⢸⢰⠀⠀⢸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⢸⠀⠀⠀⠀⠀⣯⠵⠛⠉⠉⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⢀⡇⠀⢠⢸⣿⠸⠀⠀⠸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡇⠀⢸⠀⡀⠀⡆⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⡀⠀⠸⡇⠀⢸⡸⠯⠐⠒⠒⠒⠓⠒⠒⠒⠲⡄
⠀⢀⣀⣀⣤⣤⡇⠠⢼⠀⡇⠀⣷⠀⢹⠀⢀⣤⣤⣤⣴⣶⣦⠀⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠟⠛⠛⠃⠀⡇⢀⠇⠇⠀⡇⡧⠔⢖⢩⠉⠉⠓⠤⠋⣠⠞⠁
⠐⣯⡉⢠⡔⣒⣢⠤⡬⡆⣿⠀⢣⢇⠘⡄⠈⠋⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⡠⠀⢠⢃⠎⡸⠀⡸⣿⠀⠀⣸⡜⠀⠀⣀⡴⠛⠁⠀⠀
⠀⠀⠙⠲⣌⡀⠀⠱⣣⢣⡏⢧⠈⡎⣆⢣⠰⠡⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡮⠋⢸⠁⣰⣻⣛⡠⠤⠛⣀⠤⠚⣿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⡗⢤⣉⠫⠧⠼⢧⠘⣟⡿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⣸⡔⢱⡎⣳⡠⠔⠊⠁⠀⠀⢿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠈⢹⠒⠴⣅⣱⣽⣧⠀⠀⠀⠀⠀⠀⠀⠀⠦⠤⠔⠤⠤⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣶⠒⢉⠁⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠀⠀⠀⢸⠀⢠⢄⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠁⣿⠀⡇⡇⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⡞⣾⠀⠀⠀⢸⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣟⠁⠀⠀⣿⠀⣟⡇⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⡿⢀⡆⠀⠀⠀⠀⡏⢹⠀⠀⠀⢸⠇⠈⣻⢶⠦⢄⣀⣀⠀⠀⠀⠀⠀⣀⣠⣤⡶⠿⠒⢋⣿⠀⠀⠀⣿⠀⡏⡇⠀⠀⠀⠀⢠⡆⠸⡇⠀⠀⠀⠀
⠀⠀⠀⣸⠇⣼⠀⠀⠀⠀⠀⠸⠜⠀⠀⠀⣿⣀⣀⣻⡤⡽⢛⡉⠛⠛⠛⠛⠉⣉⣉⣉⠤⠤⠒⠊⡡⣿⡴⠶⢚⠛⠢⡕⠁⠀⠀⢠⠀⢸⢡⠀⣿⠀⠀⠀⠀
⠀⠀⠀⣿⢰⣿⠀⠀⢀⢀⠀⠀⠀⠀⠀⢠⡿⠋⢉⡙⡧⡇⢸⣴⢶⣯⡉⠉⠀⠀⠀⠀⠀⢀⠤⠊⡠⠟⡦⠖⠁⠀⠀⠘⢆⡀⠀⡈⠀⡌⣸⠀⣿⠀⠀⠀⠀
⠀⠀⢨⡇⣾⣿⠀⠀⣿⢸⠀⠀⣠⠔⠒⠉⠀⠀⠈⢿⡳⡏⢸⣧⣋⣼⠇⠀⠀⢀⣀⠤⢊⡡⢔⡫⠔⠉⠀⠀⠀⠀⠀⠀⠀⠉⠓⢧⣠⠃⣿⡇⡇⠀⠀⠀⠀
⠀⠀⢸⡇⣿⣿⠀⠀⠇⡞⡤⠺⡁⠀⠀⠀⠀⠀⠀⠀⠙⠣⢌⡚⠭⠵⠦⠤⢬⣕⡲⠭⠓⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⠤⠽⣤⣿⡇⣷⠀⠀⠀⠀
⠀⠀⢸⡇⣇⢿⡄⠀⢠⣼⠾⣦⡙⢦⡀⠀⠀⠀⢀⡤⣤⠤⠌⠚⠛⠓⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⢒⣩⡴⠶⠛⠙⢿⣿⢱⡏⠀⠀⠀⠀
⠀⠀⠘⣇⣿⠘⢧⣠⡞⠁⠀⠈⠛⢦⣉⠲⠤⣀⡜⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠒⣩⡴⠞⠉⠀⠀⠀⠀⠀⠀⠹⣿⡀⠀⠀⠀⠀
⠀⠀⠀⠹⣼⣇⣾⠋⠀⠀⠀⠀⠀⠀⠙⠷⡒⠤⢇⡈⠒⠤⢄⣀⡀⠀⠀⠀⠀⠀⠀⢀⣀⡠⠤⠒⣉⣤⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀
⠀⠀⠀⠀⢈⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢱⡞⢼⠗⢶⣤⣤⣀⣉⣉⣉⣉⣉⣉⡥⢤⡲⣺⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀
⠀⠀⠀⠀⠾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣸⠓⢦⢻⡏⠉⠉⠀⠀⠀⠐⠈⠉⣹⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⣾⠀⣿⠀⠀⠱⣽⣆⠀⠀⠀⠀⠀⠀⠀⢹⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠿⢾⣶⣤⣤⡿⢀⡏⢀⣀⠀⠙⠛⠀⠀⠀⠀⠀⠀⠀⢸⠀⠈⠀⢀⣀⣄⣀⣤⡄⣤⣶⡯⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠚⠓⠛⠿⠿⠿⠯⠿⠷⠿⠶⠾⠾⠿⠿⠤⠾⠭⠿⠛⠓⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
                Select()
            else:
                print(red_color+"you did not select a correct key")
                print("action canceled"+reset_color)
                Select()
        else:
            print(red_color+"you did not select a correct key")
            print("action canceled"+reset_color)
            Select()
    else:
        print(red_color+"please add an event first"+reset_color)
        Select()
    return

#secret opton 5
def option_5():
    print(r"""
⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢻⣿⣿⣿⡿⠙⠉⣉⡉⠉⠉⠉⠉⠉⠉⣉⡉⠉⠛⢯⣍⠉⠉⠉⠙⢟⡋⢉⣽⣿⣿⣏⠉⠉⠉⠉⢉⣉⣉⣉⣉⣉⡉⠭⠭⠭⠭
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡄⠀⠀⠀⠀⠀⢸⡼⠟⠁⠀⣠⣾⡿⠀⢀⣤⡀⠀⠀⢶⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡿⠃⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠀⠀⠠⢤⣀⠀⣶⢹⢀⡇⠀⠀⠀⠀⣠⠞⠀⠀⠀⠘⠿⠋⠀⠀⠋⠀⠉⠀⠀⠀⠈⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⣀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠢⢄⡀⠈⠉⢙⣾⠮⠍⠙⠓⠲⣦⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀
⡀⢐⠐⣲⣤⣀⠉⠓⠂⡞⠀⡰⠚⠙⠓⠲⢼⡦⣀⠀⠀⠈⠛⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠘⣇⠀⠀⣈⣀⠀⢀⣔⣶⡖⠒
⠁⠀⡄⠀⠉⠛⠿⣶⢰⠃⣰⠁⠀⠀⣀⡴⢋⣥⠿⢓⣲⣾⠿⢍⣉⠐⣻⡤⢠⡀⠓⠦⣄⣀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠂⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢹⢖⣋⠤⠼⠯⡻⣿⡖⠖⢻
⠭⠥⠷⠶⡆⣀⡀⠀⡞⢠⠇⠀⢠⡾⣋⡔⠉⠀⣠⡾⠋⠀⠀⣠⣾⡫⠕⠻⣼⠹⡤⢀⣀⠈⠉⢯⠓⠒⠒⠲⣾⣳⡶⠶⠒⠲⣄⣀⣤⠞⠶⣄⡀⣴⡿⠋⠀⠀⠀⠀⠙⡞⣧⡀⠸
⠍⠋⠛⣄⣳⠈⠙⢳⡇⡸⠀⣠⢎⢴⠏⠀⠀⣼⠋⠀⠀⢀⣼⠟⠁⠀⠀⠀⠹⣧⢱⡀⠀⠉⠁⠘⢳⣄⠀⠉⠈⢿⡌⠉⠒⠢⡨⣳⡍⠑⠦⡈⢿⡋⠀⢀⡠⠴⠒⢦⡀⠸⣽⡩⠭
⠶⠾⠿⠟⠫⣤⣀⣼⡇⡇⣰⣣⢫⠃⠀⢠⡾⠁⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠀⠘⢇⠱⡄⠀⠀⠀⠀⠉⢆⠀⠀⠈⢷⠀⠀⠀⠹⡜⢽⡗⠦⡈⠪⣳⣔⠋⠀⣀⣴⠚⠃⡄⢻⣇⠀
⣉⣈⣨⣷⡄⠀⠉⣻⡿⡽⡱⢁⠇⠀⢠⡟⠁⠀⢀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡙⢆⠀⠀⠀⠀⠈⢆⠀⠀⠘⣇⠀⠀⠀⢣⠈⢿⡄⠈⠢⡈⡙⢦⡖⠁⠀⠹⡄⠱⡘⣿⠤
⠶⢆⡲⣿⣦⠾⠷⢾⣷⡳⠁⡎⠀⢀⡿⠁⠀⣀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢮⡳⠀⡀⠀⠀⠈⢆⠀⠀⢨⡄⠀⠀⠸⠀⠘⣧⡤⠤⠛⢇⡎⣇⠀⢀⠀⡇⠀⢣⢿⡍
⣄⣈⠇⣻⡟⣾⠀⡼⡱⠁⡸⠀⠀⣼⠃⠀⡴⠃⢀⡤⠄⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠚⠓⠛⢦⡙⠳⡄⠀⠈⢆⠀⠀⡆⠀⠀⠀⠀⠀⠸⡄⢀⡤⠞⡁⡿⡄⢸⠀⡇⠀⠘⡜⡇
⠓⠒⠀⠉⠛⢿⢺⡳⠁⢠⡇⠀⢠⡇⢀⡜⠡⣞⣁⣀⣀⡸⠇⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦⠤⠤⠤⠟⢦⣀⠀⠀⠈⢆⠀⡇⠀⠀⠀⠀⠀⢠⢻⠉⠀⢠⢣⣿⣷⣸⠀⡇⠀⠀⡇⢘
⡄⠤⠴⠶⠖⣺⢷⢃⠀⣸⠀⠀⣸⢳⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠙⠳⣤⡀⠘⣦⡇⠀⠀⢸⠀⠀⢸⡼⡶⠔⢁⣾⣻⣿⡿⢸⠁⠀⠀⠀⢸
⠀⠠⠤⠤⠴⣟⡏⡎⠀⡏⠀⠀⡽⡏⠀⠀⠀⣀⣤⠤⠖⠚⡃⠀⠀⠀⠀⠀⠀⠀⠀⢈⡛⠚⠳⠤⣄⡀⠀⠀⠈⠛⠯⣷⠇⠀⠀⡞⠀⠀⢸⡇⣿⢠⡾⢃⡇⣿⡇⡼⠀⠀⠀⡀⢸
⠀⠀⠀⠀⢰⢹⢠⠁⠀⢷⠀⠀⣿⢻⢀⡀⣀⣡⣤⣶⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⣽⣿⣶⣦⣄⣀⠀⠀⠀⠀⠀⡟⠀⠀⢠⠇⠀⠀⢸⠃⢸⠋⢠⠞⣼⡟⢱⠇⠀⠀⠀⡇⢸
⡲⣄⡀⠀⡟⡇⠀⠀⠀⢸⡂⢰⢸⡞⡟⠛⣿⣿⡿⠿⠛⠉⠁⠀⠲⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⢿⣿⣿⣿⣷⣦⡄⢠⠀⠀⠀⠈⠀⠀⠀⡎⠀⢸⡒⠚⠚⠛⠓⠛⠶⠦⢤⣈⣁⢸
⠉⠳⢭⡳⡇⡇⢠⠀⠀⠀⣧⠈⣧⢻⡇⢀⠌⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠃⠀⣠⠃⠀⠀⢀⡀⠀⠀⡸⠁⡄⢸⠣⠤⠖⠒⠒⠒⠦⠤⡄⠀⠉⠙
⠀⠀⠰⢯⣇⣧⢸⡄⢠⠀⠈⢦⡈⢿⣄⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⣰⠀⢀⠞⢠⠀⡴⠃⣸⠀⢸⠀⠀⠀⠀⠀⢀⡠⠊⠁⠀⠀⠉
⠀⠀⣠⢞⣿⣜⣤⢷⣸⠳⣄⠈⠻⣖⠙⠛⠃⠀⠀⠀⠀⠀⠀⠀⢠⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⡴⣺⢃⣴⡏⣠⢏⡴⣡⢶⠇⠀⡟⠛⠓⠆⠐⠒⠁⠀⠀⠀⣀⣠⠴
⠒⠞⣟⣛⠓⠚⠿⠬⣿⡇⠈⠙⡖⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣑⣋⣾⠾⠷⠾⣏⣱⣏⢀⣼⣁⡀⠀⣴⠒⣲⡤⣴⠒⠋⠁⠀⠀
⡛⠵⢖⣦⢭⣑⠢⠤⣀⡈⠙⠒⠾⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠔⣒⣛⡭⠉⢁⣀⡠⠤⠤⠐⢒⣒⣋⠭⠭⣿⣗⣻⣭⣭⣿⡽⡄⡇⠀⠀⠀⠀⠀
⡝⠛⠶⣮⣭⣓⡫⢕⣲⠭⡑⢢⣤⣀⠉⠛⠷⣄⣀⣀⣤⣀⣀⣀⣀⣀⣀⣀⡤⠖⣛⡩⠴⣒⡪⠭⠔⢒⣋⡉⠥⣤⣒⣲⡭⢽⣗⣒⣾⡯⢽⣿⠛⠿⡛⢿⣿⡏⣿⡇⠀⠀⠀⢠⠀
⢤⢌⣀⢀⣜⠙⡻⡿⢾⣭⣟⡲⠭⣟⠟⡂⠀⢮⡙⢦⣠⡇⣯⣿⣉⡿⢋⠥⠖⡩⠔⡂⠭⣔⣒⡮⣽⣗⣲⡿⢽⡿⠲⢟⠙⠛⡏⣠⣀⢌⠉⢀⡀⠀⢉⢸⣿⣭⡽⠃⠀⠀⠀⡞⠀
⡇⢀⠀⠈⠀⠀⠀⠀⢥⡂⠉⠛⠿⣷⣶⣍⣽⣂⣷⠤⢥⣤⠴⠶⣓⣤⣭⣭⣖⣻⣭⣭⠿⠷⠛⡋⢋⠅⠉⠑⠖⠉⠛⠀⠀⠀⠈⠉⠀⠀⠑⠁⠀⡀⢠⣞⡟⠛⢷⣄⠀⠀⣰⠃⠀
⣅⠀⠁⢀⠠⠀⠀⠀⠀⠀⠢⡀⠀⢹⣿⣿⣛⠿⠿⢯⣭⣭⣿⠿⠿⠻⣿⣿⡟⣩⠁⠀⠀⠐⣈⢄⣶⢠⡄⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡧⣄⣈⠻⣷⣤⡟⠀⠀
⡇⢀⠀⠀⢅⢀⠀⠐⠀⠀⠀⠓⠀⠤⠋⢹⡿⠃⡉⠉⠀⠁⠈⣧⡐⠀⢿⣿⡇⠅⠠⠆⠞⠉⠁⠀⠘⢂⠁⠀⢐⠀⡡⢄⠀⣄⣀⠀⠀⠀⠠⠀⠀⢠⡇⣿⣏⠙⠚⠿⣾⣿⣧⡀⠀
⡇⠀⠀⠄⣨⣆⠢⠀⢀⠀⠀⠀⠀⠀⢄⣸⡗⡲⠤⠁⣀⠀⠄⠠⠀⡀⢰⠿⣇⠀⠀⡆⠀⠠⣄⣀⠀⠀⠈⠆⠰⡁⠊⢀⣄⢱⠆⠰⠀⠈⠁⠠⣶⡆⣧⣿⣏⡉⠒⢤⣄⡙⢛⣿⣤
⢶⣄⠀⠀⠀⠈⠀⢧⡀⠒⡐⠄⠠⡆⡟⣿⡇⠃⠀⠀⠄⠀⠀⠀⠀⠈⢸⠰⣿⣦⡄⠃⠀⠀⠀⠀⡀⠀⠀⢁⠂⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⣿⣿⣟⡉⠘⠳⢾⡻⢶⣍⣬
⠀⣽⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠳⣧⣾⡆⠀⠏⠀⠀⡀⠀⢀⠀⠀⢸⣤⣿⡇⠀⠀⠀⠀⠃⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⢋⣄⠀⠀⠙⣶⡄⠈⣟⢆⢻⣿
⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢸⣿⣇⢄⠀⠘⠦⣀⠀⠀⠀⠀⠈⣿⢻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣕⠋⠒⣉⣀⠀⡿⣷⠀⢹⠘⡆⣯
⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⣿⣿⣘⡖⠶⠒⠶⠦⠔⠂⣶⠰⣿⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣦⡬⢤⣒⣪⣇⣇⣴⣻⠦⠿⣾
⣿⣿⣷⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣇⣝⣿⣇⣷⣀⣀⣐⣈⣂⣁⣸⣀⣿⣍⣀⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣾⣛⣛⣉⣩⣭⣥⣶⣒⣒⣚⣋⣲⣶⣐
    """)
    return
#option
def Select():
    print("Reminder: we will remove completed items (Events happened yesterday)")
    print("Choose any option below\n" \
    "        1 : View current and up coming events\n" \
    "        2 : Add an new event\n" \
    "        3 : view current date\n"\
    "        4 : Remove an event\n")
    #checks if the input is a number or not
    #https://www.w3schools.com/python/ref_string_isdigit.asp
    choice = input("Select an option: ")
    if not choice.isdigit():
        choice = "0"
    option = int(choice)
    #print list
    if option == 1:
        clear_screen()
        update_fixed_list()
        if len(fixed_list) >= 1:
            for item in fixed_list:
                print(item)
            Select()
        else:
            print(red_color+"please add an event first"+reset_color)
            Select()
    #add an event
    elif option == 2:
        add_event()
    #Date and time right now
    elif option == 3:
        clear_screen()
        date()
        Select()
    #Deleta an event
    elif option == 4:
        clear_screen()
        delete_event()
    #secret
    elif option == 5:
        option_5()
        Select()
    #If the user input something that is not in the option
    else:
        clear_screen()
        print(red_color+"Not a vaild option"+reset_color)
        Select()
    return
Select()
