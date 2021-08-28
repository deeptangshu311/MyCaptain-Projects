def my_function(string):

  d = dict()

  for key in string:

    if key not in d:

      d[key] = 1

    else:

      d[key] += 1

  return d



print(my_function(x))
