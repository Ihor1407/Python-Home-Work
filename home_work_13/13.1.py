import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

        clean_text = re.sub(r'<[^>]+>', '', html)

        lines = clean_text.split('\n')
        non_empty = []

        for line in lines:
            if line.strip():
                non_empty.append(line)

        head_text = '\n'.join(non_empty)

        with codecs.open(result_file, 'w', 'utf-8') as file:
            file.write(head_text)


delete_html_tags('draft.html')
