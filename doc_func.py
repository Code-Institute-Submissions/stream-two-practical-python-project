import operator
################## READ/WRITE FUNCTIONS ###############################

def write_to_doc(file, data):
    with open(file, "a") as file:
        file.writelines(data)
        
def read_doc(file):
    with open(file, "r") as file:
        words = file.read()
    return words

def read_and_replace(file, old, new):    
    with open(file, 'r+') as f:
        content = f.read()
        f.seek(0)
        f.truncate()
        f.write(content.replace(old, new))
        f.close
    
def write_username_and_current_word_to_file(username, letter_string, file):
    read_current_word_file = read_doc(file)
    write_data = "\n{0}\n{1}_guesses:;\n{2}\n{3}_fail_count:11:\n".format(username, username, letter_string, username)
    if username in read_current_word_file:
        with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                break
            for line in f:
                old_word = line
                new_word = letter_string
                break
            for line in f:
                ##print(line)
                old_counter = line
                new_counter = "{0}_fail_count:11:\n".format(username)
                break
        read_and_replace(file, old_word, new_word + "\n")
        read_and_replace(file, old_counter, new_counter) 
    else:
        write_to_doc(file, write_data)

def get_users_current_word(username, file):
    with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                break
            for line in f:
                word = line
                return word

def write_guesses_to_current_word_file(username, word, current_word_file, correct_guess):
    with open(current_word_file, "r") as f:
        for line in f:
            if username in line:
                break
        for line in f:
            if correct_guess not in line:
                old_line = line
                split_line = line.split(";")
                new_line = "{0}{1}:;\n".format(split_line[0], correct_guess)
                read_and_replace(current_word_file, old_line, new_line)
                break
            else:
                print("Already guessed {0}".format(correct_guess))    
                break
        
def clear_old_guesses_from_file(username, file):
    read_current_word_file = read_doc(file)
    if username in read_current_word_file:
        with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                old_line = line
                new_line = "{0}_guesses:;\n".format(username)
                break

        read_and_replace(file, old_line, new_line)
    
def get_users_correct_guesses(username, file):
    with open(file, "r") as f:
        for line in f:
            if username in line:
                break
        for line in f:
            guesses = line
            break
    return guesses

def write_current_scores_to_file(username, file, word):
    scores_file = read_doc(file)
    word_length = len(word)
    word_score = word_length - 1

    if username in scores_file:
        with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                old_score = line
                old_score_list = list(map(str, old_score.split(":")))
                old_score_to_int = int(old_score_list[2])
                new_score_sum = old_score_to_int + word_score
                new_score = ":{0}:{1}:\n".format(username, new_score_sum)
                break
        read_and_replace(file, old_score, new_score)
    else:
        write_to_doc(file, "\n:{0}\n:{1}:{2}:\n".format(username, username, word_score))

def get_current_user_score(username, file):
    scores_file = read_doc(file)
    if username in scores_file:
        with open(file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                old_score = line
                old_score_list = list(map(str,old_score.split(":")))
                current_score = old_score_list[2]
                break  

            return current_score

def incorrect_guesses_counter_iterator(current_word_file, username):
    read_current_word_file = read_doc(current_word_file)
    if username in read_current_word_file:
        with open(current_word_file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                break
            for line in f:
                break
            for line in f:
                old_count = line
                old_count_list = list(map(str,old_count.split(":")))
                counter = int(old_count_list[1])
                if counter >= 0:
                    counter -= 1
                set_new_count = old_count_list
                set_new_count[1] = str(counter)
                new_count = ":".join(set_new_count)
                break

        read_and_replace(current_word_file, old_count, new_count)

def get_incorrect_guesses_counter(current_word_file, username):
    read_current_word_file = read_doc(current_word_file)
    if username in read_current_word_file:
        with open(current_word_file, "r") as f:
            for line in f:
                if username in line:
                    break
            for line in f:
                break
            for line in f:
                break
            for line in f:
                incorrect_list = list(map(str, line.split(":")))
                incorrect_count = int(incorrect_list[1])
                ##print(incorrect_count)
                break

            return incorrect_count

def get_scores_for_leaderboard(scores_file):
    with open(scores_file, "r") as f:
        all_scores = []
        scores_line = list(f)[2::3]
        for i in scores_line:
            scores_list = list(map(str, i.split(":")))
            scores_list.pop(0)
            scores_list.pop(2)
            scores_list[1] = int(scores_list[1])
            all_scores.append(scores_list)
        all_scores.sort(key=operator.itemgetter(1), reverse=True)

        return all_scores[:10]