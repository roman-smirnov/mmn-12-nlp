# Maman 12 Code Solutions Spec and Verification 

+ This code project provides the class spec for question one and all of the bonus code questions alike. The spec is located at `submission_specs/SubmissionSpec12`, and you should make sure that your solution/s inherit and implement this class. An example of inheriting the class is present in file `solution12.py`

+ It provides for you a way to **run and therefore verify your submission** before submitting it, the same way as it will be run for automated grading. 

+ And it bypasses the need for you to fetch, filter and parse the input corpus, by delivering input data directly to your API endpoints.

## Usage

From an anaconda terminal or terminal where your python environment and this code project are available, run:

```
python go.py
```

Note that a progress bar is shown as you run this. If you are running the project inside of an IDE, you may need to remove the call to `tqdm` in the supplied code, to avoid the progress bar and IDE crashing each other. 

Replace the supplied content of `solution12.py` with your own solution, which should implement a class named `Submission`, inheriting and implementing the spec class `SubmissionSpec12`.

## How to Submit your Code

+ Just like in this code project as supplied, your solution code should be a class named `Submission` and it will be read and invoked from file `solution12.py`. If you include additional python files or classes in your solution, that is perfectly fine as long as the entry point is as just defined and follows the spec.

+ See the accompanying document for the overall zip structure where you will simply _embed_ your code solution without additional requirements to those above. 

+ For any of the code bonus questions, use the same spec (with empty methods for `_estimate_emission_probabilites` and `_estimate_transition_probabilites` which are not needed in the case of an MEMM). Each question will be submitted as a separate code project fulfilling this spec in full, just in a separate path in the zip file envelope.

