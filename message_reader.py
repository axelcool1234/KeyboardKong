# message_reader.py
# Module handles user messages and returns a bot response.
import ape_reader
def process_request(message: str) -> str:
    message = message.lower()
    if message.startswith('monkey'):
        #request  (TUPLE) = BLAH BLAH BLAH
        #response (DICT) = ape_handler.generate_response(APE_KEY, request)
        #message  (STR) = ape_reader.process_response(response)
        #return message
        pass
    elif message.startswith('help'):
        return '```' \
               '🟡 === KeyboardKong Commands === 🟡\n' \
               '!monkey personalbest [mode] [mode2]\n' \
               'mode: Categories for personal best, such as time.\n' \
               'mode2: Secondary category, such as 60 for time.\n' \
               '🟡 ============================= 🟡' \
               '```'
    else:
        return None