# Cloud Computing Project
## Mini-project 1: First Cloud Function
### Part 1: Create a Cloud Function
Description: Post a cloud function that takes in a *string* of numbers and returns and returns a *json file* that contains the *sum* of all of the single digit numbers. 

Example: 
* Input: `12345`
* Output: `{"answer": 15}`

### Part 2: Query your Cloud Function
Do a `GET` request to your cloud function with a input `012937`, `2` and `9999999999999`.

### Part 3: Adding a collaborator to your Cloud function
Add your professor as a collaborator to your cloud function via the IAM page.

## How to test?

Create new conda environment.

```bash
conda create --my-first-gcf --clone base
```

Then, activate the new environment:

```bash
conda activate my-first-gcf
```

Now, install the required packages:

```bash
pip install functions-framework flask
```
Move to this folder and run:

```bash
functions-framework --target first_cloud_function --debug
```

Then run the testing script in `./test/first_function.py`

```bash
python ./test/first_function.py
```