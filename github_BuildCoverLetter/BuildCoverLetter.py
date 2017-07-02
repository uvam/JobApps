
##-----------BuildCoverLetter--Jacob J. McDermott--(2017-June-21)------------##

from boilerplate_text import *

def greeting(recipient):
    '''(str)->str
    Return customized cover letter greeting if recipient name is known.
    Return "Dear Reader," if not. '''
    
    if recipient == 'unknown':
        greeting = 'Dear Reader,'
    else:
        greeting = 'Dear ' + recipient + ','
    return greeting

def intro(boilerplate_intro, position, organization):
    '''(str,str,str)->str
    '''
    
    boilerplate_intro = boilerplate_intro.replace(
                        '(insert_position)', position
                        )    
    boilerplate_intro = boilerplate_intro.replace(
                        '(insert_org)', organization
                        )
    if is_bootcamp == True:
           boilerplate_intro = boilerplate_intro.replace(
                        '(hone_or_apply)', 'hone'
                        )
    else:
        boilerplate_intro = boilerplate_intro.replace(
                        '(hone_or_apply)', 'apply'
                        )
    position_specific_intro = boilerplate_intro.replace(
                        '(office_location)', office_location
                        )
    
    return position_specific_intro

def geobody(organization):
    '''(str)->str    '''

    if is_geology_position == True:
        geologist_specific_body = geologist_body.replace(
                                  '(insert_org)', organization
                                  )
    return geologist_specific_body 

    #TODO: If selected for interview, emphasize how complimentary 
    #      geologist experience and programming are.
    
def progbody(organization):
    '''(str)->str    '''

    if is_programming_position == True:
        programming_specific_body = programming_body.replace(
                                    '(insert_org)', organization
                                    )
    return programming_specific_body

    #TODO: If selected for interview, emphasize how complimentary 
    #      geologist experience and programming are.

def closing():
    '''() -> str'''
    programming_joke = ('What do and Python '
                        'and the eighties band "White Snake", have in common?')
    
    #TODO: Come up with punchline involving spam.
    
    joke_about_geologists = '' #...Too easy.
    idiosyncratic_skill = ('my ability to identify a respectable number of baking '
                          'supplies by touch.')
    
    if is_programming_position  == True:
        closing = boilerplate_closing.replace('insert_joke', programming_joke)       
    if is_geology_position and is_programming_position == True:
        closing = boilerplate_closing.replace(
                  'insert_joke', joke_about_geologists
                  )
        #The programming joke might be a bit obscure.       
    position_specific_closing = closing + ' ' + idiosyncratic_skill
    return position_specific_closing
def Build_Cover_Letter():
    '''() -> str
    Return cover letter text file given imputs from boilerplate_text.py'''

    import textwrap

    coverletter = open("coverletter.txt", 'w')
    coverletter.write(textwrap.fill(my_name.rjust(79), width=79))
    coverletter.write('\n')
    coverletter.write(textwrap.fill(my_address.rjust(79), width=79))
    coverletter.write('\n')
    coverletter.write(textwrap.fill(my_email.rjust(79), width=79))
    coverletter.write('\n')
    coverletter.write(textwrap.fill(my_phone.rjust(79), width=79))
    coverletter.write('\n')
    coverletter.write('\n')
    coverletter.write(textwrap.fill(greeting(recipient), width=79))
    coverletter.write('\n')
    coverletter.write('\n')
##      coverletter.write('\t') #No, use method below instead.  
    coverletter.write(
                      textwrap.fill(('\t' +
                      intro(boilerplate_intro, position, organization)), width=79)
                      )
    coverletter.write('\n')
    coverletter.write('\n')
    coverletter.write(textwrap.fill(('\t' + geobody(organization)), width=79))
    coverletter.write('\n')
    coverletter.write(textwrap.fill(('\t' + progbody(organization)), width=79))
    coverletter.write('\n')
    coverletter.write('\n')
    coverletter.write(textwrap.fill(('\t' + (closing())), width=79))
    coverletter.close()

    return coverletter

Build_Cover_Letter()                         
                           
    #TODO: Cross fingers after submittal.

    
    
