
def questionMenu():
	for questLoop in range(0,4):
		while True:
			try:
				print ("\033[1;32m Your question  ?\n")
				answerQuestionOne = int(input("1-Yes \n2-Not \n3-Else , why?"))
				if answerQuestionOne ==3:
					whyQuestion = str(input("Why question ? >"))
					
				print("Your question ??\n")
				answerQuestionTwo = int(input("1-yes \n2-not \n3-else , why?"))
				if answerQuestionTwo == 3:
					whyQuestionTwo = str(input("why?"))
					
				print("your question?\n")
				answerQuestionThree = int(input("1-yes \n2-not \n3-else , why?"))
				if answerQuestionThree == 3:
					whyQuestionThree = str(input("why question?"))
					
				print("your question\n")
				answerQuestionFour = int(input("1-yes \n2-not \n3-else , why?"))
				if answerQuestionFour == 3:
					whyQuestionFour = str(input("why question?"))

				print("\n== BROKEN BROKEN === :) ")
				brokenCry = str(input("SAY HELLO \n"))
				print("\033[1;94m=============================================================")
				print("\033[1;94m====================another person===========================")
					
			except ValueError:
				print("Choose antoher option : ")
				print("=============================================================")
				print("====================another text===========================")
				print("=============================================================")
questionMenu()