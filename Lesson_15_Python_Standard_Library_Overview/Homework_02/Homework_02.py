# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. 
# Также реализуйте возможность запуска из командной строки с передачей параметров



import re
import logging
import argparse

def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def number_of_words(text: str):
    logging.info("Starting word count process.")
    
    try:
        text = text.replace('\'', " ")
        logging.debug(f"Text after replacing apostrophes: {text}")
        
        filtered_string = (re.sub(r'[^a-zA-Zа-яА-ЯёЁ\s]', '', text)).lower()
        logging.debug(f"Filtered string: {filtered_string}")
        
        elements = filtered_string.split()
        logging.debug(f"Split elements: {elements}")

        my_dict = {}
        for element in elements:
            if element in my_dict:
                my_dict[element] += 1
            else:
                my_dict[element] = 1
        
        my_list = [(key, value) for key, value in my_dict.items()]
        my_list = sorted(my_list, key=lambda x: x[1], reverse=True)

        logging.info(f"Initial sorted word list: {my_list}")

        length = len(my_list)
        start = -1
        end = -1
        if length > 0:
            for i in range(length - 1):
                if my_list[i][1] == my_list[i + 1][1]:
                    if start < 0:
                        start = i
                    end = i + 1
                else:
                    if start >= 0:
                        my_list[start:end] = sorted(my_list[start:end], key=lambda x: x[0], reverse=True)
                        start = -1
                        end = -1
            if start >= 0:
                my_list[start:end + 1] = sorted(my_list[start:end + 1], key=lambda x: x[0], reverse=True)

        logging.info(f"Final sorted word list: {my_list[:10]}")
        print(my_list[:10])

    except Exception as e:
        logging.error(f"Error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Process a text string and count the frequency of words.")
    parser.add_argument("text", type=str, help="The text to analyze.")
    parser.add_argument("--log", type=str, default="word_count.log", help="Log file name.")
    args = parser.parse_args()

    setup_logging(args.log)
    logging.info("Script started.")
    number_of_words(args.text)
    logging.info("Script finished.")

if __name__ == "__main__":
    main()

