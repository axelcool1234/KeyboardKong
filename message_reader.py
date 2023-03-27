# message_reader.py
# Module handles user messages and returns a bot response.
import ape_reader

class MessageProcessError(Exception):
    pass
def process_request(command: str) -> str:
    command = command.lower()
    if command.startswith('monkey'):
        request = process_monkey_request(command)
        #response (DICT) = ape_handler.generate_response(APE_KEY, request)
        #message  (STR) = ape_reader.process_response(response)
        #return message
        pass
    elif command.startswith('help'):
        #TODO: Fix this mess...
        return '```' \
               '🟡 === KeyboardKong Commands === 🟡\n' \
               '!monkey personalbest [mode] [mode2]\n' \
               'mode: Categories for personal best, such as time.\n' \
               'mode2: Secondary category, such as 60 for time.\n\n' \
               'This command gives the user their personal best in a given category.\n' \
               'Make sure your discord is linked with MonkeyType!\n' \
               '🟡 ============================= 🟡\n\n' \
               '!monkey stats\n' \
               'This command gives the user their typing statistics.\n' \
               '🟡 ============================= 🟡\n\n' \
               '!monkey profile [ID]\n' \
               'Given a user ID, retrieve information about a user.\n' \
               '🟡 ============================= 🟡\n\n' \
               '!monkey leaderboard [mode] [mode2] [entry]\n' \
               'mode: Categories for personal best, such as time.\n' \
               'mode2: Secondary category, such as 60 for time.\n\n' \
               'entry: how many entries to skip forward to.\n\n' \
               'This command gives the global leaderboard for MonkeyType users.\n' \
               '🟡 ============================= 🟡\n\n' \
               '!monkey rank [mode] [mode2]\n' \
               'mode: Categories for personal best, such as time.\n' \
               'mode2: Secondary category, such as 60 for time.\n\n' \
               'This command gives the asking user their rank.\n' \
               '🟡 ============================= 🟡\n' \
               '' \
               '```'
    else:
        return None

def process_monkey_request(command: str) -> tuple:
    command_parameters = command.split()
    match command_parameters[1]:
        case 'personalbest':
            pass
        case 'stats':
            pass
        case 'profile':
            pass
        case 'leaderboard':
            pass
        case 'rank':
            pass
        case other:
            raise MessageProcessError