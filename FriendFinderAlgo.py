
'''Source code header goes here '''

def open_file():
    ''' Remember the docstring'''
    valid_filename = False
    while valid_filename == False:
        filename = input("\nEnter a filename: ")
        try:
            fp = open(filename)
            valid_filename = True
        except:
            print("\nError in filename.")

    return fp


def read_file(fp):
    ''' Remember the docstring'''
    global n 
    n = int(fp.readline().strip())

    network = [[] for i in range(n)]

    for line in fp:
        u, v = map(int, line.split())
        network[u].append(v)  
        network[v].append(u)  

    return network

def num_in_common_between_lists(list1, list2):
    combined_list = []
    for element in list1:
        if element in list2:
            combined_list.append(element)
    common_num = len(combined_list)
    return common_num
    

def calc_similarity_scores(network):
    ''' Remember the docstring'''
    n = len(network)
    similarity_matrix = [[0] * n for i in range(n)]

    for user1 in range(n):
        for user2 in range(user1 + 1, n):
            common_friends = 0
            for friend1 in network[user1]:
                if friend1 in network[user2]:
                    common_friends += 1

            similarity_matrix[user1][user2] = common_friends
            similarity_matrix[user2][user1] = common_friends

    for user in range(n):
        total_friends = len(network[user])
        similarity_matrix[user][user] = total_friends

    return similarity_matrix


def recommend(user_id, network, similarity_matrix):
    ''' Remember the docstring'''
    n = len(similarity_matrix)
    
    most_similar_user = -1  
    highest_similarity_score = -1
    
    for candidate_user in range(n):
        if candidate_user != user_id and candidate_user not in network[user_id]:
            if similarity_matrix[user_id][candidate_user] > highest_similarity_score:
                most_similar_user = candidate_user
                highest_similarity_score = similarity_matrix[user_id][candidate_user]
    
    return most_similar_user



def main():
    # by convention "main" doesn't need a docstring
    print("Facebook friend recommendation.\n")

    "\nThe suggested friend for {} is {}"
    "\nEnter an integer in the range 0 to {}:"
    "\nError: input must be an int between 0 and {}"
    
    fp = open_file()
    network = read_file(fp)
    
    similarity_matrix = calc_similarity_scores(network)

    end = False
    while end == False:

        valid_userid = False
        while valid_userid == False:
            user_id = input("\nEnter an integer in the range 0 to {}:".format(n-1))
            try:
                user_id = int(user_id)
                valid_userid = True
            except:
                print("\nError: input must be an int between 0 and {}".format(n-1))

        second_user_id = recommend(user_id, network, similarity_matrix)

        print("\nThe suggested friend for {} is {}".format(user_id, second_user_id))

        end_choice = input("\nDo you want to continue (yes/no)? ")
        if end_choice.lower() == "no":
            end = True


if __name__ == "__main__":
    main()
