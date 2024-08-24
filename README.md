

# Demyst Coding Challenge

### Code Walk through
- Source code for Problem 1 is present in `src/data_parser.py`
- Source code for Problem 2 is present in `src/data_processing.py`
- `entrypoint.sh` script serves as the entry point for running the necessary scripts in sequence.
- The `Dockerfile` defines the environment for running your Python scripts within a container.
- `test_data_parser.py` script contains unit tests for the `data_parser.py` script.
- `test_data_processing.py` script includes unit tests for the `data_processing.py` script.


### 1. Steps to run the scripts for Problem 1 and Problem 2 in local env.
-  **Step 1:** Clone this git repo<br>
``` buildoutcfg
git clone https://github.com/nimmmalarohit/demyst_coding_challenge.git
``` 


-  **Step 2**: Change the directory to the path where entrypoint.sh is present<br>
``` buildoutcfg
cd demyst_coding_challenge
```

-  **Step 3**: Run the entrypoint.sh script<br>
``` buildoutcfg
sh entrypoint.sh
```


### 2. Steps to Build and run the code for Problem 1 and Problem 2 in Docker.
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
