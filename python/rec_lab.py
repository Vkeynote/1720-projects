def replicate_iter(times, data):
    if((not isinstance(times, int)) or (not isinstance(data, (int, float, long, complex, str)))):
            raise ValueError("Invalid arguments")
    elif(times <= 0):
            return []
    else:
            array = []
            for x in range(times):
                    array.append(data)
            return array


def replicate_recur(times, data):
    if((not isinstance(times, int)) or (not isinstance(data, (int, float, long, complex, str)))):
            raise ValueError("Invalid arguments")
    elif(times <= 0):
            return []
    else:
            return ([data] + replicate_recur((times - 1), data))   
