# PCL2CSV
# Language: Python
# Input: PCL (file to convert)
# Output: CSV (converted file)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

PluMA plugin to convert PCL (Stanford cDNA file format) to CSV.
The input PCL file is assumed to be a table with rows corresponding to members of a community
and columns corresponding to samples.  Entry (i, j) in the table corresponds to the 
abundance of member i in sample j.

It will then convert this input into an equivalent output CSV file but with rows as samples
and columns as members.  It thus transposes the matrix along the way.
