# lm_hai_evaluations
To run the filtering on acl dataset, download the anthology from [here](https://aclanthology.org/) to the datasets folder. Select the bibtex with abstracts version.

Then, run the filter_acl.py as
```
filter_acl.py > nlp_abstracts_for_keywords
```

The above will dump all the abstracts matching criteria defined in the filter_acl file. Edit the criteria as per your needs in the filter_acl script.