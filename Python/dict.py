def check_ph(ph):
    # dictionary of (min_value, max_value): 'Description of Ph'
    # just fill out for your needs
    table = {(0, 3): 'Strongly Acidic',(3, 6): 'Wakly Acidic',(6, 9): 'Neutral'}
    for ph_range, ph_description in table.items():
        # for every pair that you see in table
        if ph_range[0] <= ph < ph_range[1]:
            # if ph is greater or eqaual than min_value
            # and lesser than max_value
            print(ph_description)
            # return the ph description
            return ph_description
    
    # if the value is outside the table range just print it out
    print('ph out of range')
ph = float(input("pH observado é:\n"))
check_ph(ph)
