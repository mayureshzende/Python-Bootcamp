"""
 for an module if it is in the samw file directory then we can using the file name import and use the function 
"""
# from my_module import my_func_module

# my_func_module()


"""
 to have the code organise and let python know we are using the packaage 
 we need to create an __init__.py file -> which will be intially empty file 
 this is the way to let python know that we are creating the package 
"""
# import the main method from the main package folder 
from mypackage import main_package

# calling the main method 
main_package.main_package_method()

# we can also call the subpackage in  the nested folder 
from mypackage.subpackage import sub_package

sub_package.sub_package_method()
