# You are given the results of a sequence of matches played by India in ODIs. A win is represented by 'W' and a loss is represented by 'L'. A winning streak is a string of consecutive wins. For example, if India has played five matches with the following results - 'WLWWWL' - then it has a three-match streak. Write a code to accept the result-sequence as input and find the longest streak in it.

# sequence = input("Enter the match sequence: ").upper()

win_streaks = sequence.split('L')
longest_streak = max(len(streak) for streak in win_streaks)

print(f"The longest winning streak is: {longest_streak}")

# op:
# Enter the match sequence: wlwwwl
# The longest winning streak is: 3
