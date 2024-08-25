#!/usr/bin/env python

from game_data import name_dict

def find_name_in_db(first_letter):
  names_found = [n.lower() for n in list(name_dict.keys()) if n.lower().startswith(first_letter.lower())]
  if len(names_found) == 0:
    return False, []
  else:
    return True, names_found

def find_name(first_letter):
  found, found_names = find_name_in_db(first_letter)
  if found:
    msg = f"\nI found {len(found_names)} names.\n"
  else:
    msg = f"I didn't find any names that start with your first letter. :( \n ** Please Try Again! **\n "
  return msg, found, found_names

def guess_age(name):
  return 0
  # if first_letter in [name[0] for name in list(name_dict.keys())]:
  #   msg = "Found a name with your first letter. can you pleas guess the age?"
  #   dd = name_dict[
  # else:
  #   msg = "Couldn't find a name with your first letter. Please try again!"
  # return msg

def main():
  first_letter = input("\nPlease type the first letter of the person that you want to guess! \n")
  msg, found, found_names= find_name(first_letter)
  print (msg)

  if found:
    name_guessed = input("\nPlease Enter your guess! \n\n")
    if name_guessed.lower() in found_names:
      print ("\n You have guessed the name correctly. \n ** CONGRATULATIONS! **\n")
    else:
      print ("\n Please try again! GOOD BYE.\n")
if __name__ == "__main__":
  main()

    # ans = input("\n\n Type Y/N -> \n ")
    # if ans.lower() == "y":
    #   guessed_name = input("\n\n Type your guess:  -> \n")
  
