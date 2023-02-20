# Software Engineer: RIAAN DEVENTER
# Written on 15 February 2023

#------------------------------------------------------------------------------------------------
# ● Read in the movies.txt file. Each separate line is a description of a different movie.
# ● Create a function to return which movies a user would watch next if they have watched 
#       Planet Hulk with the description “Will he save their world or destroy it? When the Hulk 
#       becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch 
#       him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the
#       planet Sakaar where he is sold into slavery and trained as a gladiator.”
# ● The function should take in the description as a parameter and return the title of the most similar movie.
#------------------------------------------------------------------------------------------------

# ****************************************************** 
#   Import Libraries
# ******************************************************
import spacy

nlp = spacy.load('en_core_web_md')

#============= Movies list ===========
movie_lst = []
desc_lst = []

#========== Function to read movies data ==============
def read_movie_data():
    '''
    This function will open the file movies.txt and read the data from this file, 
    then read the movie name into movies_lst and the description into desc_lst. 
    Use the try-except in this function for error handling. 
    There are no headings in the file.
    '''
    # If we find the movies.txt file then f_movie will change from None to a representation of the file.
    f_movie = None
        
    while f_movie == None :
        
        try:
            # Open the file for read mode. If the file is found then f_movie value will change and 
            # the while f_movie == None will not repeat at the end of this instance.
            f_movie = open ("./movies.txt", "r")
           
            # Now read through the file till end.
            for line in f_movie :
                if line.strip () :
                    # We remove the next line character to fix the data value at the end of the line.
                    line = line.replace ("\n", "")
                    # Separate the string by " :" and place the parts into a list.
                    new_movie_lst = line.split (" :")
                    # Append 1st string to movie_lst and 2nd string to desc_lst.
                    movie_lst.append (new_movie_lst [0])
                    desc_lst.append (new_movie_lst [1])

        # If the file in the open statement above is not found then this FileNotFoundError logic will run.
        except FileNotFoundError:
            print ()
            print("--> The movie file cannot be found in the folder.")
            exit()

        finally:
            # If the file is not found, we will get an error on f_movie.close (), so we will only execute
            # this if we found the file represented by f_movie value changing from None.
            if f_movie is not None:
                f_movie.close()
            # If there are movie entries, then we will display success message else we will display error message.
            if len (movie_lst) > 0:
                pass
            else :
                print ()
                print ("--> Movies load error... CHECK the Movie File content!")

def recommend_movie(desc_to_compare):
    '''
    This function will recommend movies to watch by looking for similarities with an input
    description of a movie that has already been watched.
    '''
    # recommend_lst contains the indexes for the 3 highest similarities.
    recommend_lst = [0,0,0]
    sim_lst = [0,0,0]

    model_movie = nlp(desc_to_compare)

    for i in range (len(desc_lst)):
        similarity = nlp(desc_lst[i]).similarity(model_movie)
#        print(movie_lst[i] + " - ", similarity)
        if similarity >= sim_lst[0]:
            sim_lst[0], sim_lst[1], sim_lst[2] = similarity, sim_lst[0], sim_lst[1]
            # We move the recommendations to the right and insert the new higher recommendation at index 0.
            recommend_lst[0], recommend_lst[1], recommend_lst[2] = i, recommend_lst[0], recommend_lst[1]
        elif similarity >= sim_lst[1]:
            sim_lst[1], sim_lst[2] = similarity, sim_lst[1]
            # We move the recommendations to the right and insert the new higher recommendation at index 0.
            recommend_lst[1], recommend_lst[2] = i, recommend_lst[1]
        elif similarity >= sim_lst[2]:
            sim_lst[2] = similarity
            # We move the recommendations to the right and insert the new higher recommendation at index 0.
            recommend_lst[2] = i      
        
    return recommend_lst

# ============  MAIN LOGIC - Recommend Movies  ===============
# Load the movie data from the file.
read_movie_data()

# Load the description for the movie that was watched.

desc_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, \
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in \
peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Now we call the recommendation function and pass the description of what the viewer have watched.
recommend_lst = recommend_movie (desc_to_compare)
# print(recommend_lst)
# Now we can display the recommended movies.
print()
print(f"--------------- Movie Recommendations for Planet Hulk Viewers ---------------")

print (f"1 : {movie_lst[recommend_lst[0]]}")
print (f"2 : {movie_lst[recommend_lst[1]]}")
print (f"3 : {movie_lst[recommend_lst[2]]}")

print(f"-----------------------------------------------------------------------------\n")
