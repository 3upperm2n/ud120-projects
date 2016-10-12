#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    import numpy
    # rerr = np.subtract(predictions, net_worths)
    # rerr = np.square(rerr)
    rerr = numpy.subtract(predictions, net_worths)
    rerr = numpy.square(rerr)
#     print rerr
    tmp = numpy.concatenate((ages, net_worths), axis=1)
#     print tmp
    tmp = numpy.concatenate((tmp, rerr), axis=1)
#     print tmp
    
    tup_tmp = tuple(map(tuple, tmp))
#     print tup_tmp

     # sort the tup_tmp according to the error
    # http://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
    new_tup_tmp = sorted(tup_tmp, key=lambda x: x[2])
#     print new_tup_tmp

    # sorted in increasing order, extract the 90%
    cleaned_data = new_tup_tmp[:len(age) * 0.9]
    
    
    return cleaned_data

