
TimeBank Validation
-------------------

Note: these instructions are for Unix/Linux platforms.


1. Validation with XML Schema

To validate the TimeBank files using the schema:

	% java ValidateTimeML ../data/timeml <log_file>

This assumes version 1.4.4 of the Xerces Java Parser, available at
http://xerces.apache.org. You may first need to recompile the .java
file for your platform:

	% javac ValidateTimeML.java


2. Validation with DTD

This catches less problems but may be easier to work with for some.

To validate the TimeBank files using the DTD:

	% perl validate.pl ../data/timeml

which will write to standard output. Use "grep -v INFO-300" on the
output to filter out the reference counts. Note that the reference
counts are not always correct. There are, for example, cases of signal
ids that are referred to but that are not reported as such by the
validation script.

The script assumes the Perl module XML::Checker::Parser, avaliable
at CPAN (http://www.cpan.org). 




