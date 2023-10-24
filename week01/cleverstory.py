# Input of the needed words
adj1 = input('Provide one adjective: ')
animal = input('Provide one animal: ')
verb1 = input('Provde one verb: ')
exclam = input('Provide one exclamation: ')
verb2 = input('Provide another verb: ')
verb3 = input('Provide one final verb: ')

# Output of the story

print()
print('Here is your story:')
print()
print('The other day, I was really in trouble. It all started when I saw a very')
print(f'{adj1.lower()} {animal.lower()} {verb1.lower()} down the hallway. "{exclam.capitalize()}!" I yelled. But all')
print(f'I could think to do was to {verb2.lower()} over and over. Miraculously,')
print(f'that caused it to stop, but not before it tried to {verb3.lower()}')
print('right in front of my family.')

# Adding a prompt to see if the user would like to continue the story

print()
more = input('Would you like to continue the story? ')

# Checking to see if the first character of the input above is Y (assuming they said yes)
if more[0].lower() == 'y':
    # Needed to use " to accomodate aren't in the prompt
    print()
    verb4 = input("We aren't done with verbs, we need one more: ")
    noun = input('Provide one noun: ')
    historic_figure = input('Provide the name of a Historic Figure: ')
    time = input('Provide a length of time: ')    
    catch_phrase = input('What is the catch phrase of your favorite movie character? ')
    vacation_spot = input('What is your favorite vacation spot? ')

    print()
    print(f'Had I not {verb3.lower()}ed, I am very sure that the {animal.lower()} would have {verb4.lower()}ed.')
    print(f'Having to clean up the {noun} would have taken {time.lower()}.')
    print(f'Gratefully, {historic_figure.title()} saw this fiasco and said: "{catch_phrase}"')
    print(f'Then all of a sudden I woke up from this strange dream and realized that I was late to catch my flight to {vacation_spot.title()}!')

# If they don't want more story, thanking them for reading part 1
else:
    print('Thank you for reading my short story.')

