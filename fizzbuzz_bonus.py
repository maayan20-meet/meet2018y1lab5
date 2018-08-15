


while True:
    input_response = input('question')
    try:
        input_response = int(input_response)
    except:
        print('wrong input type')
        break
    if (input_response % 3 == 0) and (input_response % 5 == 0):
        print('fizzbuzz')
    elif input_response % 5 == 0:
        print('buzz')
    elif input_response % 3 == 0:
        print('fizz')
    else:
        print(input_response)
        
