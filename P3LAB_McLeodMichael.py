#CTI-110
#P3LAB - Debugging
#Michael McLeod
#2/24/20
def main ():
    score = int(input('enter numerical score.'))
    
    if score >= 90:
        print('Your grade is A.')
    else:
        if score >= 80:
            print ('Your grade is B.')
        else:
            if score >= 70:
                print ('Your grade is C')
            else:
                if score >= 60:
                    print ('Your score is D.')
                else:
                    print ('Your score is F.')
main()
