feedback_files = ['feedback1.txt','feedback2.txt','feedback3.txt'] 

def read_file(feedback_files): #function made to read content of all 3 files and handle exception if a file is not found
    feedback = []
    for file_name in feedback_files:
        try:
            with open(file_name, 'r+') as file: #open file in reading mode to read and store all feedbacks in feedback list 
                feedback.append(file.readlines())  
        except FileNotFoundError as f: #handling an exception(if it occurs) if one of the files is not found 
            print(f"{file_name} not found. Check spelling or see if file exists.")
            return None
    
    return feedback

def split_feedback(feedback): #function to split up the lines into names, ratings and comments and storing it in spli_data[]
    split_data = []
    for lines in feedback:  
        for line in lines:  
            if line:  
                x = line.split(': ') #using split to seperate name and rating,comment
                name = x[0] 
                y = x[1].split(' - ') #using split to seprate rating and comment
                rating = y[0]
                comment = y[1]
                split_data.append((name, rating, comment)) #storing name, rating and comment in list 
    
    return split_data


def average(split_data, output_file): #function to calculate and display average rating and total number of feedbacks
    avg = sum(int(i[1]) for i in split_data) / len(split_data)  #calculating average by adding all ratings in split_data list and dividing it by the length of the list

    with open(output_file, 'a+') as out_file:  
        out_file.write(f'Total Feedback Entries: {len(split_data)}\n') #displaying total entries
        out_file.write(f'Average Rating: {avg}\n')  #displaying average rating


def comment_summary(feedback_files, output_file): #function to write all feedbacks into output file 
    with open(output_file, 'a+') as out_file: #file open with append mode to add each feedback at the end of file
        out_file.write('Feedbacks:\n')  
        for file_name in feedback_files:
            with open(file_name, 'r+') as in_file: 
                for line in in_file:
                    out_file.write(line)  

#using the functions created above                
feedback_files = ['feedback1.txt', 'feedback2.txt', 'feedback3.txt'] 
a = read_file(feedback_files)

if a is not None: #if a file is not found the below statements are not executed and code is terminated 
    b = split_feedback(a)
    average(b, 'feedback_summary.txt')
    comment_summary(feedback_files, 'feedback_summary.txt')
