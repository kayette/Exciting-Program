import wolframalpha
import wikipedia
from tkinter import *
import speech_recognition as sr
import pyjokes

while True:
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("\nListening...")
		audio = r.listen(source)
		try:
			print("\nRecognizing...")
			text = r.recognize_google(audio)
			print("\nYou said: " + text)
			if text == "stop":
				print("\nProgram will exit. Thank you for using Primo!\n")
				break
			elif text == "hi primo":
				print("\nHello there, human. I'm Primo. How may I be of service?")
				continue
			elif text == "tell me a joke":
				joke = pyjokes.get_joke()
				print("\n" + joke)
			else:
				window = Tk()
				window.title("Primo")
				window.geometry("1000x800")
				try:
					app_id = "6LQW8W-82QHWQL39G"
					client = wolframalpha.Client(app_id)
					res = client.query(text)
					answer = next(res.results).text
					print("\nAnswer from Wolfram|Alpha:")
					print(answer)
					label1 = Label(window, justify=LEFT, wraplength=850, compound=CENTER, padx=10, text=answer, font='Arial 15')
					label1.pack()
					window.after(5000, lambda: window.destroy())
					mainloop()
				except Exception as e:
					print("\nNo results from Wolfram|Alpha. Trying wikipedia...")
					answer = wikipedia.summary(text)
					print("\nAnswer from Wikipedia:")
					print(answer)
					label1 = Label(window, justify=LEFT, wraplength=850, compound=CENTER, padx=10, text=answer, font='Arial 15')
					label1.pack()
					window.after(500000, lambda: window.destroy())
					mainloop()
		except Exception as e:
			print(e)
			answer = "\nSorry, I did not get that. Come again?"
			print(answer)