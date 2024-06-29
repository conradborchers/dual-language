# Dual Language

Supplementary repository for peer review.

## Folder structure and sequence 

### Step 1: Obtain public Facebook post data

For downloading the public Facebook post data, you may use the following code using
code for the CrowdTangle API: 
https://anonymous.4open.science/r/download-baseline-data/

### Step 2: Run the following scripts in sequence

* `1-access-district-webpages.ipynb`: Code to access and scrape US school districts' webpages

* `2-check-dl-in-fb-posts.py`: Code to check mentionings of dual language in public Facebook posts

* `3-analysis.ipynb`: Code to perform descriptive and inferential analyses featured in the manuscript

## Other data files from publicly available sources

* `4-elsi-21-22.csv`: Publicly available data of US school districts, including their website URLs for webscraping and demographic data

* `ccd_frpl.csv` and `crdc_lep_sum.csv`: Publicly available daa from the CCD and CRDC on free/reduced price lunch and English language learner statistics of US school districts

