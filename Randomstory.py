import random
print("Type the cmd (Generate) and create a funny wacky story")
GenerateInput = input()
#creating important story elements
sentence_starters = ['Around 690 BC ', 'Somewhere around 1987 of november ', 'Somewhere in the bingus ages ']
charecters = ['There lived a floppa ', 'there lived a bingus ', 'There lived a johnny ']
time = ['one day', 'one afternoon ','one bingus moon ','one floppa moon ']
story_plots = [' he was passing by ', ' he was going for a picnic to ', 'he was pooping in a tv ']
place = [' the mountains ', ' the garden ', 'the eiffel tower ', 'the bingus highway ', 'the pp house ']
second_character = [' he saw a man ', ' he saw a young lady ', 'he saw a bingus ', 'he saw a floppa ']
age = [' who seemed to be in late 20s ', ' who seemed very old and feeble ', 'who seemed to be a tarek ', 'he seemed to be as chill as aaron ']
work = [' searching something. ', ' digging a well on roadside. ', 'pooping on a rock ']

if GenerateInput == "Generate":
    print(random.choice(sentence_starters) + random.choice(charecters) + random.choice(time) + random.choice(story_plots) + random.choice(place)
          + random.choice(second_character) + random.choice(age) + random.choice(work))
