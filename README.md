# House of Mutants GitHub
This is the GitHub repository for the Copenhagen BioHackathon 2021

## Team Members
Tanya (GitHub: [latticetower](https://github.com/latticetower))

Sven (GitHub: [sklumpe](https://github.com/sklumpe))

Thomas (GitHub: [ngthomas](https://github.com/ngthomas))

Michael (GitHub: [MSBradshaw](https://github.com/MSBradshaw))

Here, we look at two data sets of single of multi mutant sequences,
their wildtype secondary structure and biophysical descriptors to
predict stability scores of both single and multiple mutations within
the protein sequence.

## Model
We've decided that we want to focus on features and want to start with a strong baseline. We've chosen [catboost](https://catboost.ai). It gives good results out of the box, it is interpretable, feature scaling doesn't affect its performance - all because it uses gradient boosting on decision trees. It also works ok with categorical features. After that we were trying to deal with the data :slightly_smiling_face: and improve our models.

Our baseline solution also uses N-fold cross-validation, for each score 

### Single mutants
The performance of our current best solution for single mutants test file is shown on the plot:
![Plot with our best model performance on the test set (single mutants)](images/single-mutants-best-solution.png)

### Multiple mutants
The performance of our current best solution for multiple mutants test file is shown on the plot:
![Plot with our best model performance on the test set (multiple mutants)](images/multiple-mutants-best-solution.png)

### Things we wanted to do to run the world, but didn't finish


## Misc
Please also see the our team's [BioLib page](https://biolib.com/house-of-mutants-mt24/house-of-mutants/) for further information
