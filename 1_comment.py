# this is the single comment

# these
# are
# the
# multi
# comment

'''
These 
are 
the 
multi 
comment 
also
'''

message = "# This is not a comment because it's inside quotes"

print(message)


'''
Rule when write a comment # source https://stackoverflow.blog/2021/12/23/best-practices-for-writing-code-comments/
1. Comment not duplicate code
2. Good comment do not excuse unclear code
3. If you can't write clear comment, there may be a problem with the code
4. Comment should dispel confusion, not cause it
5. Explain unidiomatic code in comments
6. Include links to external references where they will be most helpfull
7. Add comments when fixing bug
8. Use comments to mark incomplete implementations
9. Use specific tag for specific comment ('TODO', 'FIXME', 'NOTE')

Sample no 1
    i = i + 1 # add one to i (it's wrong)

Sample no 2
    Bad
        # sum a + b
        result = a + b
    Good (comment can remove, because variable name more clear than before)
        totalPrice = productPrice + tax

Sample no 9
    # TODO: Add validation when user login
'''
