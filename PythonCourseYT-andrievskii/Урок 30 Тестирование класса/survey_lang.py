from work import AnonymousSurvey

question = "Какой язык программирования интересен?:"
my_survey = AnonymousSurvey(question)


my_survey.show_question()
print("Нажмите 'Q' для выхода \n")
while True:
	response = input("Language: ")
	if response == 'Q':
		break
	my_survey.store_responce(response)


print("\n Спасибо за ответ")
my_survey.show_results()