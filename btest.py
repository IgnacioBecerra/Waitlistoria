import mechanize
import sys

br = mechanize.Browser()

#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('user-agent', '   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'),
('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

br.open('https://act.ucsd.edu/scheduleOfClasses/scheduleOfClassesStudent.htm')

for form in br.forms():
    if form.attrs.get('id') == 'socFacSearch':
        br.form = form
        break


#br.set_debug_http(True)
#br.set_debug_responses(True)

br.form['courses'] = "CSE 100"
#br['selectedTerm'] = 'WI18'

print br.form


response = br.submit()
#print response.read()

#sys.stdout=open("test.txt","w")
print response.read()
#sys.stdout.close()