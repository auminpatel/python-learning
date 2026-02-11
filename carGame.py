inputField = ''
started = False
while True:
    inputField = input("> ").lower()
    if inputField == 'help':
        print("""start: to start the car'
              stop: to stop the car'
              quit: to exit the game""")
    elif (inputField == 'start'):
        if started:
            print('You have already started')
        else:
            print('Car started... Ready to go!')
            started = True
    elif (inputField == 'stop'):
        if not started:
            print('Car has already stopped')
        else:
            print('Car stopped...')
            started = False
    elif (inputField == 'quit'):
        break
    else :
        print('I dont understand that')

