import random
capitals={'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phoenix', 'Arkansas':'Little Rock','California':'Sacramento','Colorado':'Denver','Connecticut':'hearthford','Delaware':'Dover','Florida':'Tallahasee','Georgia':'Atlanta','hawai':'Honolulu','Idaho':'Boise','Illinoise':'Springield','Indiana':'Indianapolis','Iowa':'Des Moines','kansas':'topeka','kentucky':'Frankfort','Louisiana':'baton Rouge','Maine':'Augusta','Maryland':'Annapolis','Massachusetts':'Boston','Michigan':'Lansing','Minnesota':'Saint Paul','Mississipi':'Jackson','Missouri':'jefferson City','Montana':'Helena','Nebraska':'Linkoln','nevada':'Carson City','New Hampshire':'Concord','New Jersey':'Trenton','New Mexico':'Santa Fe','New York':'Albany','North Carolina':'Raleigh','North Dakota':'Bismark','ohio':'Columbus','oklahoma':'Oklahoma City','Oregon':'Salem','Pennsylvania':'Harrisburg','Rhode Island':'Providence','South Carolina':'Columbia','South Dakota':'Pierre','Tennessee':'Nashvile','Texas':'Austin','Utah':'Salt lake city','Vermont':'Montpelier','Virginia':'Richmond','Washington':'Olympia','West Virginia':'Charleston','Wisconsin':'madison','Wyoming':'Cheyenne'}
for quizNum in range(35):
    quizFile=open('capitalsquiz%s.txt' %(quizNum+1), 'w')
    answerkeyfile=open('capitalsquiz_answers%s.txt' %(quizNum+1), 'w')
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(' '*20+'State Capitals Quiz (Form %s)' %(quizNum+1))
    quizFile.write('\n\n')
    states=list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(50):
        correctAnswers=capitals[states[questionNum]]
        wrongAnswers=list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswers)]
        wrongAnswers=random.sample(wrongAnswers, 3)#uzima prvi argument listu i broj atributa koje ce da random uzme
        AnswerOption=wrongAnswers+[correctAnswers]
        random.shuffle(AnswerOption)
        quizFile.write('%s. What is the capital of %s?\n' %(questionNum+1,states[questionNum]))
        for i in range(4):
            quizFile.write('       %s: %s\n' %('ABCD'[i], AnswerOption[i]))
            quizFile.write('\n')
        answerkeyfile.write('%s. %s\n' %(questionNum+1,'ABCD'[AnswerOption.index(correctAnswers)]))
    quizFile.close()
    answerkeyfile.close()
