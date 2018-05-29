def is_palindrome_string(s):
    if s is None:
        return False
    
    len_string = len(s)
    if s == s[len_string::-1]:
        return True
    else:
        return False




def find_longest_palindrome_substring(s):
    len_string = len(s)
    max_len_palindrome_string =  0
    longest_palindrome_substring = ""
    
    for i in range(len_string):
        start_pos = i
        step = start_pos
        print("start_pos = %d"%i)
        #print("step = %d"%i)
        print("len_string - start_pos = %d"%(len_string - start_pos))
        print("start_pos - 0 = %d"%(start_pos - 0))

        if (len_string - start_pos) < (start_pos - 0):
            step = len_string - start_pos
        else:
            step = start_pos
                
        print("step = %d"%step)
        
      
        for j in range(step + 1):
            
               temp_str = s[start_pos - j :start_pos + j + 1]
               print("current temp_str is %s"%temp_str)

               if is_palindrome_string(temp_str) is True:
                  print("%s is palindrome string"%temp_str)

                  if len(temp_str) > max_len_palindrome_string:
                     max_len_palindrome_string = len(temp_str)
                     longest_palindrome_substring = temp_str
    
    return longest_palindrome_substring




if __name__ == '__main__':
     #print(is_palindrome_string('aba'))
     s = 'aba'
     longest_palindrome_string = find_longest_palindrome_substring(s)
     print(longest_palindrome_string)
