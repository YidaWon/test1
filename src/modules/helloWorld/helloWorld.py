from logs import logDecorator as lD 
import json, pprint

config = json.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.modules.helloWorld.helloWorld'


@lD.log(logBase + '.doSomething')
def doSomething(logger):
    '''print a line
    
    This function asks the user for input. Then adds the sum of digits.
    Repeat until only a single digit is left. Returns that digit.
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    '''

    x = input('Hello world. Please enter any integer and I will sum it: ')

    while len(str(x)) > 1:
        total = 0
        for n in str(x):
            total += int(n)
        x = total

    print('Hello world, your summed digit is', str(x)+'.')

    return

@lD.log(logBase + '.main')
def main(logger, resultsDict):
    '''main function for helloWorld
    
    This function finishes all the tasks for the
    main function. This is a way in which a 
    particular module is going to be executed. 
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    resultsDict: {dict}
        A dintionary containing information about the 
        command line arguments. These can be used for
        overwriting command line arguments as needed.
    '''

    print('='*30)
    print('Main function of helloWorld')
    print('='*30)

    doSomething()

    print('Getting out of helloWorld')
    print('-'*30)

    return

