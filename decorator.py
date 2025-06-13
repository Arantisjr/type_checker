from functools import wraps
import inspect


 # This decorator checks if the arguments passed to a function
 # match the types you wrote in the function's definition.
def type_checker(fxn):
    # keeps the  functions original name and meta data(if it's remved the functions name in which the decorator is passed will be changed to wrapper )

    @wraps(fxn)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fxn) #gets info about the functions arguments and thier types
        bound_args = sig.bind(*args, **kwargs) # binds the passed arguments to the function's signature
        bound_args.apply_defaults() # fill out any default values for the arguments


        # going through each argumenunt in the function and it value

        for name, value in bound_args.arguments.items():
            # gets the type you wrote for any argument if any
            expected_type = fxn.__annotations__.get(name)
            if expected_type: # tthat is if you wrote a type for this arguments
                # checking if the value matches the type
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"argument {name} must be {expected_type}"
                    )
                # if all types are correct run the original function
        return fxn(*args, **kwargs)
    return wrapper         

