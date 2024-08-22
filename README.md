# Demyst Coding Challenge

### Step 1: 
#### Clone this git repo
```git clone https://github.com/nimmmalarohit/demyst_coding_challenge.git```


### Step 2: 
#### Change the directory to the path where Dockerfile is present
`cd demyst_coding_challenge`


### Step3: 
#### Below command builds a Docker image from the Dockerfile in the current directory.
`docker build -t data-parser-app .`


### Step 4: 
#### Run the Below command to build the Docker image for the project. This executes the tests inside a containerized environment.
`docker run --rm data-parser-app`
