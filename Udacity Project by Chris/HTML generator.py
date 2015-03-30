#Will take in data (As a list in the order of row 1, row 2, row 3...ect.) and the total number of columns and generate a HTML table 
def generate_table(data, col_length):
    table = ""
    counter = 0
    table += '<table  style="width:100%" border="3" bordercolor = "white">'
    header = False
    for element in data:
        counter += 1
        if counter >= col_length and header == False:
            table += "\n\t\t\t\t<th>%s</th>" % element
            table+= "\n\t\t\t</tr>"
            counter = 0
            header = True
        elif counter >= col_length:
            table += "\n\t\t\t\t<td>%s</td>" % element
            table+= "\n\t\t\t</tr>"
            counter = 0
        elif header == False and counter == 1:
            table += "\n\t\t\t<tr>"
            table += "\n\t\t\t\t<th>%s</th>" % element
        elif header == False:
            table += "\n\t\t\t\t<th>%s</th>" % element
        elif counter == 1:
            table += "\n\t\t\t<tr>"
            table += "\n\t\t\t\t<td>%s</td>" % element  
        else:
            table += "\n\t\t\t\t<td>%s</td>" % element
    table += '\n</table>'
    return table

#will take in data and produces a HTML unordered list
def generate_list(list_contents):
    finished_list = ""
    finished_list += "<ul>"
    for content in list_contents:
        finished_list += """
\t<li> """+ content + """</li>"""
    finished_list += """
</ul>"""
    return finished_list

#THe next three functions allow for the generation of HTML code
def generate_concept_HTML(concept_title, concept_description):
    subtitle_id = ""
    for letter in concept_title:
        if letter == " ":
            subtitle_id += "_"
        else:
            subtitle_id += letter
            
    html_text_1 = '''
        <div class="info">
            <div class="subtitle" id ="''' + subtitle_id + '''">
                <h2>''' + concept_title + '''</h2>'''
    html_text_2 = '''
            </div>

                ''' + concept_description
    html_text_3 = '''
        </div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)


def make_HTML_for_many_concepts(title, list_of_concepts):
    title_id = ""
    for letter in title:
        if letter == " " or "/":
            title_id += "_"
        else:
            title_id += letter
    HTML = '''<div class = "container">
    <div class = "title" id ="''' + title_id + '''">
        <h1> ''' +title + ''' </h1>
    </div>'''
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML += concept_HTML
    HTML += '''
</div>'''
    return HTML
