from cprofile_decorator import profile
'''
cprofile decorator argument:
    * with_file:
        - True: save the result in CSV file
        - False: print the result to console
'''
text = "some test test for this section"
@profile(text, with_file=False)
def create_file(*args, **kwargs):
    with open("test.txt", 'w') as file:
        file.write(args[0])


@profile(with_file=True)
def looping(*args, **kwargs):
    for i in range(50000000):
        pass

if __name__ == "__main__":
    looping
    create_file


