import io
import pstats
import cProfile

# save cprofile resilt in excel file
def save_file(cprofile):
    result = io.StringIO()
    pstats.Stats(cprofile,stream=result).print_stats()
    result=result.getvalue()
    result='ncalls'+result.split('ncalls')[-1]
    result='\n'.join([','.join(line.rstrip().split(None,5)) for line in result.split('\n')])
   
   
    with open('test.csv', 'w+') as f:
        f.write(result)
        f.close()


def profile(*args, **kwargs):
    '''cProfile decorator'''
    def warpper(func):
        cprofile = cProfile.Profile()
        cprofile.enable()
        res = func(*args, **kwargs)
        cprofile.disable()
        
        if kwargs.get('with_file') == True:
            save_file(cprofile)
        else:
            cprofile.print_stats()

        return res
    return warpper

