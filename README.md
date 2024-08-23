

# Demyst Coding Challenge

- Source code for Problem 1 is present in `src/data_parser.py`
- Source code for Problem 2 is present in `src/data_processing.py`


#### Steps to Build and run the code for Problem 1 and Problem 2 in Docker.


-  **Step 1:** Clone this git repo<br>
``` buildoutcfg
git clone https://github.com/nimmmalarohit/demyst_coding_challenge.git
``` 


-  **Step 2**: Change the directory to the path where Dockerfile is present<br>
``` buildoutcfg
cd demyst_coding_challenge
```


- **Step3**: Below command builds a Docker image from the Dockerfile in the current directory.<br>
``` buildoutcfg
docker build -t demyst-app .
```


-  **Step 4**: This executes the tests and runs code for problem 1 and 2 inside a containerized environment.<br>
``` buildoutcfg
docker run --rm demyst-app
```
