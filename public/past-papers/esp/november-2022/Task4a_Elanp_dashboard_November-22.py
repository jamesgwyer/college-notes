import pandas as pd

def main_menu():
    flag = True

    while flag:

        print("#################################################")
        print("#### Welcome to Elanp Air Flight Data system ####")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. View passenger numbers")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice


def get_depart():
    flag = True

    while flag:

        print("########### Please select departure airport #############")
        print("### 1. Dublin (DUB)")
        print("### 2. Edinburgh (EDI)")
        print("### 3. Glasgow (GLA")
        print("### 4. London Heathrow (LHR)")
        print("### 5. London Luton (LTN)")
        print("### 6. Manchester (MAN)")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice


def get_destination(depart):
    flag = True

    while flag:

        print("########### Please select destination airport #############")
        print("### 1. Dublin (DUB)")
        print("### 2. Edinburgh (EDI)")
        print("### 3. Glasgow (GLA")
        print("### 4. London Heathrow (LHR)")
        print("### 5. London Luton (LTN)")
        print("### 6. Manchester (MAN)")

        choice = input('Enter your number selection here: ')
        
        if choice == depart:
            print("")
            print("")
            print("############### Data entry error ###################")
            print('Destination and departure airports must be different')
            print("")
            print("")           
        else:
            try:
                int(choice)
            except:
                print("Sorry, you did not enter a valid option")
                flag = True
            else:    
                print('Choice accepted!')
                flag = False

    return choice

def get_number_days():

    flag = True

    while flag:

        print("########### Please enter the number of previous days of data you wish to see #############")
        choice = input('Enter your number selection here: ')
 
        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid number")
            flag = True
        else:    
            print("########### You have chosen to see data for the last {} days #############".format(choice))
            flag = False
        

    return int(choice)


        
        

def convert_men_choice(choice):
    if choice == "1":
        conv_choice = "DUB"
        return conv_choice
    elif choice == "2":
        conv_choice =  "EDI"
        return conv_choice
    elif choice == "3":
        conv_choice =  "GLA"
        return conv_choice
    elif choice == "4":
        conv_choice =  "LHR"
        return conv_choice
    elif choice == "5":
        conv_choice =  "LTN"
        return conv_choice
    else:
        conv_choice =  "MAN"
        return conv_choice


def get_data( depart, dest,days):
    df = pd.read_csv("Task4a_data.csv")
    extract = df.loc[(df['From'] == depart) & (df['To'] == dest)]
    extract_days = extract.iloc[: , -days: ]
    print("We have found these flights that match your criteria:")
    return extract_days



main_menu_choice = main_menu()
depart_airport = get_depart()


destination_airport = get_destination(depart_airport)

dep_choice = convert_men_choice(depart_airport)
dest_choice = convert_men_choice(destination_airport)

days = get_number_days()
print("You have selected departure from: {}".format(dep_choice))
print("You have selected destination as: {}".format(dest_choice))



extracted_data = get_data(dep_choice, dest_choice, days) 

extract_no_index = extracted_data.to_string(index=False)



print(extract_no_index)


