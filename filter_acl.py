import re
import pdb

def extract_matching_entries(file_path, criteria):
    with open(file_path, 'r') as file:
        content = file.read()

    bib_entries = re.findall(r'@\w+\{([^,]+),\s*([\s\S]+?)\n\}', content)

    unique_criterias = set([field_name for field_name, _ in criteria])
    matching_entries = []
    for entry in bib_entries:
        fields = [field.strip() for field in entry[1].split(',')]
        criteria_found = {}
        for criterion in criteria:
            field_name, condition = criterion
            for field in fields:
                if field.startswith(field_name) and re.search(condition, field, re.IGNORECASE):
                    criteria_found[field] = 1
                    break

        if len(criteria_found) == len(unique_criterias):
            matching_entries.append(entry)

    return matching_entries

# Example usage
file_path = 'datasets/anthology+abstracts.bib'  # Replace with the path to your text file
criteria = [
    ('booktitle =', r'Proceedings of the 20(18|19|20|21|22|23) Conference on Empirical Methods in Natural Language Processing'), # Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, Proceedings of the (58th|59th|60th) Annual Meeting of the Association for Computational Linguistics
    ('booktitle =', r'Proceedings of the (53rd|54th|55th|56th|57th|58th|59th|60th) Annual Meeting of the Association for Computational Linguistics'),
    #('booktitle =', r'long papers'),
    #('title =', 'evaluation'),
    ('abstract =', 'persona'),
    #('abstract =', 'demographics')
    #('title =', r'\b\d{4}\.acl-long\.\d+\b')  # '2022.acl-long.419'
]
matching_entries = extract_matching_entries(file_path, criteria)

# Print the matching entries
for entry in matching_entries:
    print(entry[0])  # Print the entry key
    print(entry[1])  # Print the entry content
    print('---')